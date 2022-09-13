from cProfile import label
from tkinter import *
main_window = Tk()
#main_window.geometry('400x110')

#labels
#Label(main_window,text='Hello WOrld').pack()
#Label(main_window,text='This is a label').pack()

#we can't use pack and grid in the same column
Label(main_window,text='What\'s your name?').grid(row = 0,column = 0)
Label(main_window,text='How old are you?').grid(row = 1,column = 0)

#test input
entry1 = Entry(main_window,width=40,borderwidth=5)
entry1.grid(row=0,column=1)#placing the entry
#my_name =entry1.get()
'''
entry1.delete(0,ENDtt)
'''
entry2 = Entry(main_window,width=40,borderwidth=5)
entry2.grid(row=1,column=1)
#my_age = entry2.get()

#function for button
def onClick():
    print(f'Welcome {entry1.get()}.You/re {entry2.get()} years old')

#button widget
Button(main_window,text='Click me',command=onClick).grid(row=2,column=1)


main_window.mainloop()
