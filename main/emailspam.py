import smtplib
from email.message import EmailMessage
import random
# Predefine variable
sent = int(0)

while (True):
    sent = sent + 1
    # Senders email (must be a gmail adress)
    from_addr = 'gmail@gmail.com'
    # Recipients (doesnt need to be multiple)
    to_addr = ['email@email.com', 'email2@email.com']
    # Read password.txt for password
    p_reader = open('password.txt')
    cipher = p_reader.read()
    # Prevents inbox from sorting all sent emails into one conversation
    number = random.randint(0,10000)

    # Subject & Body
    subject = 'Message (' + str(number) + ')'
    body = 'body!'
    # Construct email
    msg = EmailMessage()
    msg.add_header('from', from_addr)
    msg.add_header('To',', '.join(to_addr))
    msg.add_header('subject', subject)
    msg.set_payload(body)
    # creates SMTP session
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
    print(f'Email sent to: {", ".join(to_addr)} ({sent})')
