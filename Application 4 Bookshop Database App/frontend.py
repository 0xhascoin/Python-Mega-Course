"""
    A program that store these book details:
    Title, Author, Year, ISBN

    User can >
    view all records,
    search an entry,
    add an entry
    update/delete an entry

"""

from tkinter import *
import backend

window = Tk()

title = Label(window, text='Title')
author = Label(window, text='Author')
year = Label(window, text='Year')
isbn = Label(window, text='ISBN')

title.grid(row=0, column=0)
author.grid(row=0, column=2)
year.grid(row=1, column=0)
isbn.grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

books_list_scrollbar = Scrollbar(window)
books_list_scrollbar.grid(row=2, column=2, rowspan=6)
books_list = Listbox(window, height=6, width=35)
books_list.grid(row=2, column=0, rowspan=6, columnspan=2)
books_list.configure(yscrollcommand=books_list_scrollbar.set)
books_list_scrollbar.configure(command=books_list.yview)

# Buttons

viewall = Button(window, text='View All', width=12)
viewall.grid(row=2, column=3)

search = Button(window, text='Search Entry', width=12)
search.grid(row=3, column=3)

add = Button(window, text='Add Entry', width=12)
add.grid(row=4, column=3)

update = Button(window, text='Update', width=12)
update.grid(row=5, column=3)

delete = Button(window, text='Delete', width=12)
delete.grid(row=6, column=3)

close = Button(window, text='Close', width=12)
close.grid(row=7, column=3)

window.mainloop()
