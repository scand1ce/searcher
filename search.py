import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title('SEARCH_G_Y')
app.configure(background='#ececec')

s_lable = ttk.Label(app, text='Поиск', font='Arial 14 bold', foreground='blue')
s_lable.grid(row=1, column=0)

text = ttk.Entry(app, width=50, )
text.grid(row=1, column=1)

search_engine = StringVar()
search_engine.set('google')


def search():
    if search_engine.get() == 'google':
        if text.get().strip() != '':
            webbrowser.open('https://www.google.com/search?q=' +
                            text.get())

    elif search_engine.get() == 'youtube':
        if text.get().strip() != '':
            webbrowser.open('https://www.youtube.com/results?search_query=' +
                            text.get())


def searchBtn():
    search()


def enterBtn(event):
    search()


btn_s = ttk.Button(app, text='Найти', width=10,
                   command=searchBtn)
btn_s.grid(row=1, column=2)

text.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text='Google', value='google',
                               variable=search_engine)
radio_google.grid(row=2, column=0, sticky=W)

radio_bing = ttk.Radiobutton(app, text='YouTube', value='youtube',
                             variable=search_engine)
radio_bing.grid(row=2, column=2, sticky=E)

app.wm_attributes('-topmost', True)

text.focus()

app.mainloop()
