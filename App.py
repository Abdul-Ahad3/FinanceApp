from tkinter import *

window = Tk("500x500")
label1 = Label(window, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(window, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
welcome = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F')

label1.pack()   
label2.pack()
welcome.place(x=150, y=300)
window.geometry("500x500")
window.config(background="#FC4C4F")

window.mainloop()