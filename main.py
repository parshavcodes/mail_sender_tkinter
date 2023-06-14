import smtplib
from tkinter import *


def send_mail():
    my_email = "YOUR MAIL"
    my_password = "YOUR PASSWORD"
    email = email_entry.get()
    subject = subject_entry.get()
    message = message_entry.get("1.0", END)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=[email],
            msg=f"Subject: {subject}\n\n{message}"
        )

    connection.close()


window = Tk()
window.title("Mail sender")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mail_img = PhotoImage(file="mail.png")
canvas.create_image(100, 100, image=mail_img)
canvas.grid(row=0, column=1)

# LABEL

email_label = Label(text="Email/username:")
email_label.grid(row=1, column=0)

subject_label = Label(text="Subject:")
subject_label.grid(row=2, column=0)

message_label = Label(text="Message:")
message_label.grid(row=3, column=0)


# ENTRIES
email_entry = Entry(width=35)
email_entry.grid(row=1, column=1,columnspan=2, sticky="EW")
email_entry.focus_set()

# BUTTON

send_button = Button(text="Send", width=36, command=send_mail )
send_button.grid(row=5, column=1, columnspan=2, sticky="EW")



subject_entry = Entry(width=30)
subject_entry.insert(0, "optional")
subject_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

message_entry = Text(height=7, width=30)
message_entry.grid(row=4, column=1,columnspan=2, sticky="EW")



window.mainloop()
