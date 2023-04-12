from password import keys
from email.message import EmailMessage
import smtplib


def email_sender(dict):

    for i in dict["recievers"]:

        email=EmailMessage()
        email['from']='avishkar sonni'
        email['to']= i
        email['subject']='Python bot for sending mails and spamming'

        email.set_content(dict["em_content"])
        with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('holierthanthou35@gmail.com', keys)
            smtp.send_message(email)
            print(dict)
            print("Sent the mail")