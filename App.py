from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
import os

#Code for the main window (after next button is pressed)
def nextB():
    #Function for opening a new file
    def newP():
        file = open("C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\file.txt", 'x')

    #Function for opening an already existing file
    def Open():
        os.startfile(filedialog.askopenfilename())

    #Function for exiting the window
    def exit():
        mainWin.destroy()

    #Function for changing background color
    def bGround():
        mainWin.config(bg=colorchooser.askcolor()[1])
    
    def prevShow():
        ledger = ledEntry.get()
        account = accEntry.get()
        date = [day.get(), mon.get(), year.get()]
        file = open("C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\file.txt", 'w')
        file.write(">>>>>>>>>>>>>>>>>> " + ledEntry.get() + " <<<<<<<<<<<<<<<<<<\n")
        file.write(day.get() + " " + mon.get() + ", " + year.get() + " -- " + accEntry.get() + " -- " + transac.get())

    #Main window
    mainWin = Tk()

    menuBar = Menu(mainWin, font=("Arial", 30)) #Main menu bar
    i=10

    #File drop down menu
    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newP)
    fileMenu.add_command(label="Open", command=Open)
    fileMenu.add_command(label="Save")#, command=save)
    fileMenu.add_command(label="Save As")#, command=SaveAs)
    fileMenu.add_command(label="Exit", command=exit)

    #Edit drop down menu
    editMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Background", command=bGround)
    
    #Font Size menu in Edit Menu
    fsMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font Size', menu=fsMenu)
    while(i<=50):
        fsMenu.add_command(label=str(i))
        i+=2
    
    #Font menu in Edit Menu
    fontMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font', menu=fontMenu)
    fontMenu.add_command(label="Arial")
    fontMenu.add_command(label="Times New Roman")
    fontMenu.add_command(label="Calibri")

    #Frame to hold the account details
    accFrame = Frame(mainWin,bg='#FC4C4F')
    accFrame.grid(row=0, column=0)

    #Date frame
    dFrame = Frame(accFrame, bg='#FC4C4F')
    dFrame.grid(row=0, column=2, rowspan=2)

    #Transactions frame
    tFrame = Frame(mainWin, bg='#FC4C4F')
    tFrame.grid(row=1, column=0)

    #Ledger title
    ledLabel = Label(accFrame, text='Ledger title', font=('Arial', 20), bg='#FC4C4F')
    ledLabel.grid(row=0, column=0, padx=5, pady=5)

    ledEntry = Entry(accFrame, font=('Arial', 20))
    ledEntry.grid(row=1, column=0, padx=5, pady=5)

    #Account title
    accLabel = Label(accFrame, text='Account title', font=('Arial', 20), bg='#FC4C4F')
    accLabel.grid(row=0, column=1, padx=5, pady=5)

    accEntry = Entry(accFrame, font=('Arial', 20))
    accEntry.grid(row=1, column=1, padx=5, pady=5)

    #Date
    dateLabel = Label(dFrame, text='Date', font=('Arial', 20), bg='#FC4C4F')
    dateLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    day = ttk.Combobox(dFrame, value=["0","1","2","3","4","5","6","7","8","9","10",
                                      "11","12","13","14","15","16","17","18","19","20",
                                      "21","22","23","24","25","26","27","28","29","30",
                                      "31"], font=('Arial', 20), width=5)
    day.grid(row=1, column=0, padx=(5, 1), pady=5)

    mon = ttk.Combobox(dFrame, value=["January","February","March", "April", 
                                      "May","June","July","August",
                                      "September","October","November","December"], font=('Arial', 20), width=15)
    mon.grid(row=1, column=1, pady=5)

    year = ttk.Combobox(dFrame, value=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
                                      "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019",
                                      "2020","2021","2022","2023","2024","2025","2026","2027","2028","2029",
                                      "2030","2031","2032","2033","2034","2035","2036","2037","2038","2039",
                                      "2040","2041","2042","2043","2044","2045","2046","2047","2048","2049",
                                      "2050"], font=('Arial', 20), width=8)
    year.grid(row=1, column=2, padx=(1, 5), pady=5)

    #Transaction
    tLabel = Label(tFrame, text='Select Transaction', font=('Arial', 20), bg='#FC4C4F')
    tLabel.grid(row=0, column=0, padx=5, pady=5)

    transac = ttk.Combobox(tFrame, values=['Cash Recieved', 'Online recieved', 'Cash payment', 'Online Payment'], 
                           font=('Arial', 20), width=20)
    transac.grid(row=1, column=0, padx=5, pady=5)

    #Amount of Cash/Payment
    cashLabel = Label(tFrame, text='Amount(Cash)', font=('Arial', 20), bg='#FC4C4F')
    cashLabel.grid(row=0, column=1, padx=5, pady=5)

    cash = Entry(tFrame, font=('Arial', 20), width=20)
    cash.grid(row=1, column=1, padx=5, pady=5)
    
    #Button to show preview
    preview = Button(mainWin, text='Show Preview', font=('Arial', 20), bg='black', fg='#FC4C4F', command=prevShow)
    preview.place(relx=0.98, rely=0.98, anchor='se')

    mainWin.geometry("1130x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)
    welcome.destroy()

#Welcome window
welcome = Tk()

label1 = Label(welcome, text="My App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
nextButton = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=nextB)

label1.pack()   
label2.pack()
nextButton.place(relx=0.35, rely=0.6)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()