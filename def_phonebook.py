import numpy as np
import pandas as pd
from tkinter import *
from tkinter import simpledialog

## Now load a file we save before
main = np.load("contacts.npy", allow_pickle=True)

## For printing a label in GUI window
def label(master, text="nothing", x=0, y=0):
    list_area = Label(master, text=text, bg="gray20", 
                        font=("times of roman", 15), fg="white",
                        pady=10)
    list_area.place(x=x, y=y)

## Making a function to create a new contact
def add(master):
    global main
    name = simpledialog.askstring(title="Name of the new contact", prompt="Write Name of new contact")
    num = simpledialog.askstring(title="Number of new contact", prompt="Write Number of new contact")
    add_array = np.array([name,num], dtype=object)
    main = np.vstack((main,add_array))
    label(master=master, text=add_array[0]+"'s number is added to the list                        ", x=10, y=410)
    return main

## Making a funtion to save the new created contact
def save(master):
    label(master=master, text="Saving.....                             ", x=10, y=410)
    np.save("contacts", main)
    label(master=master, text="File is Saved.                          ", x=10, y=410)

## making a funtion to save a contact list in excel file
def excel_file(master):
    label(master=master, text="saving.......", x=10, y=410)
    df = pd.DataFrame(main)
    filepath = 'excel_contacts.xlsx'
    df.to_excel(filepath, index=False)
    label(master=master, text="File is saved as excel file.", x=10, y=410)

## Making a function to see the full contact list
def see(master):
    text = Text(master)
    text.grid(row=0, column=1)
    scrollbar = Scrollbar(master, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=0, sticky="nsew")
    text.insert(END, main)

## Making a function to search a contect with only
     # some words (we don't need to write full name of contact)
def search(master):
    s = list(main[:,0])
    n = simpledialog.askstring(title="Type name", prompt="Type name")
    lis = []
    for i,elem in enumerate(s):
        if n in elem:
            no = s.index(elem)
            ad = str(f"     {main[no,0]} -- {main[no,1]}       ")
            lis.append(ad)
    text = Text(master)
    text.grid(row=0, column=1)
    scrollbar = Scrollbar(master, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=0, sticky='nsew')
    lis = np.array([lis],dtype=object)
    text.insert(END, lis)

## Making a function to remove a existing contact
def remove(master):
    global main
    main_list = list(main[:,0])
    ## First we have to search all names belonging to that
    remove_name = simpledialog.askstring(title="searching a name to remove.....",
                                         prompt="Search a name to remove")
    lis = []
    for i,elem in enumerate(main_list):
        if remove_name in elem:
            elem_no = main_list.index(elem)
            ad = str(f'         {main[elem_no,0]} -- {main[elem_no,1]}      ')
            lis.append(ad)
    text = Text(master)
    text.grid(row=0, column=1)
    scrollbar = Scrollbar(master, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=0, sticky='nsew')
    lis = np.array([lis], dtype=object)
    text.insert(END, lis)

    ## Now we have to take input with the full name of contact to remove
    full_remove_name = simpledialog.askstring(title="Removing name", 
                                              prompt="Type full name to remove")
    if full_remove_name in main_list:
        index_no_to_remove = main_list.index(full_remove_name)
        main = np.delete(main, index_no_to_remove, 0)

    label(master=master, text=full_remove_name+" is removed.")
