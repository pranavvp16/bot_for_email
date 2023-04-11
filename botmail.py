from tkinter import *
import smtplib
from password import keys
from email.message import EmailMessage
recievers = []
em_content = ''

def email_sender():

    for i in recievers:

        email=EmailMessage()
        email['from']='avishkar sonni'
        email['to']= i 
        email['subject']='Python bot for sending mails and spamming'

        email.set_content(em_content)
        with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('holierthanthou35@gmail.com', keys)
            smtp.send_message(email)
            print("Sent the mail")
        
tk = Tk()
tk.minsize(width=300, height=400)

add_label = Label(text="Add emails you want to send one by one: ")
add_label.pack(padx=5, pady=2)

email_entry = Entry(width=30)
email_entry.pack()

def refresh():
    reciever = email_entry.get()
    recievers.append(reciever)
    print(recievers)
    email_entry.delete(0, END)

add_button = Button(tk, text='add', command=refresh)
add_button.pack(padx=5, pady=15)

Matter_Label = Label(text="you can write your email here: ")
Matter_Label.pack()

Matter_Entry = Text()
Matter_Entry.pack(padx=20, pady=10)

def content_change():
    global content
    content = Matter_Entry

Content_add_Button = Button(text="add", command=content_change)
Content_add_Button.pack()

warning_label = Label(text='by clicking this button You will send the designated email to everyone you added')
warning_label.pack(pady=10)

send_button = Button(text="send", command=email_sender)
send_button.pack(padx=5, pady=15)

tk.mainloop()