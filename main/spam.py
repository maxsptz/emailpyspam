# Import statements
import smtplib
from email.message import EmailMessage
import random
import time
import getpass
import sys
import os

# Colour Scheme

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    print(bcolors.WARNING + "This can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in gmail.txt and gmailpass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Yahoo DISCLAIMER

def yahooInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Yahoo has a limit of 100 emails per hour per account" + bcolors.ENDC)
    print(bcolors.WARNING + "This can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in yahoo.txt and yahoopass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Outlook DISCLAIMER

def outlookInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Outlook/Hotmail has a limit of 100 recipiants per day per account" + bcolors.ENDC)
    print(bcolors.WARNING + "This can be surpassed by using multiple emails."\
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
        print (gmail)
        print (gmail[1])
        print (emailnum)
        emailnum += 1
        print (emailnum)
        from_addr = gmail[emailnum]
        file.close()
    except IOError:
        print ("gmail.txt not found")
        from_addr = "\n"
    try:
        passFile = open("gmailpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("gmailpass.txt not found")
        cipher = "\n"

    return from_addr,cipher

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
        file.close()
    except IOError:
        print ("yahoo.txt not found")
        from_addr = "\n"
    try:
        passFile = open("yahoopass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("yahoopass.txt not found")
        cipher = "\n"
    return from_addr,cipher

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
        file.close()
    except IOError:
        print ("outlook.txt not found")
        from_addr = "\n"
    try:
        passFile = open("outlookpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passFileStuff.split(",")
        passnum += 1
        cipher = passThing[passnum]
        file.close()
    except IOError:
        print ("outlookpass.txt not found")
        cipher = "\n"
    return from_addr,cipher

# Send with limits (Gmail)

def gSingle():
    from_addr = input(bcolors.OKGREEN + 'Your Google Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

# Send with limits (Yahoo)

def ySingle():
    from_addr = input(bcolors.OKGREEN + 'Your Yahoo Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

# Send with limits (Outlook/Hotmail)

def oSingle():
    from_addr = input(bcolors.OKGREEN + 'Your Hotmail/Outlook Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

# Main structure (subject, body, etc.)

def structure():
    to_addr = []
    addr = ""
    number = random.randint(0, 10000)
    while True:
        addr = input(bcolors.OKGREEN + "Type in the recipient, hit enter to finish: " + bcolors.ENDC)
        if not addr:
            break
        else:
            to_addr.append(addr)
    predef = input(bcolors.OKGREEN + 'Would you like to use the subject saved in subject.txt? (Y/N): ' + bcolors.ENDC)
    if predef.lower() == 'y':
        p_reader = open("subject.txt", 'r')
        subject = p_reader.readline()
        index = len(subject) - 1
        subject = subject[0:index]
        p_reader.close()
        length = len (subject)
        subject += ' (' + str(number) + ')'
    else:
        subject = input(bcolors.OKGREEN + 'Subject: ' + bcolors.ENDC)
        length = len (subject)
        subject += ' (' + str(number) + ')'

    predef1 = input(bcolors.OKGREEN + 'Would you like to use the body saved in body.txt? (Y/N): ' + bcolors.ENDC)

    if predef1.lower() == 'y':
        f = open("body.txt", "r")
        body = f.read()
        f.close()
    else:
        body = input(bcolors.OKGREEN + 'Body: ' + bcolors.ENDC)
    speed = float(input(bcolors.FAIL + "At what interval should the emails get sent out? (seconds): " + bcolors.ENDC))

    print(bcolors.WARNING + "Emails will be sent continuously, until this window is closed." + bcolors.ENDC)
    time.sleep(1)
    return speed,to_addr,body,subject

# Main Spammer (Gmail)

def gmailSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
            global sent
            sent += 1
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
                server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))
                server.quit()
                print(bcolors.OKGREEN + f'Email sent to: {", ".join(to_addr)} ({sent})' + bcolors.ENDC)
                time.sleep(speed)
            except smtplib.SMTPAuthenticationError:
                print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
                sys.exit()
            except smtplib.SMTPRecipientsRefused:
                print(bcolors.FAIL + "\nThe The Recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
                sys.exit()

# Main Spammer (Yahoo)

def yahooSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
        global sent
        sent += 1
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
            server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))
            server.quit()
            print(bcolors.OKGREEN + f'Email sent to: {", ".join(to_addr)} ({sent})' + bcolors.ENDC)
            time.sleep(speed)
        except smtplib.SMTPAuthenticationError:
            print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            print(bcolors.FAIL + "\nThe The Recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
            sys.exit()

# Main Spammer (Outlook/Hotmail)

def outlookSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
        global sent
        sent += 1
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
            server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))
            server.quit()
            print(bcolors.OKGREEN + f'Email sent to: {", ".join(to_addr)} ({sent})' + bcolors.ENDC)
            time.sleep(speed)
        except smtplib.SMTPAuthenticationError:
            print(bcolors.FAIL + "\nThe email / password you have entered is incorrect! Exiting..." + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPRecipientsRefused:
            print(bcolors.FAIL + "\nThe The Recipient's email adress is invalid! Exiting..." + bcolors.ENDC)
            sys.exit()

# Main Program
sent = 0
emailnum = -1
passnum = -1
banner()
choice = mailChoice()
# Gmail
if choice == "1":
    multiple = gmailInstruct()
    if multiple == "1" or multiple.upper() == "YES":
        from_address,password = gMultiple()
        spam = True
        while spam is True:
            print(from_address,"\n",password)
            sent += 1
            #gmailSpam(from_addr,cipher)
            if sent == 19:
                sent = 0
                from_address,password = gMultiple()
                spam = True
                if from_address or password != "\n":
                    spam = False
    elif multiple == "2" or multiple == "NO":
        from_address,password = gSingle()
        sent += 1
        while sent < 19:
            #gmailSpam(from_address,password)
            print(f"{from_address}, {password}")
    else:
        print (bcolors.FAIL + "Invaid choice!" + bcolors.ENDC)
        sys.exit()
