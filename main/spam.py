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
    try:
    os.system('clear')
    try:
        file1 = open('banner.txt', 'r')
        print(' ')
        print(bcolors.OKGREEN + file1.read() + bcolors.ENDC)
        file1.close()
    except IOError:
        print('Banner File not found')

def mailChoice():
    print(bcolors.WARNING + '''
    Choose a Mail Service:
    1) Gmail
    2) Yahoo
    3) Hotmail/Outlook
    ''' + bcolors.ENDC + '--------------------------------------------------------------')
    choice = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return choice

def gmailInstruct():
    print(bcolors.FAIL + "DISCLAIMER: Gmail has a limit of 500 emails per day per account" + bcolors.ENDC)
    print(bcolors.WARNING + """\nThis can be surpassed by using multiple emails.
    Do you wish to surpass the limit using multiple emails? (Emails and passwords must be predefined in
    gmail.txt and gmailpass.txt)
    1) Yes
    2) No
    """ + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

def yahooInstruct():
    print(bcolors.FAIL + "DISCLAIMER: Yahoo has a limit of 100 emails per hour per account" + bcolors.ENDC)
    print(bcolors.WARNING + """\nThis can be surpassed by using multiple emails.
    Do you wish to surpass the limit using multiple emails? (Emails and passwords must be predefined in
    yahoo.txt and yahoopass.txt)
    1) Yes
    2) No
    """ + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

def outlookInstruct():
    print(bcolors.FAIL + "DISCLAIMER: Outlook/Hotmail has a limit of 100 recipiants per day per account" + bcolors.ENDC)
    print(bcolors.WARNING + """\nThis can be surpassed by using multiple emails.
    Do you wish to surpass the limit using multiple emails? (Emails and passwords must be predefined in
    outlook.txt and outlookpass.txt)
    1) Yes
    2) No
    """ + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

#if multiple == "1" or multiple.upper() == "YES":
def gMultiple():
    try:
        file = open("gmail.txt", "r")
        fileStuff = file.readline()
        gmail = fileStuff.split(",")
        emailnum = -1
        if gmail[emailnum] != "\n":
            emailnum += 1
            from_addr = gmail[emailnum]
        else:
            print (bcolors.FAIL + "ERROR: No more emails in gmail.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("gmail.txt not found")
    try:
        passFile = open("gmailpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passfileStuff.split(",")
        passnum = -1
        if passThing[passnum] != "\n":
            passnum += 1
            cipher = passThing[passnum]
        else:
            print (bcolors.FAIL + "ERROR: No more passwords in gmailpass.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("gmailpass.txt not found")
    return from_addr,cipher

def yMultiple():
    try:
        file = open("yahoo.txt", "r")
        fileStuff = file.readline()
        yahoo = fileStuff.split(",")
        emailnum = -1
        if yahoo[emailnum] != "\n":
            emailnum += 1
            from_addr = yahoo[emailnum]
        else:
            print (bcolors.FAIL + "ERROR: No more emails in yahoo.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("yahoo.txt not found")
    try:
        passFile = open("yahoopass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passfileStuff.split(",")
        passnum = -1
        if passThing[passnum] != "\n":
            passnum += 1
            cipher = passThing[passnum]
        else:
            print (bcolors.FAIL + "ERROR: No more passwords in yahoopass.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("yahoopass.txt not found")
    return from_addr,cipher

def oMultiple():
    try:
        file = open("outlook.txt", "r")
        fileStuff = file.readline()
        outlook = fileStuff.split(",")
        emailnum = -1
        if outlook[emailnum] != "\n":
            emailnum += 1
            from_addr = outlook[emailnum]
        else:
            print (bcolors.FAIL + "ERROR: No more emails in outlook.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("outlook.txt not found")
    try:
        passFile = open("outlookpass.txt", "r")
        passFileStuff = passFile.readline()
        passThing = passfileStuff.split(",")
        passnum = -1
        if passThing[passnum] != "\n":
            passnum += 1
            cipher = passThing[passnum]
        else:
            print (bcolors.FAIL + "ERROR: No more passwords in outlookpass.txt" + bcolors.ENDC)
        file.close()
    except IOError:
        print ("outlookpass.txt not found")
    return from_addr,cipher

def gSingle():
    from_addr = input(bcolors.OKGREEN + 'Your Google Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

def ySingle():
    from_addr = input(bcolors.OKGREEN + 'Your Yahoo Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

def oSingle():
    from_addr = input(bcolors.OKGREEN + 'Your Hotmail/Outlook Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    return from_addr,cipher

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

def gmailSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
            global sent += 1
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

def yahooSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
        global sent += 1
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

def outlookSpam(speed,from_addr,to_addr,body,subject,length,cipher):
    while True:
        global sent += 1
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
