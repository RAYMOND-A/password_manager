from tkinter import *
from tkinter import messagebox
import random
import pyperclip # for copying data in clipboard

# the import * imports all classes not method hence we do not use it

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_symbols = [random.choice(symbols) for char in range(nr_numbers)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    password_input.insert(0, password)

    # print(f"Your password is: {password}")
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    psw = password_input.get()
    saved_email = email_input.get()
    saved_website = website_input.get()

    if len(psw) == 0 or len(saved_website) == 0:
        messagebox.showerror(title=saved_email, message="Please fill all fields")

    else:

        is_ok = messagebox.askokcancel(title=saved_website,
                                       message=f"These are the details entered:\n Email: {saved_email}\n Password: {psw} \n Is it ok to save?")

        if is_ok:
            with open('saved_info.txt', 'a') as file_object:
                file_object.write(f"{psw} | {saved_email} | {saved_website}\n")
                # it is unclear if writing the file_name in the newly created file is really what you want.
            password_input.delete(0, END)
            # email_input.delete(0, END)
            website_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,)

canvas = Canvas(width=200, height=200, )

padlock_img = PhotoImage(file="download.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

website_lb = Label(text="Website:")
website_lb.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2,)
website_input.focus()


email_lb = Label(text="Email/Username:", )
email_lb.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "johndoe@gmail.com")


password_lb = Label(text="Password:",)
password_lb.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

password_generator = Button(text="generate", command=generate_password)
password_generator.grid(row=3, column=2)


add_pw = Button(text="Add", width=36, command=save)
add_pw.grid(row=4, column=1, columnspan=2)




window.mainloop()