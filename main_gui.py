import os
import tkinter
from cProfile import label
from tkinter import *
USER = os.getlogin()

main_menu = Tk() #create window for main_menu
main_menu.geometry("400x300") #set wm window
main_menu.title("My computer")
main_menu.iconphoto(False, tkinter.PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\testimage.png"))
#why th do i spend sm time on icon 32x32 TO GET SOMETHING LIKE THIS

mypc_text = Label(main_menu, text="Hello, how may i can help you today?", font= 10) #make a text
enter = Button(main_menu, text="Enter")

mypc_face = PhotoImage(file=r"C:\Users\ComServices\PycharmProjects\My computer\image file\pcicon.png")
textbox = Entry(main_menu, justify=LEFT, width=50)
button_for_more = Button(main_menu, text="V", width=2, height=1)

#mypc_image_on_main_menu
mypc_text.pack()
textbox.pack()
button_for_more.pack()
enter.pack()

main_menu.resizable(False, False)
main_menu.mainloop()
