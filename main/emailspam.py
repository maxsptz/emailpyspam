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
    os.system('clear')
    try:
        file1 = open('banner.txt', 'r')
        print(' ')
        print(bcolors.OKGREEN + file1.read() + bcolors.ENDC)
        file1.close()
    except IOError:
        print('Banner File not found')

def validChoice(ch):
    valid = False
    while not valid:
        if ch == "1" or ch == "2" or ch == "3":
            valid = True
        else:
            print (bcolors.FAIL + "Invalid choice!" + bcolors.ENDC)
            time.sleep(1)
            ch = input(bcolors.FAIL + "Enter a valid choice: " + bcolors.ENDC)
    return ch

def validMultiple(mult):
    valid = False
    while not valid:
        if mult == "1" or mult.upper() == "YES" or mult == "2" or mult.upper() == "NO":
            valid = True
        else:
            print (bcolors.FAIL + "Invalid choice!" + bcolors.ENDC)
            time.sleep(1)
            mult = input(bcolors.FAIL + "Enter a valid choice: " + bcolors.ENDC)
    return mult

def validRecipientNum(recipientNum,choice):
    global to_addr
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
            print (bcolors.FAIL + "Invalid number of recipients! You must start over." + bcolors.ENDC)
            time.sleep(1)
            to_addr = []
            while True:
                addr = input(bcolors.OKGREEN + "\nType in the recipient(s), hit enter to finish: " + bcolors.ENDC)
                if not addr:
                    break
                else:
                    to_addr.append(addr)
            recipientNum = len (to_addr)
            valid = False
    return recipientNum

def validSend(send,choice,multiple,recipientNum,numOfSenders):
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
                if choice == "3":
                    if (send * recipientNum) < (300 * numOfSenders):
                        valid = True
                    else:
                        message = True
                elif choice == "1" or choice == "2":
                    if (send * recipientNum) < (500 * numOfSenders):
                        valid = True
                    else:
                        message = True
            else:
                message = True
        if message:
            print (bcolors.FAIL + "Invalid amount!" + bcolors.ENDC)
            print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
            time.sleep(1)
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
            time.sleep(1)
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

def validYahoo(from_addr,cipher):
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
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

def validOutlook(from_addr,cipher):
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
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

# Choose Mail Service

def mailChoice():
    print(bcolors.WARNING + '''
    Choose a Mail Service:
    1) Gmail
    2) Yahoo
    3) Hotmail/Outlook
    ''' + bcolors.ENDC + '--------------------------------------------------------------')
    choice = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return choice

# Gmail DISCLAIMER

def gmailInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Gmail has a limit of 500 emails per day per account" + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in gmail.txt and gmailpass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Yahoo DISCLAIMER

def yahooInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Yahoo has a limit of 100 recipients per email (this cannot be exceeded)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nYahoo also has a limit of 500 emails per day per account." + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in yahoo.txt and yahoopass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Outlook DISCLAIMER

def outlookInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Outlook has a limit of 100 recipients per email (this cannot be exceeded)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nOutlook also has a limit of 300 emails per day per account (limit also depends on reputation of email address)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in outlook.txt and outlookpass.txt)"\
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
        print ("gmail.txt not found! Exiting...")
        sys.exit()
    try:
        passFile = open("gmailpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("gmailpass.txt not found! Exiting...")
        sys.exit()

    return from_addr,cipher,numOfSenders

# Surpass Limit with multiple emails (Yahoo)

def yMultiple():
    global emailnum
    global passnum
    try:
        file = open("yahoo.txt", "r")
        fileStuff = file.readline()
        yahoo = fileStuff.split(",")
        emailnum += 1
        from_addr = yahoo[emailnum]
        numOfSenders = len (yahoo)
        if yahoo[-1] == "\n" or yahoo[-1] == "":
            numOfSenders -= 1
        file.close()
    except IOError:
        print ("yahoo.txt not found! Exiting...")
        sys.exit()
    try:
        passFile = open("yahoopass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("yahoopass.txt not found! Exiting...")
        sys.exit()
    return from_addr,cipher,numOfSenders

# Surpass Limit with multiple emails (Outlook/Hotmail)

def oMultiple():
    global emailnum
    global passnum
    try:
        file = open("outlook.txt", "r")
        fileStuff = file.readline()
        outlook = fileStuff.split(",")
        emailnum += 1
        from_addr = outlook[emailnum]
        numOfSenders = len (outlook)
        if outlook[-1] == "\n" or outlook[-1] == "":
            numOfSenders -= 1
        file.close()
    except IOError:
        print ("outlook.txt not found! Exiting...")
        sys.exit()
    try:
        passFile = open("outlookpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("outlookpass.txt not found! Exiting...")
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

# Send with limits (Yahoo)

def ySingle():
    valid = False
    while not valid:
        from_addr = input(bcolors.OKGREEN + 'Your Yahoo Email: ' + bcolors.ENDC)
        cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
        valid = validYahoo(from_addr,cipher)
    numOfSenders = 1
    return from_addr,cipher,numOfSenders

# Send with limits (Outlook/Hotmail)

def oSingle():
    valid = False
    while not valid:
        from_addr = input(bcolors.OKGREEN + 'Your Hotmail/Outlook Email: ' + bcolors.ENDC)
        cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
        numOfSenders = 1
        valid = validOutlook(from_addr,cipher)
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
    recipientNum = validRecipientNum(recipientNum,choice)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    limit = input(bcolors.OKGREEN + "Would you like to send a specific number of emails? (Y/N): " + bcolors.ENDC)
    if limit.lower() == "y":
        send = input(bcolors.FAIL + "Enter the number of emails you want to send: " + bcolors.ENDC)
        #set send variable
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
            print ("subject.txt not found! Exiting...")
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
            print ("body.txt not found! Exiting...")
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
        sent += (1*recipientNum)
        Sent += (1*recipientNum)
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
            time.sleep(speed)
        except smtplib.SMTPAuthenticationError:
            print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            print(bcolors.FAIL + "\nThe recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
            sys.exit()

# Main Spammer (Yahoo)

def yahooSpam(speed,from_addr,to_addr,body,subject,length,cipher,recipientNum):
    global sent
    global Sent
    sent += (1*recipientNum)
    Sent += (1*recipientNum)
    number = random.randint(0, 10000)
    subject = subject[0:length] + " (" + str(number) + ")"
    # Construct email
    msg = EmailMessage()
    msg.add_header('From', from_addr)
    msg.add_header('To', ', '.join(to_addr))
    msg.add_header('Subject', subject)
    msg.set_payload(body)
    # Connect
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    # Start TLS for security
    server.starttls()
    try:
        server.login(from_addr, cipher)
        server.send_message(msg, from_addr=from_addr, to_addrs=to_addr)
        server.quit()
        time.sleep(speed)
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
        sys.exit()
    except smtplib.SMTPRecipientsRefused:
        print(bcolors.FAIL + "\nThe recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
        sys.exit()

# Main Spammer (Outlook/Hotmail)

def outlookSpam(speed,from_addr,to_addr,body,subject,length,cipher,recipientNum):
    global sent
    global Sent
    sent += (1*recipientNum)
    Sent += (1*recipientNum)
    number = random.randint(0, 10000)
    subject = subject[0:length] + " (" + str(number) + ")"
    # Construct email
    msg = EmailMessage()
    msg.add_header('From', from_addr)
    msg.add_header('To', ', '.join(to_addr))
    msg.add_header('Subject', subject)
    msg.set_payload(body)
    # Connect
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    # Start TLS for security
    server.starttls()
    try:
        server.login(from_addr, cipher)
        server.send_message(msg, from_addr=from_addr, to_addrs=to_addr)
        server.quit()
        time.sleep(speed)
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
        sys.exit()
    except smtplib.SMTPRecipientsRefused:
        print(bcolors.FAIL + "\nThe recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
        sys.exit()

# Main Program

def getops(): #Get options and turn off interactive mode
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interactive', default=False, action='store_true', dest='interactive', help='this choice negates interactive mode')
    parser.add_option('-t', '--to', action='append', dest='to_address', help='the email address you are spamming e.x.: email@gmail (cannot conatin.com)')
    parser.add_option('-f', '--from', type='string', dest='from_address', help='the email you are spamming from')
    parser.add_option('-d', '--interval', type='int', dest='sendSpeed', help='the interval in seconds in which you want to send the emails')#this cant be set to i cause interactive mode is set to i as well
    parser.add_option('-p', '--password', type='string', dest='password', help='the password for the email account you are spamming from')
    parser.add_option('-s', '--subject', type='string', dest='subject', help='the subject of the email you want to spam')
    parser.add_option('-b', '--body', type='string', dest='body', help='the actual message inside the email you wish to spam')
    parser.add_option('-n', '--number', dest='recipientNum', help='the number of emails you want to send')
    (options, arguments) = parser.parse_args()
    return options

try:
    ops = getops()
    sent = 0
    Sent = 0
    choice = '0'
    emailnum = -1
    passnum = -1
    banner()

    if(ops.interactive == False): #This checks if the user wants to run the program in interactive mode
        choice = mailChoice()
        choice = validChoice(choice)
        if choice == "1":
            multiple = gmailInstruct()
            multiple = validMultiple(multiple)
            if multiple == "1" or multiple.upper() == "YES":
                from_address,password,numOfSenders = gMultiple()
                sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
                if table:
                    print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
                else:
                    print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                spam = True
                while spam is True and Sent < send:
                    if from_address == "" or from_address == "\n":
                        spam = False
                    else:
                        try:
                            gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                            if table:
                                print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                            else:
                                print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                        except smtplib.SMTPSenderRefused:
                            print ("Limit reached. Switching emails...")
                            from_address,password,numOfSenders = gMultiple()
                            spam = True
                            sent = 0
                        if sent == 500:
                            from_address,password,numOfSenders = gMultiple()
                            spam = True
                            sent = 0
            elif multiple == "2" or multiple.upper() == "NO":
                from_address,password,numOfSenders = gSingle()
                sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
                if table:
                    print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
                else:
                    print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                while sent != 500 and Sent < send:
                    try:
                        gmailSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                        if table:
                            print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                        else:
                            print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                    except smtplib.SMTPSenderRefused:
                        print ("Limit reached. Exiting...")
                        sys.exit()
            else:
                print (bcolors.FAIL + "Invaid choice!" + bcolors.ENDC)
                sys.exit()

    elif(ops.interactive == True):
        length = len(ops.subject) #find the length of the subject, in order to provide a seed for the random number generator in gmailSpam()
        recipientNum = int(ops.recipientNum)# set this variable to an integer
        if recipientNum <= 500:
            gmailSpam(ops.sendSpeed, ops.from_address, ops.to_address, ops.body, ops.subject, length, ops.password, recipientNum)# run the spam script with the given options

    # Yahoo
    elif choice == "2":
        multiple = yahooInstruct()
        multiple = validMultiple(multiple)
        if multiple == "1" or multiple.upper() == "YES":
            from_address,password,numOfSenders = yMultiple()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if table:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
            spam = True
            while spam is True and Sent < send:
                if from_address == "" or from_address == "\n":
                    spam = False
                else:
                    try:
                        yahooSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                        if table:
                            print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                        else:
                            print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                    except smtplib.SMTPSenderRefused:
                        print ("Limit reached. Switching emails...")
                        from_address,password,numOfSenders = yMultiple()
                        spam = True
                        sent = 0
                    if sent == 500:
                        from_address,password,numOfSenders = yMultiple()
                        spam = True
                        sent = 0
        elif multiple == "2" or multiple.upper() == "NO":
            from_address,password,numOfSenders = ySingle()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if table:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
            while sent != 500 and Sent < send:
                try:
                    yahooSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                    if table:
                        print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                    else:
                        print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                except smtplib.SMTPSenderRefused:
                    print ("Limit reached. Exiting...")
                    sys.exit()
        else:
            print (bcolors.FAIL + "Invaid choice!" + bcolors.ENDC)
            sys.exit()

    # Outlook/Hotmail
    elif choice == "3":
        multiple = outlookInstruct()
        multiple = validMultiple(multiple)
        if multiple == "1" or multiple.upper() == "YES":
            from_address,password,numOfSenders = oMultiple()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if table:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
            spam = True
            while spam is True and Sent < send:
                if from_address == "" or from_address == "\n":
                    spam = False
                else:
                    try:
                        outlookSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                        if table:
                            print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                        else:
                            print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                    except smtplib.SMTPSenderRefused:
                        print ("Limit reached. Switching emails...")
                        from_address,password,numOfSenders = oMultiple()
                        spam = True
                        sent = 0
                    if sent == 300:
                        from_address,passwor,numOfSenders = oMultiple()
                        spam = True
                        sent = 0
        elif multiple == "2" or multiple.upper() == "NO":
            from_address,password,numOfSenders = oSingle()
            sendSpeed,to_address,body,subject,length,recipientNum,send = structure(choice,numOfSenders)
            if table:
                print (tabulate([[from_address,to_address,Sent]], headers=["From:", "To:","Sent:"], tablefmt="github"))
            else:
                print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
            while sent != 300 and Sent < send:
                try:
                    outlookSpam(sendSpeed,from_address,to_address,body,subject,length,password,recipientNum)
                    if table:
                        print (tabulate([[from_address,to_address,Sent]], headers=["     ","   ","     "], tablefmt="github"))
                    else:
                        print ("\nFrom:",from_address,"\tTo:",to_address,"\tSent:",Sent)
                except smtplib.SMTPSenderRefused:
                    print ("Limit reached. Exiting...")
                    sys.exit()
        else:
            print (bcolors.FAIL + "Invaid choice! Exiting..." + bcolors.ENDC)
            sys.exit()
    else:
        print (bcolors.FAIL + "Invaid choice! Exiting..." + bcolors.ENDC)
        sys.exit()

except KeyboardInterrupt:
    print(bcolors.FAIL + "\nCancelled!" + bcolors.ENDC)
    sys.exit()

# Add an option to give a submenu to user to choose from predefined recipient list
