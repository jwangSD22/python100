from tkinter import *
from pwgenfunc import pwgenfunction
import json
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    password = str(pwgenfunction())
    password_input.delete(0,END)
    password_input.insert(0, str(password))

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    user_input = website_input.get()

    try:
        with open('./data.json','r') as f:
            data = json.load(f)
        
        entry = data[user_input]
            
    except:
        messagebox.showinfo('Website not in database', 'Website not found in database')
    
    else:
        messagebox.showinfo(f'{user_input}',f'Email:   {entry["email"]}\nPassword:   {entry["password"]}')

        


# ---------------------------- SAVE PASSWORD ------------------------------- #

# this will be a function added to the add button

def add_account():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

## need to add a checker to see if there's a valid value within each field

    try:
        with open('./data.json','r') as f:
            data = json.load(f)
            data.update(new_data)    
            print('new data updated')

    except:
        with open('./data.json','w') as d:
            json.dump(new_data, d, indent=4)
    else:
        with open('./data.json','w') as d:
            json.dump(data, d, indent=4)


    website_input.delete(0,END)
    password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50, bg='white')


## canvas logo
canvas = Canvas(width=200,height=200)
canvas.config(bg='white', highlightthickness=0)
img_path = './logo.png'
lock_img = PhotoImage(file=img_path)
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)


#website label
website_label = Label(text='Website:',width=20)
website_label.config(background='white')
website_label.grid(row=1,column=0)

#email/username label
email_label = Label(text='Email/Username:',width=20)
email_label.config(background='white')
email_label.grid(row=2,column=0)

#password label
password_label = Label(text='Password:',width=20)
password_label.config(background='white')
password_label.grid(row=3,column=0)



#website_input
website_input = Entry(width=37)
website_input.grid(row=1, column = 1)
website_input.focus()

#search_btn
website_search = Button(text='Search',command=search,width=13,background='white')
website_search.grid(row=1,column = 2)

#email_input
email_input = Entry(width=55)
email_input.grid(row=2, column = 1, columnspan=2)
email_input.insert(0,'jackw1689@gmail.com')

#password_input
password_input = Entry()
password_input.config(width=37)
password_input.grid(row=3, column = 1)

#gen_password_button
gen_password_btn = Button(text='Generate Password',command=gen_pass)
gen_password_btn.config(background='white')
gen_password_btn.grid(row=3,column=2)

#add
add = Button(text="Add", command = add_account)
add.config(width=46,background='white')
add.grid(row=4,column=1,columnspan=2)

window.mainloop()

