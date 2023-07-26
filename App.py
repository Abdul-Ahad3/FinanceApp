from tkinter import *

def next():
    mainWin = Tk()

    menuBar = Menu(mainWin)

    fileMenu = Menu(menuBar)
    menuBar.add_cascade(label="File", menu=fileMenu)
    editMenu = Menu(menuBar)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    mainWin.geometry("900x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)
    welcome.destroy()

welcome = Tk()

label1 = Label(welcome, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
next = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=next)

label1.pack()   
label2.pack()
next.place(x=150, y=300)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()