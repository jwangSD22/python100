from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(width=600,height=600, padx=50,pady=50, bg='white')


## canvas logo
canvas = Canvas(width=200,height=200)
canvas.config(bg='white', highlightthickness=0)
img_path = './logo.png'
lock_img = PhotoImage(file=img_path)
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

#website label
website_label = Label(text='Website:')
website_label.config(background='white')
website_label.grid(row=1,column=0)

#email/username label
email_label = Label(text='Email/Username:')
email_label.config(padx=10,background='white')
email_label.grid(row=2,column=0)


#password label
password_label = Label(text='Password:')
password_label.config(background='white')
password_label.grid(row=3,column=0)

#website_input
website_input = Entry()
website_input.config(width=35)
website_input.grid(row=1, column = 1, columnspan=2)

#email_input
email_input = Entry()
email_input.config(width=35)
email_input.grid(row=2, column = 1, columnspan=2)

#password_input
password_input = Entry()
password_input.config(width=21)
password_input.grid(row=3, column = 1)

#gen_password_button
gen_password_btn = Button(text='Generate Password')
gen_password_btn.config(width=10,background='white')
gen_password_btn.grid(row=3,column=2)

#add
add = Button(text="Add")
add.config(width=36,background='white')
add.grid(row=4,column=1,columnspan=2)

window.mainloop()

