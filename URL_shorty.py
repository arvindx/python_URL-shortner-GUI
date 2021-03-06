import pyshorteners
from tkinter import *
from PIL import Image, ImageTk

import pyperclip

root = Tk()
root.geometry('400x400')
root.resizable(False, False)
root.title('URL Shortener')
root.config(bg='#4a536b')


image = Image.open('url.png')
test = ImageTk.PhotoImage(image)
Label(image=test, bg='#4a536b').pack()

url = StringVar()
url_short = StringVar()

Label(root, text='URL Shortener', bg='#4a536b', fg='#ff9a8d', font='Times 22 bold').pack()
# Label(root, text='@_python.py_', bg='#4a536b', fg='#ff9a8d', font='Times 15 bold italic').pack()

Label(root, text='Enter URL: ', bg='#4a536b', fg='#aed6dc', font='Times 10 bold').place(x=50, y=220)
Entry(root, textvariable= url, width=35, font='Times 12' ).place(x=50, y=240)

Label(root, text='New URL: ', bg='#4a536b', fg='#aed6dc', font='Times 10 bold').place(x=50, y=330)
text = Entry(root, width=47, textvariable=url_short)
text.place(x = 50, y=330)

def Convert_fun():
    con_url = pyshorteners.Shortener().tinyurl.short(url.get())
    url_short.set(con_url)


Button(root, text= 'Convert', bg='#fff', fg='#000', font='Times 15 bold', command=Convert_fun).place(x=150, y=280)




def Copy_password():
    pyperclip.copy(url_short.get())
    

Button(root, text = 'Copy', command = Copy_password).place(x = 170, y= 363)

root.mainloop()