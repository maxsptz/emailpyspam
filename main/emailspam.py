# Import statements
import smtplib
from email.message import EmailMessage
import random
import time
import getpass
import sys
import os
try:
    from tabulate import tabulate
except ModuleNotFoundError:
    table = False
else:
    table = True
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    loadingBar = False
else:
    loadingBar = True

# Colour Scheme

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #-----
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'

# Functions

def banner():
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')
    try:
        file1 = open('banner.txt', 'r')
        print(' ')
        print(bcolors.OKGREEN + file1.read() + bcolors.ENDC)
        file1.close()
    except IOError:
        print( bcolors.FAIL + 'Banner File not found!' + bcolors.ENDC)

def validChoice(ch):
    valid = False
    while not valid:
        if ch == "1" or ch == "2" or ch == "3" or ch == "#":
            valid = True
        else:
            print (bcolors.FAIL + "Invalid choice!" + bcolors.ENDC)
            time.sleep(0.5)
            ch = input(bcolors.FAIL + "Enter a valid choice: " + bcolors.ENDC)
    return ch

def validMultiple(mult):
    valid = False
    while not valid:
        if mult == "1" or mult.upper() == "YES" or mult == "2" or mult.upper() == "NO":
            valid = True
        else:
            print (bcolors.FAIL + "Invalid choice!" + bcolors.ENDC)
            time.sleep(0.5)
            mult = input(bcolors.FAIL + "Enter a valid choice: " + bcolors.ENDC)
    return mult

def validRecipientNum(to_addr,recipientNum,choice):
    valid = False
    while not valid:
        message = False
        if recipientNum > 0:
            if choice == "1":
                if recipientNum <= 500:
                    valid = True
                else:
                    message = True
            elif choice == "2" or choice == "3":
                if recipientNum <= 100:
                    valid = True
                else:
                    message = True
        else:
            message = True
        if message:
            print (bcolors.FAIL + "Invalid number of recipients! You must start over.\n" + bcolors.ENDC)
            time.sleep(0.5)
            to_addr = []
            while True:
                addr = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish: " + bcolors.ENDC)
                if not addr:
                    break
                else:
                    to_addr.append(addr)
            recipientNum = len (to_addr)
            valid = False
    return to_addr,recipientNum

def validSend(send,multiple,recipientNum,numOfSenders):
    valid = False
    while not valid:
        message = False
        try:
            int (send)
        except ValueError:
            message = True
        else:
            send = int (send)
            if send > 0:
                if send % recipientNum == 0:
                    if (send * recipientNum) < (500 * numOfSenders):
                        valid = True
                    else:
                        message = True
                else:
                    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count (e.g. 1 email with 2 recipients counts as 2 emails)." + bcolors.ENDC)
                    print (bcolors.FAIL + "Amount can't be evenly distributed to recipients!"\
                    "\ne.g. 5 emails can't be evenly distributed to 2 recipients" + bcolors.ENDC)
                    time.sleep(0.5)
                    send = input(bcolors.FAIL + "Enter the number of emails you want to send: " + bcolors.ENDC)
                    valid = False
            else:
                message = True
        if message:
            print (bcolors.FAIL + "Invalid amount!" + bcolors.ENDC)
            print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count (e.g. 1 email with 2 recipients counts as 2 emails)." + bcolors.ENDC)
            time.sleep(0.5)
            send = input(bcolors.FAIL + "Enter the number of emails you want to send: " + bcolors.ENDC)
            valid = False
    return send

def validSpeed(s):
    valid = False
    while not valid:
        try:
            float (s)
        except ValueError:
            print (bcolors.FAIL + "Invalid number for speed!" + bcolors.ENDC)
            time.sleep(0.5)
            s = input(bcolors.FAIL + "At what interval should the emails get sent out? (seconds): " + bcolors.ENDC)
        else:
            s = float (s)
            valid = True
    return s

def validGmail(from_addr,cipher):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Start TLS for security
    server.starttls()
    try:
        server.login(from_addr, cipher)
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Try again" + bcolors.ENDC)
        valid = False
    else:
        valid = True
    return valid


def recipientLists():
    print(bcolors.WARNING + '\nManage predefined recipient lists: ')
    print("""
    1) Create new recipient list
    2) Delete existing recipient list
    3) Edit existing recipient list
    4) List all existing recipient lists
    5) Exit
    """ + bcolors.ENDC + '--------------------------------------------------------------')
    option = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return option

def createRList():
    sure = "N"
    recipientLists = {}
    while sure.upper() != "Y":
        nameList = input("Name of list: ")
        rList = []
        while True:
            entry = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish: " + bcolors.ENDC)
            if not thing:
                break
            else:
                rList.append(ent)


        sure = input("Are you sure? (Y/N): ")
        if sure.upper() == "N":
            break
        elif sure.uppper() == "Y":
            racipientLists[nameList] = rList

def deleteRList():
    print("Working on it")

def editRList():
    print("Working on it")

def listRLists():
    print("Working on it")



# Choose Mail Service

def mailChoice():
    print(bcolors.WARNING + '''
    Choose an Option:
    1) Gmail Spammer
    2) Yahoo Spammer
    3) Outlook/Hotmail Spammer
    #) Recipients Editor
    ''' + bcolors.ENDC + '--------------------------------------------------------------')
    choice = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return choice

def legacy(choice):
    if choice == "2" or choice == "3":
        print(bcolors.FAIL + bcolors.BOLD + 'The development team has decided to depreciate this feature as we have run into too many errors with this mail service.' + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + "If you would like to try and fix the errors or test these mail services, do the following:"\
         '\n • Refer to our "legacy" branch' + bcolors.ENDC, end = " (")
        print(bcolors.URL + "https://github.com/Curioo/emailpyspam/tree/legacy" + bcolors.ENDC, end = ")\n")
        print(bcolors.FAIL + bcolors.BOLD + ' • Access the original code for this service'\
        '\n(• Submit a pull request)'+ bcolors.ENDC)
        time.sleep(1)
        sys.exit()

# Gmail DISCLAIMER

def gmailInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: To send emails with Gmail, you need to enable less secure apps:\n" + bcolors.ENDC)
    print(bcolors.URL + "https://myaccount.google.com/lesssecureapps" + bcolors.ENDC)
    print(bcolors.FAIL + "\nDISCLAIMER: Gmail has a limit of 500 emails per day per account" + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count (e.g. 1 email with 2 recipients counts as 2 emails)." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(If so, emails and passwords must be predefined in gmail.txt and gmailpass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Surpass Limit with multiple emails (Gmail)

def gMultiple():
    global emailnum
    global passnum
    try:
        file = open("gmail.txt", "r")
        fileStuff = file.readline()
        fileStuff = file.readline()
        gmail = fileStuff.split(",")
        emailnum += 1
        from_addr = gmail[emailnum]
        numOfSenders = len (gmail)
        if gmail[-1] == "\n" or gmail[-1] == "":
            numOfSenders -= 1
        file.close()
    except IOError:
        print (bcolors.FAIL + "gmail.txt not found! Exiting..." + bcolors.ENDC)
        sys.exit()
    try:
        passFile = open("gmailpass.txt", "r")
        passFileStuff = passFile.readline()
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print (bcolors.FAIL + "gmailpass.txt not found! Exiting..." + bcolors.ENDC)
        sys.exit()

    return from_addr,cipher,numOfSenders

# Send with limits (Gmail)

def gSingle():
    valid = False
    while not valid:
        from_addr = input(bcolors.OKGREEN + 'Your Google Email: ' + bcolors.ENDC)
        cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
        valid = validGmail(from_addr,cipher)
    numOfSenders = 1
    return from_addr,cipher,numOfSenders

# Main structure (subject, body, etc.)

def structure(choice,numOfSenders):
    to_addr = []
    addr = ""
    number = random.randint(0, 10000)
    while True:
        addr = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish: " + bcolors.ENDC)
        if not addr:
            break
        else:
            to_addr.append(addr)
    recipientNum = len (to_addr)
    to_addr,recipientNum = validRecipientNum(to_addr,recipientNum,choice)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    limit = input(bcolors.OKGREEN + "Would you like to send a specific number of emails? (Y/N): " + bcolors.ENDC)
    if limit.lower() == "y":
        send = input(bcolors.FAIL + "Enter the number of emails you want to send: " + bcolors.ENDC)
        send = validSend(send,choice,multiple,recipientNum,numOfSenders)
    else:
        send = float ("inf")
    predef = input(bcolors.OKGREEN + 'Would you like to use the subject saved in subject.txt? (Y/N): ' + bcolors.ENDC)
    if predef.lower() == 'y':
        try:
            p_reader = open("subject.txt", 'r')
            subject = p_reader.readline()
            index = len(subject) - 1
            subject = subject[0:index]
            p_reader.close()
            length = len (subject)
            subject += ' (' + str(number) + ')'
        except IOError:
            print (bcolors.FAIL + "subject.txt not found! Exiting..." + bcolors.ENDC)
            sys.exit()
    else:
        subject = input(bcolors.OKGREEN + 'Subject: ' + bcolors.ENDC)
        length = len (subject)
        subject += ' (' + str(number) + ')'

    predef1 = input(bcolors.OKGREEN + 'Would you like to use the body saved in body.txt? (Y/N): ' + bcolors.ENDC)

    if predef1.lower() == 'y':
        try:
            f = open("body.txt", "r")
            body = f.read()
            f.close()
        except IOError:
            print (bcolors.FAIL + "body.txt not found! Exiting..." + bcolors.ENDC)
            sys.exit()
    else:
        body = input(bcolors.OKGREEN + 'Body: ' + bcolors.ENDC)
    speed = input(bcolors.FAIL + "At what interval should the emails get sent out? (seconds): " + bcolors.ENDC)
    speed = validSpeed(speed)

    print(bcolors.WARNING + "Emails will be sent continuously, until this window is closed." + bcolors.ENDC)
    time.sleep(1)
    return speed,to_addr,body,subject,length,recipientNum,send

# Main Spammer (Gmail)

def gmailSpam(speed,from_addr,to_addr,body,subject,length,cipher,recipientNum):
        global sent
        global Sent
        number = random.randint(0, 10000)
        subject = subject[0:length] + " (" + str(number) + ")"
        # Construct email
        msg = EmailMessage()
        msg.add_header('From', from_addr)
        msg.add_header('To', ', '.join(to_addr))
        msg.add_header('Subject', subject)
        msg.set_payload(body)
        # Connect
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS for security
        server.starttls()
        try:
            server.login(from_addr, cipher)
            server.send_message(msg, from_addr=from_addr, to_addrs=to_addr)
            server.quit()
            sent += (1*recipientNum)
            Sent += (1*recipientNum)
            time.sleep(speed)
        except smtplib.SMTPAuthenticationError:
            print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            print(bcolors.FAIL + "\nThe recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
            sys.exit()

# Main Program
try:
    sent = 0
    Sent = 0
    emailnum = -1
    passnum = -1
    banner()
    choice = mailChoice()
    choice = validChoice(choice)
    legacy(choice)
    if choice == "#":
        option = recipientLists()
        while option != "5":
            if option == "1":
                createRList()
            elif option == "2":
                deleteRList()
            elif option == "3":
                editRList()
            elif option == "4":
                listRLists()
            else:
                print(bcolors.FAIL + "\nInvalid choice!\n" + bcolors.ENDC)
            option = recipientLists()

    # Gmail
    if choice == "1":
        multiple = gmailInstruct()
        multiple = validMultiple(multiple)
        if multiple == "1" or multiple.upper() == "YES":
            from_address,password,numOfSenders = gMultiple()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if loadingBar and send != float ("inf"):
                pbar = tqdm(total=(send/recipientNum))
            elif table and recipientNum <= 2:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent + bcolors.ENDC)
            spam = True
            while spam is True and Sent < send:
                if from_address == "" or from_address == "\n":
                    spam = False
                else:
                    try:
                        gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                        if loadingBar and send != float ("inf"):
                            pbar.update(1)
                        elif table and recipientNum <= 2:
                            print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                        else:
                            print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent + bcolors.ENDC)
                    except smtplib.SMTPSenderRefused:
                        print ("Limit reached. Switching emails...")
                        from_address,password,numOfSenders = gMultiple()
                        spam = True
                        sent = 0
                    except smtplib.SMTPDataError:
                        print ("Limit reached. Switching emails...")
                        from_address,password,numOfSenders = gMultiple()
                        spam = True
                        sent = 0
                    if sent == 500:
                        from_address,password,numOfSenders = gMultiple()
                        spam = True
                        sent = 0
            if loadingBar and send != float ("inf"):
                pbar.close()
        elif multiple == "2" or multiple.upper() == "NO":
            from_address,password,numOfSenders = gSingle()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if loadingBar and send != float ("inf"):
                pbar = tqdm(total=(send/recipientNum))
            elif table and recipientNum <= 2:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent + bcolors.ENDC)
            while sent != 500 and Sent < send:
                try:
                    gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                    if loadingBar and send != float ("inf"):
                        pbar.update(1)
                    elif table and recipientNum <= 2:
                        print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                    else:
                        print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent + bcolors.ENDC)
                except smtplib.SMTPSenderRefused:
                    print ("Limit reached. Exiting...")
                    sys.exit()
                except smtplib.SMTPDataError:
                    print ("Limit reached. Exiting...")
                    sys.exit()
            if loadingBar and send != float ("inf"):
                pbar.close()
        else:
            print (bcolors.FAIL + "Invaid choice!" + bcolors.ENDC)
            sys.exit()
except KeyboardInterrupt:
    print(bcolors.FAIL + "\nCancelled!" + bcolors.ENDC)
    sys.exit()

# Add an option to give a submenu to user to choose from predefined recipient list
