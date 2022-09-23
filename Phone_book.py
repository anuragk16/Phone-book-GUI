from tkinter import *
from def_phonebook import *

## Makin a GUI window
win = Tk()
win.title("PHONE BOOK")
win.geometry("700x500+200+20")
## setting minimum and maximum size of window
win.minsize(700, 500)
win.maxsize(700, 500)
win.config(bg="gray10")

## making a menubar buttons for all functions
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label='See', command = lambda : see(win))
filemenu.add_separator()
filemenu.add_command(label='Save', command = lambda : save(win))
filemenu.add_separator()
filemenu.add_command(label='Make excel file', command = lambda : excel_file(win))
filemenu.add_separator()
filemenu.add_command(label='Search', command = lambda : search(win))
filemenu.add_separator()
filemenu.add_command(label='Exit', command = lambda : win.destroy)
filemenu.add_separator()

menubar.add_cascade(label="file", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_separator()
editmenu.add_command(label="Add", command= lambda : add(win))
editmenu.add_separator()
editmenu.add_command(label="Remove", command= lambda : remove(win))
editmenu.add_separator()

menubar.add_cascade(label="Edit", menu=editmenu)

win.config(menu=menubar)

mainloop()
