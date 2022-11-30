import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='Pranav Prajapati'
email['to']='parthjadhav594@gmail.com'
email['subject']='Python bot for sending mails and spamming'

email.set_content('This mail was directly sent by a python bot')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pranavprajapati586@gmail.com','fhvvelfzfwpmwagp')
    smtp.send_message(email)
    print("Sent the mail")