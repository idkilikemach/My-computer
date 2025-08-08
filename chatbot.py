import tkinter as tk
from tkinter import *

chat = Tk()
chat.geometry("400x300")
chat.title("Chat with me")
sent = Button(chat, text="Send", width=10, height=3) #to send text to bot
chat_textbox = Text(chat, height=4, width=46)
chat.iconphoto(False, tk.PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"))

#set place for gui

chat_textbox.place(x=0, y=245)
sent.place(x=321, y=245)
chat.resizable(False, False)
chat.mainloop()
