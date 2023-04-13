from tkinter import *
import customtkinter as ctk
from helper import email_sender
from functools import partial
recievers = []
email_dictionary = {}

window = ctk.CTk()
window.minsize(width=450, height=600)
window.title('EMAIL BOT')

add_label = ctk.CTkLabel(master= window, text="Add emails you want to send one by one: ")
add_label.pack()

email_entry = ctk.CTkEntry(window, width=200, corner_radius=5)
email_entry.pack()
def refresh():
    reciever = email_entry.get()
    recievers.append(reciever)
    email_entry.delete(0, END)


# add list of recievers in dictionary
email_dictionary["recievers"] = recievers

button = ctk.CTkButton(window,
                       corner_radius=10,
                       command=refresh,
                       fg_color="transparent",
                       hover_color='green4',
                       text="add",
                       border_width=1,
                       border_color='green4'
                        )
button.pack(padx=5, pady=10)

add_mail = ctk.CTkLabel(window,
                        text="Write Your Mail Here: "
                        )
add_mail.pack()

change_mail = ctk.CTkTextbox(window, 
                             corner_radius=10,
                             border_spacing=1,
                             font=('Arial', 12),
                             height=300,
                             width=400
                             )
change_mail.pack()


def assign_mail():
    email_dictionary["em_content"] = change_mail.get(1.0, "end-1c")


change_button = ctk.CTkButton(window,
                              corner_radius=10,
                              fg_color="transparent",
                              hover_color='green4',
                              text="Modify",
                              border_width=1,
                              border_color='green4',
                              command=assign_mail)
change_button.pack()

warning_label = ctk.CTkLabel(window,
                             text='by clicking this button You will send the designated \n email to everyone you added')
warning_label.pack(pady=20)

send_button = ctk.CTkButton(window,
                            corner_radius=10,
                            fg_color="transparent",
                            hover_color='green4',
                            text="send",
                            border_width=1,
                            border_color='green4',
                            # partial allows to run callable object with parameters
                            command=partial(email_sender, email_dictionary)
                        )

send_button.pack()


window.mainloop()
