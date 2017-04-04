# -*- coding: utf-8 -*-

from Tkinter import *

root = Tk()

root.title("Finance Tracking Tool")

root.config(width=900, height=900)

etiket = Label(text="Finance Tracking Tool")
etiket.pack()

buttonConnect = Button(text="Connect", command=root.destroy)
buttonConnect.pack()

buttonList = Button(text="List", command=root.destroy)
buttonList.pack()

buttonAdd = Button(text="Add", command=root.destroy)
buttonAdd.pack()

buttonModify = Button(text="Modify", command=root.destroy)
buttonModify.pack()

ButtonDelete = Button(text="Delete", command=root.destroy)
ButtonDelete.pack()

ButtonCancel = Button(text="Cancel", command=root.destroy)
ButtonCancel.pack()

root.mainloop()