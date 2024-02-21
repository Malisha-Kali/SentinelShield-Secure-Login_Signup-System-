# from customtkinter import *
# from PIL import Image
# from tkinter import messagebox, simpledialog
# import sqlite3
# import bcrypt
# import random
# import string

# x = 50
# trail = 3
# conn = sqlite3.connect('user.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL, password TEXT NOT NULL, mfa_enabled INTEGER DEFAULT 0, mfa_code TEXT)')

# seconds = 10

# def set_entryFields():
#     usernameEntry.delete(0, END)
#     passwordEntry.delete(0, END)
#     usernameEntry.configure(placeholder_text= 'username')
#     passwordEntry.configure(show= '*', placeholder_text= 'password')
#     window.focus()

# def decrement_trail():
#     global trail
#     trail -= 1
#     trailLabel.configure(text= f'You have {trail} trails left')
#     if trail <= 0:
#         innerButton.configure(state=DISABLED)
#         SignupButton.configure(state=DISABLED)
#         countdown()

# def generate_mfa_code():
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# def countdown():
#     global seconds
#     trailLabel.configure(text= f'Wait for {seconds} seconds')
#     if seconds > 0:
#         seconds -= 1
#         window.after(1000, countdown)
#     else:
#         trailLabel.configure(text= '')
#         innerButton.configure(state=NORMAL)
#         SignupButton.configure(state=NORMAL)
#         trail = 3
#         seconds = 10

# def generate_captcha_text():
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# def move_frame(direction):
#     global x
#     if direction == 'right' and x<370:
#         x+=1
#         topframe.place(x=x, y=10)
#         topframe.after(1,move_frame, direction)
#     elif direction == 'left' and x>50:
#         x-=1
#         topframe.place(x=x, y=10)
#         topframe.after(1,move_frame, direction)

# def move_left():
#     move_frame('left')
#     headingLabel.configure(text='Sign Up')
#     innerButton.configure(text='Sign Up', command= register_user)
#     trailLabel.configure(text= '')
#     set_entryFields()

# def move_right():
#     move_frame('right')
#     headingLabel.configure(text='Login')
#     innerButton.configure(text='Login', command=login_user)
#     set_entryFields()

# def display_captcha():
#     global captcha_text
#     captcha_text = generate_captcha_text()
#     captchaLabel.configure(text=f'CAPTCHA: {captcha_text}')

# def login_user():
#     global trail
#     if usernameEntry.get() == '' or passwordEntry.get() == '' or captchaEntry.get() == '':
#         messagebox.showerror('Error', 'All Fields are Required')
#     elif captchaEntry.get() != captcha_text:
#         messagebox.showerror('Error', 'Invalid CAPTCHA')
#     else:
#         cursor.execute('SELECT password, mfa_enabled, mfa_code FROM users WHERE username=?', [usernameEntry.get()])
#         result = cursor.fetchone()
#         if result:
#             stored_password, mfa_enabled, mfa_code = result
#             if bcrypt.checkpw(passwordEntry.get().encode('UTF-8'), stored_password):
#                 if mfa_enabled:
#                     mfa_input = simpledialog.askstring("MFA Verification", "Enter MFA Code:")
#                     if mfa_input == mfa_code:
#                         messagebox.showinfo('Success', 'Logged in Successfully')
#                         trail = 3
#                         trailLabel.configure(text= '')
#                     else:
#                         messagebox.showerror('Error', 'Invalid MFA Code')
#                         decrement_trail()
#                 else:
#                     messagebox.showinfo('Success', 'Logged in Successfully')
#                     trail = 3
#                     trailLabel.configure(text= '')
#             else:
#                 messagebox.showerror('Error', 'Invalid Password')
#                 passwordEntry.delete(0, END)
#                 decrement_trail()
#         else:
#             messagebox.showerror('Error', 'Invalid Username')
#             usernameEntry.delete(0, END)
#             passwordEntry.delete(0, END)
#             decrement_trail()

# def register_user():
#     if usernameEntry.get() == '' or passwordEntry.get() == '' or captchaEntry.get() == '':
#         messagebox.showerror('Error', 'All Fields are Required')
#     elif captchaEntry.get() != captcha_text:
#         messagebox.showerror('Error', 'Invalid CAPTCHA')
#     else:
#         cursor.execute('SELECT username FROM users WHERE username=?', [usernameEntry.get()])
#         if cursor.fetchone() is not None:
#             messagebox.showerror('Error' ,'Username Already Exists')
#         else:
#             encode_password = passwordEntry.get().encode('UTF-8')
#             hashed_password = bcrypt.hashpw(encode_password, bcrypt.gensalt())
#             cursor.execute('INSERT INTO users (username, password) VALUES (?,?)',[usernameEntry.get(), hashed_password])
#             conn.commit()
#             messagebox.showinfo('Success', 'Registration Successful')
#             enable_mfa()  # Automatically enable MFA after registration

# def enable_mfa():
#     global trail
#     cursor.execute('UPDATE users SET mfa_enabled=1 WHERE username=?', [usernameEntry.get()])
#     mfa_code = generate_mfa_code()
#     cursor.execute('UPDATE users SET mfa_code=? WHERE username=?', [mfa_code, usernameEntry.get()])
#     conn.commit()
#     messagebox.showinfo('Success', 'MFA Enabled Successfully. MFA Code: ' + mfa_code)
#     trail = 3
#     trailLabel.configure(text= '')

# # Create a window
# window = CTk()
# window.title("Login and Signup Page")
# window.wm_geometry('+500+100')
# mainframe = CTkFrame(window,fg_color='blue4',width=600,height=400)
# mainframe.grid(row=0, column=0, padx=30, pady=30)

# LoginButton = CTkButton(mainframe, text="Login", fg_color='blue4', font=('arial', 20, 'bold'), 
#                         border_color='blue2', border_width=1, hover_color='blue2', cursor='hand2', command=move_right)
# LoginButton.place(x=430, y=300)

# SignupButton = CTkButton(mainframe, text="Sign Up", fg_color='blue4', font=('arial', 20, 'bold'), 
#                         border_color='blue2', border_width=1, hover_color='blue2', cursor='hand2', command=move_left)
# SignupButton.place(x=30, y=300)

# topframe = CTkFrame(window, fg_color='white', width=300, height=400)
# topframe.place(x=50, y=10)

# LogoImage = CTkImage(light_image=Image.open('login.png'), size=(80,80))
# LogoLabel = CTkLabel(topframe,image=LogoImage, text='')
# LogoLabel.grid(row=0, column=0, pady=(20,0))

# headingLabel = CTkLabel(topframe, text='Sign Up', font=('arial', 30, 'bold'), text_color='blue4')
# headingLabel.grid(row=1, column=0, pady=(20,0))

# usernameEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), width=200, height=30, placeholder_text='username')
# usernameEntry.grid(row=2, column=0, padx=(20), pady=(30,20))

# passwordEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), 
#                         width=200, height=30, placeholder_text='password', show='*')
# passwordEntry.grid(row=3, column=0, padx=(20), pady=(0,20))

# captchaLabel = CTkLabel(topframe, text='', font=('arial', 20, 'bold'), text_color='blue4')
# captchaLabel.grid(row=4, column=0, pady=(0, 20))

# captchaEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), 
#                         width=200, height=30, placeholder_text='Enter CAPTCHA')
# captchaEntry.grid(row=5, column=0, padx=(20), pady=(0,20))

# innerButton = CTkButton(topframe, text='Sign Up', fg_color='blue2', 
#                         font=('arial', 20, 'bold'), hover_color='blue4', 
#                         cursor='hand2', command=register_user)
# innerButton.grid(row=6, column=0, pady=20)

# trailLabel = CTkLabel(topframe, text='', font=('arial', 20, 'bold'), text_color='blue4')
# trailLabel.grid(row=7, column=0, pady=(0, 20))

# display_captcha()  # Display CAPTCHA when the window is loaded

# window.mainloop()




from customtkinter import *
from PIL import Image
from tkinter import messagebox,simpledialog
import sqlite3
import bcrypt
import random
import string

x = 50
trail = 3
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL, password TEXT NOT NULL, mfa_enabled INTEGER DEFAULT 0, mfa_code TEXT)')

seconds = 10

def set_entryFields():
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    usernameEntry.configure(placeholder_text= 'username')
    passwordEntry.configure(show= '*', placeholder_text= 'password')
    window.focus()

def decrement_trail():
    global trail
    trail -= 1
    trailLabel.configure(text= f'You have {trail} trails left')
    if trail <= 0:
        innerButton.configure(state=DISABLED)
        SignupButton.configure(state=DISABLED)
        countdown()

def generate_mfa_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def countdown():
    global seconds
    trailLabel.configure(text= f'Wait for {seconds} seconds')
    if seconds > 0:
        seconds -= 1
        window.after(1000, countdown)
    else:
        trailLabel.configure(text= '')
        innerButton.configure(state=NORMAL)
        SignupButton.configure(state=NORMAL)
        trail = 3
        seconds = 10

def generate_captcha_text():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def move_frame(direction):
    global x
    if direction == 'right' and x<370:
        x+=1
        topframe.place(x=x, y=10)
        topframe.after(1,move_frame, direction)
    elif direction == 'left' and x>50:
        x-=1
        topframe.place(x=x, y=10)
        topframe.after(1,move_frame, direction)

def move_left():
    move_frame('left')
    headingLabel.configure(text='Sign Up')
    innerButton.configure(text='Sign Up', command= register_user)
    trailLabel.configure(text= '')
    set_entryFields()
    display_captcha()

def move_right():
    move_frame('right')
    headingLabel.configure(text='Login')
    innerButton.configure(text='Login', command=login_user)
    set_entryFields()
    display_captcha()

def display_captcha():
    global captcha_text
    captcha_text = generate_captcha_text()
    captchaLabel.configure(text=f'CAPTCHA: {captcha_text}')

def login_user():
    global trail
    if usernameEntry.get() == '' or passwordEntry.get() == '' or captchaEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif captchaEntry.get() != captcha_text:
        messagebox.showerror('Error', 'Invalid CAPTCHA')
    else:
        cursor.execute('SELECT password, mfa_enabled, mfa_code FROM users WHERE username=?', [usernameEntry.get()])
        result = cursor.fetchone()
        if result:
            stored_password, mfa_enabled, mfa_code = result
            if bcrypt.checkpw(passwordEntry.get().encode('UTF-8'), stored_password):
                if mfa_enabled:
                    mfa_input = simpledialog.askstring("MFA Verification", "Enter MFA Code:")
                    if mfa_input == mfa_code:
                        messagebox.showinfo('Success', 'Logged in Successfully')
                        generate_captcha_text()
                        display_captcha()
                        trail = 3
                        trailLabel.configure(text= '')
                    else:
                        messagebox.showerror('Error', 'Invalid MFA Code')
                        generate_captcha_text()
                        display_captcha()
                        decrement_trail()
                else:
                    messagebox.showinfo('Success', 'Logged in Successfully')
                    generate_captcha_text()
                    display_captcha()
                    trail = 3
                    trailLabel.configure(text= '')
            else:
                messagebox.showerror('Error', 'Invalid Password')
                passwordEntry.delete(0, END)
                generate_captcha_text()
                display_captcha()
                decrement_trail()
        else:
            messagebox.showerror('Error', 'Invalid Username')
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
            generate_captcha_text()
            display_captcha()
            decrement_trail()

def register_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '' or captchaEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif captchaEntry.get() != captcha_text:
        messagebox.showerror('Error', 'Invalid CAPTCHA')
    else:
        cursor.execute('SELECT username FROM users WHERE username=?', [usernameEntry.get()])
        if cursor.fetchone() is not None:
            messagebox.showerror('Error' ,'Username Already Exists')
        else:
            encode_password = passwordEntry.get().encode('UTF-8')
            hashed_password = bcrypt.hashpw(encode_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users (username, password) VALUES (?,?)',[usernameEntry.get(), hashed_password])
            conn.commit()
            messagebox.showinfo('Success', 'Registration Successful')
            enable_mfa()  # Automatically enable MFA after registration

def enable_mfa():
    global trail
    cursor.execute('UPDATE users SET mfa_enabled=1 WHERE username=?', [usernameEntry.get()])
    mfa_code = generate_mfa_code()
    cursor.execute('UPDATE users SET mfa_code=? WHERE username=?', [mfa_code, usernameEntry.get()])
    conn.commit()
    messagebox.showinfo('Success', 'MFA Enabled Successfully. MFA Code: ' + mfa_code)
    trail = 3
    trailLabel.configure(text= '')

# Create a window
window = CTk()
window.title("Login and Signup Page")
window.wm_geometry('+500+100')
mainframe = CTkFrame(window,fg_color='blue4',width=600,height=400)
mainframe.grid(row=0, column=0, padx=30, pady=30)

LoginButton = CTkButton(mainframe, text="Login", fg_color='blue4', font=('arial', 20, 'bold'), 
                        border_color='blue2', border_width=1, hover_color='blue2', cursor='hand2', command=move_right)
LoginButton.place(x=430, y=300)

SignupButton = CTkButton(mainframe, text="Sign Up", fg_color='blue4', font=('arial', 20, 'bold'), 
                        border_color='blue2', border_width=1, hover_color='blue2', cursor='hand2', command=move_left)
SignupButton.place(x=30, y=300)

topframe = CTkFrame(window, fg_color='white', width=300, height=400)
topframe.place(x=50, y=10)

LogoImage = CTkImage(light_image=Image.open('login.png'), size=(80,80))
LogoLabel = CTkLabel(topframe,image=LogoImage, text='')
LogoLabel.grid(row=0, column=0, pady=(20,0))

headingLabel = CTkLabel(topframe, text='Sign Up', font=('arial', 30, 'bold'), text_color='blue4')
headingLabel.grid(row=1, column=0, pady=(20,0))

usernameEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), width=200, height=30, placeholder_text='username')
usernameEntry.grid(row=2, column=0, padx=(20), pady=(30,20))

passwordEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), 
                        width=200, height=30, placeholder_text='password', show='*')
passwordEntry.grid(row=3, column=0, padx=(20), pady=(0,20))

captchaLabel = CTkLabel(topframe, text='', font=('arial', 20, 'bold'), text_color='blue4')
captchaLabel.grid(row=4, column=0, pady=(0, 20))

captchaEntry = CTkEntry(topframe, font=('arial', 20, 'bold'), 
                        width=200, height=30, placeholder_text='Enter CAPTCHA')
captchaEntry.grid(row=5, column=0, padx=(20), pady=(0,20))

innerButton = CTkButton(topframe, text='Sign Up', fg_color='blue2', 
                        font=('arial', 20, 'bold'), hover_color='blue4', 
                        cursor='hand2', command=register_user)
innerButton.grid(row=6, column=0, pady=20)

trailLabel = CTkLabel(topframe, text='', font=('arial', 20, 'bold'), text_color='blue4')
trailLabel.grid(row=7, column=0, pady=(0, 20))

display_captcha()  # Display CAPTCHA when the window is loaded

window.mainloop()

