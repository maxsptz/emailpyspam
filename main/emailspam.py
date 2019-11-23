import smtplib
from email.message import EmailMessage
import random
import time
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

try:
	file1 = open('banner.txt', 'r')
	print(' ')
	print (bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('Banner File not found')

print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
choice = int(input(bcolors.OKGREEN + 'Number: ' + bcolors.ENDC))

# Gmail
if choice == 1:
    number = random.randint(0,10000)
    from_addr = input(bcolors.OKGREEN + 'Your Google Email: ' + bcolors.ENDC)
    cipher = getpass.getpass(bcolors.OKGREEN + 'Password:' + bcolors.ENDC)
    to_addr = []
    addr = ""
    while True:
        addr = input(bcolors.OKGREEN + "Type in the recipient, hit enter to finish: " + bcolors.ENDC)
        if not addr:
            break
        else:
            to_addr.append(addr)
    predef = input(bcolors.OKGREEN + 'Would you like to use the subject saved in subject.txt? (Y/N) ' + bcolors.ENDC)
    if predef.lower() == 'y':
        f = open("subject.txt", "r")
        subject = f.read() + ' (' + str(number) + ')'
    else:
        subject = input(bcolors.OKGREEN + 'Subject: ' + bcolors.ENDC)
        subject = subject + ' (' + str(number) + ')'

    predef1 = input(bcolors.OKGREEN + 'Would you like to use the body saved in body.txt? (Y/N) ' + bcolors.ENDC)

    if predef1.lower() == 'y':
        f = open("body.txt", "r")
        body = f.read()
    else:
        body = input(bcolors.OKGREEN + 'Body: ' + bcolors.ENDC)
    print(bcolors.WARNING + "Emails will be sent continuously, until this window is closed." + bcolors.ENDC)
    time.sleep(1)
    sent = int(0)
    while (True):
        sent += 1
        # Construct email
        msg = EmailMessage()
        msg.add_header('from', from_addr)
        msg.add_header('To',', '.join(to_addr))
        msg.add_header('subject', subject)
        msg.set_payload(body)
        # Connect
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS for security
        server.starttls()
        # Authentication
        server.login(from_addr, cipher)

        # Sending the mail
        server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))

        # Terminating the session
        server.quit()

        # Output
        print(bcolors.OKGREEN + f'Email sent to: {", ".join(to_addr)} ({sent})' + bcolors.ENDC)

# Yahoo Mail
elif choice == 2:
    number = random.randint(0,10000)
    from_addr = input(bcolors.OKGREEN + 'Your Yahoo Email: ' + bcolors.ENDC)
    cipher = getpass.getpass()
    to_addr = []
    addr = ""
    while True:
        addr = input(bcolors.OKGREEN + "Type in the recipient, hit enter to finish: " + bcolors.ENDC)
        if not addr:
            break
        else:
            to_addr.append(addr)
    predef = input(bcolors.OKGREEN + 'Would you like to use the subject saved in subject.txt? (Y/N) ' + bcolors.ENDC)
    if predef.lower() == 'y':
        f = open("subject.txt", "r")
        subject = f.read() + ' (' + str(number) + ')'
    else:
        subject = input(bcolors.OKGREEN + 'Subject:' + bcolors.ENDC)
        subject = subject + ' (' + str(number) + ')'

    predef1 = input(bcolors.OKGREEN + 'Would you like to use the body saved in body.txt? (Y/N) ' + bcolors.ENDC)

    if predef1.lower() == 'y':
        f = open("body.txt", "r")
        body = f.read()
    else:
        body = input(bcolors.OKGREEN + 'Body: ' + bcolors.ENDC)
    print(bcolors.WARNING + "Emails will be sent continuously, until this window is closed." + bcolors.ENDC)
    time.sleep(1)
    sent = int(0)
    while (True):
        sent += 1
        # Construct email
        msg = EmailMessage()
        msg.add_header('from', from_addr)
        msg.add_header('To',', '.join(to_addr))
        msg.add_header('subject', subject)
        msg.set_payload(body)
        # Connect
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        # Start TLS for security
        server.starttls()
        # Authentication
        server.login(from_addr, cipher)

        # Sending the mail
        server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))

        # Terminating the session
        server.quit()

        # Output
        print(bcolors.OKGREEN + f'Email sent to: {", ".join(to_addr)} ({sent})' + bcolors.ENDC)
# Outlook / Hotmail
elif choice == 3:
    number = random.randint(0,10000)
    from_addr = input(bcolors.OKGREEN + 'Your Hotmail/Outlook Email: ' + bcolors.ENDC)
    cipher = getpass.getpass()
    to_addr = []
    addr = ""
    while True:
        addr = input(bcolors.OKGREEN + "Type in the recipient, hit enter to finish: " + bcolors.ENDC)
        if not addr:
            break
        else:
            to_addr.append(addr)
    predef = input(bcolors.OKGREEN + 'Would you like to use the subject saved in subject.txt? (Y/N) ' + bcolors.ENDC)

    if predef.lower() == 'y':
        f = open("subject.txt", "r")
        subject = f.read() + ' (' + str(number) + ')'
    else:
        subject = input(bcolors.OKGREEN + 'Subject: ' + bcolors.ENDC)
        subject = subject + ' (' + str(number) + ')'

    predef1 = input(bcolors.OKGREEN + 'Would you like to use the body saved in body.txt? (Y/N) ' + bcolors.ENDC)

    if predef1.lower() == 'y':
        f = open("body.txt", "r")
        body = f.read()
    else:
        body = input(bcolors.OKGREEN + 'Body: ' + bcolors.ENDC)

    print(bcolors.WARNING + "Emails will be sent continuously, until this window is closed." + bcolors.ENDC)

    time.sleep(1)
    sent = int(0)
    while (True):
        sent += 1
        # Construct email
        msg = EmailMessage()
        msg.add_header('from', from_addr)
        msg.add_header('To',', '.join(to_addr))
        msg.add_header('subject', subject)
        msg.set_payload(body)
        # Connect
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        # Start TLS for security
        server.starttls()
        # Authentication
        server.login(from_addr, cipher)

        # Sending the mail
        server.send_message(msg, from_addr=from_addr, to_addrs=', '.join(to_addr))

        # Terminating the session
        server.quit()

else:
    print(bcolors.FAIL + 'Invalid input! Exiting...')
    time.sleep(2)
    sys.exit(0)
