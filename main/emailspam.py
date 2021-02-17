# Import statements
import smtplib
from email.message import EmailMessage
import random
import time
import getpass
import sys
import os
import optparse

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
def resize():
    cmdsize = os.get_terminal_size()
    num = 0
    col = ""
    lin = ""
    for c in range (len (cmdsize)):
        try:
            if cmdsize[c] == "=":
                num += 1
            int (cmdsize[c])
        except ValueError:
            "Placeholder"
        else:
            if num == 1:
                col += str (cmdsize[c])
            else:
                lin += str (cmdsize[c])
    if sys.platform.startswith('win32'):
        if col < "123" or lin < "35":
            os.system('mode con:cols=123 lines=35')
    else:
        """if col < "123" or lin < "49":
            os.system("printf '\e[8;49;123t'")"""

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

def validRecipientNum(to_addr,recipientNum):
    valid = False
    while not valid:
        message = False
        if 0 < recipientNum <= 500:
            valid = True
        else:
            message = True
        if message:
            print (bcolors.FAIL + "Invalid number of recipients! You must start over.\n" + bcolors.ENDC)
            time.sleep(0.5)
            to_addr = []
            addr = ""
            number = random.randint(0, 10000)
            while True:
                addr = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish (or \"#\" to use a predefined recipient list): " + bcolors.ENDC)
                if addr == "#":
                    recipients = listSelector(recipientLists)
                    if recipients != "normal":
                        to_addr = recipients
                        break
                elif not addr:
                    save = input (bcolors.OKGREEN + "\nDo you want to save these recipients to a new recipient list? (Y/N): " + bcolors.ENDC)
                    if save.upper() == "Y":
                        nameList = input (bcolors.OKGREEN + "\nName of new list: " + bcolors.ENDC)
                        if nameList in recipientLists:
                            print (bcolors.FAIL + "\nList already exists!\n" + bcolors.ENDC)
                        else:
                            print ("\n" + bcolors.OKGREEN + nameList + ":",end = " ")
                            print (to_addr)
                            print ("" + bcolors.ENDC,end = "")
                            sure = input(bcolors.REDBG + "\nAre you sure? (Y/N): " + bcolors.ENDC)
                            if sure.upper() == "Y":
                                recipientLists[nameList] = to_addr
                                saveRescipientLists()
                    break
                else:
                    to_addr.append(addr)
    return to_addr,recipientNum

def validSend(send,multiple,recipientNum):
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
                if send < 500:
                    valid = True
                else:
                    message = True
            else:
                message = True
        if message:
            print (bcolors.FAIL + "Invalid amount!" + bcolors.ENDC)
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
        print(bcolors.FAIL + "\nThe email / password you have entered is incorrect\nor access to less secure apps is disabled! Try again" + bcolors.ENDC)
        valid = False
    else:
        valid = True
    return valid

def resetAllLists():
    global recipientLists
    try:
        while ("recipientLists.txt"):
            os.remove ("recipientLists.txt")
    except FileNotFoundError:
        print (bcolors.WARNING + "\nLists successfully deleted" + bcolors.ENDC)
    recipientLists = {}
    saveRescipientLists()

def saveRescipientLists():
    f = open ("recipientLists.txt", "w")
    for thing in range (len (sorted (recipientLists))):
        f.write (sorted (recipientLists)[thing] + ":")
        for things in range (len (recipientLists[sorted (recipientLists)[thing]])):
            f.write (recipientLists[sorted (recipientLists)[thing]][things] + ":")
        f.write ("\n")
    f.close()

def recipientEditor(recipientLists):
    print(bcolors.WARNING + '''
    Choose an Option:
    1) Add a list of recipients
    2) Edit list of recipients
    3) Delete a list of recipients
    4) View all lists
    5) Quit recipient editor
    #) Delete all saved lists
    ''' + bcolors.ENDC + '--------------------------------------------------------------')
    option = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)

    while option != "5":
        if option == "1":
            nameList = input(bcolors.OKGREEN + "\nName of new list: " + bcolors.ENDC)
            if nameList in recipientLists:
                print (bcolors.FAIL + "\nList already exists!\n" + bcolors.ENDC)
            else:
                rList = []
                while True:
                    entry = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish: " + bcolors.ENDC)
                    if not entry:
                        break
                    else:
                        rList.append(entry)
                print ("\n" + bcolors.OKGREEN + nameList + ":",end = " ")
                print (rList)
                print ("" + bcolors.ENDC,end = "")
                sure = input(bcolors.REDBG + "\nAre you sure? (Y/N): " + bcolors.ENDC)
                if sure.upper() == "Y":
                    recipientLists[nameList] = rList
                    saveRescipientLists()
                else:
                    break
        elif option == "2":
            if len (recipientLists) == 0:
                print (bcolors.FAIL + "\nYou don't have any saved lists yet!\n" + bcolors.ENDC)
            else:
                wantEdit = input(bcolors.OKGREEN + '\nEnter the name of the list you would like to edit: ' + bcolors.ENDC)
                if wantEdit not in recipientLists:
                    print (bcolors.FAIL + "\nList not found!\n" + bcolors.ENDC)
                else:
                    print ("\n" + bcolors.OKGREEN + wantEdit + ":",end = " ")
                    print (recipientLists[wantEdit])
                    print ("" + bcolors.ENDC,end = "")
                    print(bcolors.WARNING + '''
                    Choose an Option:
                    1) Add a recipient
                    2) Delete a recipient
                    3) Exit
                    ''' + bcolors.ENDC + '--------------------------------------------------------------')
                    opt = input (bcolors.OKGREEN + "\nNumber: " + bcolors.ENDC)
                    while opt != "3":
                        if opt == "1":
                            edit = input (bcolors.OKGREEN + "\nEnter new recipient: " + bcolors.ENDC)
                            rlist = recipientLists[wantEdit]
                            if edit in rlist:
                                print (bcolors.FAIL + "\nRecipient already in list!\n" + bcolors.ENDC)
                            else:
                                rlist.append (edit)
                                recipientLists[wantEdit] = rlist
                                print (bcolors.OKGREEN + '\nCurrent list:\n')
                                print (recipientLists[wantEdit])
                                print ("" + bcolors.ENDC,end = "")
                                saveRescipientLists()
                        elif opt == "2":
                            if len (recipientLists[wantEdit]) == 0:
                                print (bcolors.FAIL + "\nYou don't have any recipients in this list yet!\n" + bcolors.ENDC)
                            else:
                                edit = input (bcolors.OKGREEN + "\nEnter recipient you wish to delete: " + bcolors.ENDC)
                                rlist = recipientLists[wantEdit]
                                if edit not in rlist:
                                    print (bcolors.FAIL + "\nRecipient not found!\n" + bcolors.ENDC)
                                else:
                                    rlist.remove (edit)
                                    recipientLists[wantEdit] = rlist
                                print (bcolors.OKGREEN + '\nCurrent list:\n')
                                print (recipientLists[wantEdit])
                                print ("" + bcolors.ENDC,end = "")
                                saveRescipientLists()
                        else:
                            print (bcolors.FAIL + "\nInvaid choice!\n" + bcolors.ENDC)
                        print(bcolors.WARNING + '''
                        Choose an Option:
                        1) Add a recipient
                        2) Delete a recipient
                        3) Exit
                        ''' + bcolors.ENDC + '--------------------------------------------------------------')
                        opt = input (bcolors.OKGREEN + "\nNumber: " + bcolors.ENDC)
        elif option == "3":
            if len (recipientLists) == 0:
                    print (bcolors.FAIL + "\nYou don't have any saved lists yet!\n" + bcolors.ENDC)
            else:
                wantDel = input (bcolors.OKGREEN + "\nEnter the name of the list you would like to delete: " + bcolors.ENDC)
                if wantDel not in recipientLists:
                    print (bcolors.FAIL + "\nList not found" + bcolors.ENDC)
                else:
                    print ("\n" + bcolors.OKGREEN + wantDel + ":",end = " ")
                    print (recipientLists[wantDel])
                    print ("" + bcolors.ENDC,end = "")
                    print (bcolors.REDBG + "\nAre you sure? (Y/N):" + bcolors.ENDC, end = " ")
                    sure = input ()
                    if sure.upper() == "Y":
                        del recipientLists[wantDel]
                        saveRescipientLists()
                    else:
                        break
        elif option == "4":
            if len (recipientLists) == 0:
                    print (bcolors.FAIL + "\nYou don't have any saved lists yet!\n" + bcolors.ENDC)
            else:
                keys = sorted (recipientLists)
                for list in range (len (keys)):
                    print ("")
                    k = keys[list]
                    print (bcolors.OKGREEN + k,"\n-",end = "" )
                    print (("-")*len (k),end = "")
                    print ("-" + bcolors.ENDC)
                    for entry in range (len (recipientLists[k])):
                        print (bcolors.OKGREEN + recipientLists[k][entry] + bcolors.ENDC)
                time.sleep(1.5)
        elif option == "#":
            print (bcolors.REDBG + "\nAre you sure? (Y/N):" + bcolors.ENDC, end = " ")
            sure = input ()
            if sure.upper() == "Y":
                resetAllLists()
                recipientLists = {}
        else:
            print (bcolors.FAIL + "\nInvaid choice!\n" + bcolors.ENDC)
        time.sleep(0.5)
        print(bcolors.WARNING + '''
        Choose an Option:
        1) Add a list of recipients
        2) Edit list of recipients
        3) Delete a list of recipients
        4) View all lists
        5) Quit recipient editor
        #) Delete all saved lists
        ''' + bcolors.ENDC + '--------------------------------------------------------------')
        option = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')
    banner()
    return recipientLists

def listSelector(recipientLists):
    if len (recipientLists) == 0:
            print (bcolors.FAIL + "\nYou don't have any saved lists yet.\n" + bcolors.ENDC)
            openEditor = input (bcolors.GREEN + "Would you like to enter the recipient list editor? (Y/N): " + bcolors.ENDC)
            if openEditor.upper() == "Y":
                recipientLists = recipientEditor(recipientLists)
                Continue = True
            else:
                Continue = False
    else:
        Continue = True
    if Continue:
        wantUse = input (bcolors.OKGREEN + "\nEnter the name of the list you would like to use (or \"#\" to show all existing lists): " + bcolors.ENDC)
        while wantUse == "#":
            keys = sorted (recipientLists)
            for list in range (len (keys)):
                print ("")
                k = keys[list]
                print (bcolors.OKGREEN + k,"\n-",end = "" )
                print (("-")*len (k),end = "")
                print ("-" + bcolors.ENDC)
                for entry in range (len (recipientLists[k])):
                    print (bcolors.OKGREEN + recipientLists[k][entry] + bcolors.ENDC)
            wantUse = input (bcolors.OKGREEN + "\nEnter the name of the list you would like to use (or \"#\" to show all existing lists): " + bcolors.ENDC)
        if wantUse not in recipientLists:
            print (bcolors.FAIL + "\nList not found" + bcolors.ENDC)
            recipients = "normal"
        else:
            print ("\n" + bcolors.OKGREEN + wantUse + ":",end = " ")
            print (recipientLists[wantUse])
            print ("" + bcolors.ENDC,end = "")
            print (bcolors.REDBG + "\nAre you sure? (Y/N):" + bcolors.ENDC, end = " ")
            sure = input ()
            if sure.upper() == "Y":
                recipients = recipientLists[wantUse]
            else:
                recipients = "normal"
    else:
        recipients = "normal"
    return recipients

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

def legacy():
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
    print(bcolors.FAIL + "\nNOTE: To send emails with Gmail, you need to enable less secure apps:\n" + bcolors.ENDC)
    print(bcolors.URL + "https://myaccount.google.com/lesssecureapps" + bcolors.ENDC)
    print(bcolors.FAIL + "\nDISCLAIMER: Gmail has a limit of 500 emails per day per account" + bcolors.ENDC)
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
        cipher = getpass.getpass(bcolors.OKGREEN + 'Password (Note: Input is hidden):' + bcolors.ENDC)
        valid = validGmail(from_addr,cipher)
    numOfSenders = 1
    return from_addr,cipher,numOfSenders

# Main structure (subject, body, etc.)

def structure(recipientLists):
    to_addr = []
    addr = ""
    number = random.randint(0, 10000)
    cnt = 0
    while True:
        if cnt == 0:
            addr = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish (or \"#\" to use a predefined recipient list): " + bcolors.ENDC)
            cnt += 1
        else:
            addr = input(bcolors.OKGREEN + "Type in the recipient(s), hit enter to finish: " + bcolors.ENDC)
            cnt += 1
        if addr == "#" and cnt == 1:
            recipients = listSelector(recipientLists)
            if recipients != "normal":
                to_addr = recipients
                break
        elif not addr:
            save = input (bcolors.OKGREEN + "\nDo you want to save these recipients to a new recipient list? (Y/N): " + bcolors.ENDC)
            if save.upper() == "Y":
                nameList = input (bcolors.OKGREEN + "\nName of new list: " + bcolors.ENDC)
                if nameList in recipientLists:
                    print (bcolors.FAIL + "\nList already exists!\n" + bcolors.ENDC)
                else:
                    print ("\n" + bcolors.OKGREEN + nameList + ":",end = " ")
                    print (to_addr)
                    print ("" + bcolors.ENDC,end = "")
                    sure = input(bcolors.REDBG + "\nAre you sure? (Y/N): " + bcolors.ENDC)
                    if sure.upper() == "Y":
                        recipientLists[nameList] = to_addr
                        saveRescipientLists()
            break
        else:
            to_addr.append(addr)
    recipientNum = len (to_addr)
    to_addr,recipientNum = validRecipientNum(to_addr,recipientNum)
    bcc = input(bcolors.OKGREEN + "Would you like recipients to not see other recipients (use BCC header)? (Y/N): " + bcolors.ENDC)
    if bcc.lower() == "y":
        bcc = "BCC"
    else:
        bcc = "To"
    limit = input(bcolors.OKGREEN + "Would you like to send a specific number of emails? (Y/N): " + bcolors.ENDC)
    if limit.lower() == "y":
        send = input(bcolors.FAIL + "Enter the number of emails you want to send: " + bcolors.ENDC)
        send = validSend(send,multiple,recipientNum)
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
    return speed,to_addr,body,subject,length,recipientNum,send,bcc

# Main Spammer (Gmail)

def gmailSpam(speed,from_addr,to_addr,body,subject,length,cipher,bcc):
        global sent
        global Sent
        number = random.randint(0, 10000)
        subject = subject[0:length] + " (" + str(number) + ")"
        msg = EmailMessage()
        msg.add_header('From', from_addr)
        if bcc != "BCC": msg.add_header('To', ', '.join(to_addr))
        msg.add_header('Subject', subject)
        msg.set_payload(body)
        # Connect
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS for security
        server.starttls()
        try:
            server.login(from_addr, cipher)
            server.send_message(msg, from_addr = from_addr, to_addrs = to_addr)
            server.quit()
            sent += (1)
            Sent += (1)
            time.sleep(speed)
        except smtplib.SMTPAuthenticationError:
            print(bcolors.FAIL + "\nThe email / password you have entered is incorrect\nor access to less secure apps is disabled!\nExiting..." + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            print(bcolors.FAIL + "\nThe recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
            sys.exit()

def getops(): #Get options and turn off interactive mode
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interactive', default=False, action='store_true', dest='interactive', help='this choice negates interactive mode')
    parser.add_option('-t', '--to', action='append', dest='to_address', help='the email address you are spamming e.x.: email@gmail (cannot contain .com)')
    parser.add_option('-f', '--from', type='string', dest='from_address', help='the email you are spamming from')
    parser.add_option('-d', '--interval', type='int', dest='sendSpeed', help='the interval in seconds in which you want to send the emails')#this cant be set to i cause interactive mode is set to i as well
    parser.add_option('-p', '--password', type='string', dest='password', help='the password for the email account you are spamming from')
    parser.add_option('-s', '--subject', type='string', dest='subject', help='the subject of the email you want to spam')
    parser.add_option('-b', '--body', type='string', dest='body', help='the actual message inside the email you wish to spam')
    parser.add_option('-e', '--num-of-emails', dest='recipientNum', help='the number of email addresses you want to send from')
    parser.add_option('-n', '--num', type='int', dest='send', help='the number of emails you wish to send')
    (options, arguments) = parser.parse_args()
    return options

# Main Program
try:
    sent = 0
    Sent = 0
    ops = getops()
    emailnum = -1
    passnum = -1
    if (ops.interactive == False):
        resize()
        banner()
        choice = mailChoice()
        choice = validChoice(choice)
        try:
            recipientLists = {}
            f = open("recipientLists.txt", "r")
            for l in f:
                line = l.split(":")
                line.remove ("\n")
                values = []
                key = line[0]
                line.remove (key)
                for v in range (len (line)):
                    val = line[v]
                    values.append (val)
                recipientLists[key] = values
            f.close()
        except IOError:
            recipientLists = {}
            saveRescipientLists()
        while choice == "#":
            recipientLists = recipientEditor(recipientLists)
            choice = mailChoice()
            choice = validChoice(choice)
        if choice == "2" or choice == "3":
            legacy()
        # Gmail
        if choice == "1":
            multiple = gmailInstruct()
            multiple = validMultiple(multiple)
            if multiple == "1" or multiple.upper() == "YES":
                from_address,password,numOfSenders = gMultiple()
                sendSpeed,to_address,body,subject,length,recipientNum,send,bcc = structure(recipientLists)
                if loadingBar and send != float ("inf"):
                    pbar = tqdm(total=(send))
                elif table and recipientNum <= 2:
                    print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
                else:
                    print (bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",str (Sent) + bcolors.ENDC)
                spam = True
                while spam is True and Sent < send:
                    if from_address == "" or from_address == "\n":
                        spam = False
                    else:
                        try:
                            gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,bcc)
                            if loadingBar and send != float ("inf"):
                                pbar.update(1)
                            elif table and recipientNum <= 2:
                                print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                            else:
                                print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",str (Sent) + bcolors.ENDC)
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
                sendSpeed,to_address,body,subject,length,recipientNum,send,bcc = structure(recipientLists)
                if loadingBar and send != float ("inf"):
                    pbar = tqdm(total=(send))
                elif table and recipientNum <= 2:
                    print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
                else:
                    print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",str (Sent) + bcolors.ENDC)
                while sent != 500 and Sent < send:
                    try:
                        gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,bcc)
                        if loadingBar and send != float ("inf"):
                            pbar.update(1)
                        elif table and recipientNum <= 2:
                            print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                        else:
                            print ( bcolors.OKGREEN + "\nFrom:",from_address,"\tTo:",to_address,"\tSent:",str (Sent) + bcolors.ENDC)
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
    elif (ops.interactive == True): # this code is called when the user disables interactive mode
        numsent = -1
        length = len(ops.subject)  # find the length of the subject, in order to provide a seed for the random number generator in gmailSpam()
        recipientNum = int(ops.recipientNum)  # set this variable to an integer
        if recipientNum <= 500:
            ops.send = ops.send - 2
            while numsent <= ops.send:
                gmailSpam(ops.sendSpeed, ops.from_address, ops.to_address, ops.body, ops.subject, length, ops.password, bcc)  # run the spam script with the given options
                numsent = numsent + 1
            number = str(numsent + 1)
            print("[+] EMAILS SENT " + number)

except KeyboardInterrupt:
    print(bcolors.FAIL + "\nCancelled!" + bcolors.ENDC)
    sys.exit()
