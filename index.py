from tkinter import *
from PIL import Image, ImageTk
from tkfontawesome import icon_to_image
from tkinter import messagebox, font
import webbrowser

root = Tk()
root.geometry("470x500")
root.resizable(False,False)
#set fonts
default_font = font.nametofont('TkDefaultFont')
default_font.configure(family='Ubuntu', size=14, weight='normal')
text_font = font.nametofont('TkTextFont')
text_font.configure(family='Helvetica', size=12, weight='normal')
fixed_font = font.nametofont('TkFixedFont')
fixed_font.configure(family='Ubuntu', size=12, weight='normal')

appImg_src = Image.open('applogo.png')
app_img = ImageTk.PhotoImage(appImg_src)
user_img = icon_to_image('user', fill="white", scale_to_width=40)


# components here
# PACK geometry manager
Label(root, image=app_img).pack()
Label(root, text="Sign In to BoAI", font=("Ubuntu, 28")).pack(pady=12)

#form
form = Frame(root, width=250, height=200)
form.pack_propagate(False)
form.pack()
box1= Frame(form, height=22)
box1.pack(pady=8, fill='x')
box1.pack_propagate(False)
box2= Frame(form, height=22)
box2.pack_propagate(False)
box2.pack(fill='x')
Label(box1, text="username", bg='#D75656', fg='white').pack(side='left', expand=True, fill='both')
username= Entry(box1)
username.pack(side='right', expand=True, fill='both', padx=4)
Label(box2, text="password", bg='#D75656', fg='white', padx=2).pack(side="left", expand=True, fill='both')
password= Entry(box2)
password.pack(side='right', expand=True, fill='both', padx=4)

def check_input():
 if username.get() == 'asd' and password.get() == '123':
  messagebox.showinfo("Info", "Login successfull")
 else:
  messagebox.showerror('Error', "Username or password is incorrect!")
  
signIn = Button(form, padx=4, pady=4, text='Sign In', bg='#BD114A', fg='white', cursor='hand2', comman=check_input)
signIn.pack(pady=6, fill='x', expand=True)

def on_check(isChecked, btn):
 if isChecked.get():
  btn.config(bg='green')
 else:
  btn.config(bg='SystemButtonFace')

isChecked = BooleanVar(value=False)
footer = Frame(form, height=10)
footer.pack(fill='x', pady=14)
remember = Checkbutton(footer, text="Remember me", font=('Ubuntu', 8), variable=isChecked, command= lambda: on_check(isChecked, remember))
remember.pack(side='left', anchor='w')
link = Label(footer, text="Forgot password?", fg='blue', font=font.Font(size=8), cursor='hand2')
link.pack(side='right', anchor='e')
link.bind('<Enter>', lambda e: link.config(font=font.Font(underline=1, size=8)))
link.bind('<Leave>', lambda e: link.config(font=font.Font(underline=0, size=8)))
def open_url(url):
 webbrowser.open_new(url)
link.bind('<Button-1>', lambda e: open_url("https://www.pythonguis.com/"))

root.mainloop()
