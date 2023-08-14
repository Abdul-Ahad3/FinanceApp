from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import *
from tkinter import simpledialog
import os

def nexB():
    #Opens the ledger made already
    def openLedger():
        new_file_path = "C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\" + ledEntry.get() + ".txt"
        file = open(new_file_path, 'w')
        file.write("\n")
        nextB()
    
    global row
    row=2
    #Function to check if the ledger entry box is empty or not
    def checkLedger():
        global row
        row+=1
        if(ledEntry.index("end") != 0 and tcEntry.index("end") != 0):
            nextB()
            x = Button(ledgerWin, text=ledEntry.get(), font=('Arial', 20), bg='black', fg='#FC4C4F', width=30, command=openLedger)
            x.grid(row=row, column=1, padx=5, pady=5)
        elif(ledEntry.index("end") == 0):
            messagebox.showerror(parent=ledgerWin, title='Error', message='Please enter a valid Ledger name')
        elif(tcEntry.index("end") == 0):
            messagebox.showerror(parent=ledgerWin, title='Error', message='Please enter a valid cash amount')
    
    ledgerWin = Tk()
    ledgerWin.title("Finance App")
   
    #Total Available Cash
    global tcEntry
    tcEntry = Entry(ledgerWin, font=('Arial', 30), width=22)
    tcEntry.insert(0, "Enter starting cash")
    tcEntry.bind("<FocusIn>", lambda e: tcEntry.delete(0, "end"))
    tcEntry.grid(row=0, column=0, padx=5, pady=5)
    
    #Ledger Title
    global ledEntry
    ledEntry = Entry(ledgerWin, font=('Arial', 30), width=22)
    ledEntry.bind("<FocusIn>", lambda e: ledEntry.delete(0, "end"))
    ledEntry.grid(row=1, column=0, padx=5, pady=5)

    #Add Ledger Button
    button = Button(ledgerWin, text='+ Add Ledger', font=('Arial', 20), bg='black', fg='#FC4C4F', width=30, command =checkLedger)
    button.grid(row=2, column=0, padx=5, pady=5)
    
    ledgerWin.geometry("500x600")
    ledgerWin.config(background='#FC4C4F', menu=menuBar)
    welcome.destroy()
    ledgerWin.mainloop()


#Code for the main window (after next button is pressed)
def nextB():
    mainWin = Tk()
    mainWin.title("Finance App")

    #Function for opening a new file
    def newP():
        file = open("C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\file.txt", 'x')

    #Function for opening an already existing file
    def Open():
        os.startfile(filedialog.askopenfilename())

    #Function for saving file
    def save():
        new_file_path = "C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\" + ledEntry.get() + ".txt"
        file = open(new_file_path, 'x')
    
    #Function for exiting the window
    def exit():
        mainWin.destroy()

    #Function for changing background color
    def bGround():
        back = colorchooser.askcolor()[1]
        mainWin.config(bg=back)
        accFrame.config(bg=back)
        tFrame.config(bg=back)
        dFrame.config(bg=back)
        lrFrame.config(bg=back)
    
    accInfo = [["Date", "Account title", "Transaction", "Amount(Rs.)"]]
    global total
    total=int(tcEntry.get())
    def addInfo():
        global total
        #Condition to alter the calculation of total cash according to transaction type
        if(transac.get() == 'Cash Recieved' or transac.get() == 'Online Recieved' or transac.get() == 'Loan Recieved' or transac.get() == 'Loan Taken'):
            total = total + int(cash.get())
        elif(transac.get() == 'Cash Payment' or transac.get() == 'Online Payment' or transac.get() == 'Loan Given' or transac.get() == 'Loan Paid'):
            total = total - int(cash.get())
        
        if(transac.get() == "Loan Taken" or transac.get() == "Loan Given"):
            if (messagebox.askyesno(message='Would you like to add a reminder for the loan?')):
                lbox = simpledialog.askstring("Loan Title", "Enter the name of recipient/donor")
                lbox1 = simpledialog.askstring("Due date", "Enter due date in format dd/mm/yyyy")

                tk.Button(lrFrame, text=lbox, font=('Arial', 10), bg='black', fg='#FC4C4F').grid(row=0, column=0, padx=5, pady=5)
        
        if(transac.get() == "Payment Due"):
            if (messagebox.askyesno(message='Would you like to add a reminder for the payment?')):
                pbox = simpledialog.askstring("Payment Title", "Enter the name of recipient/payer")
                pbox1 = simpledialog.askstring("Due date", "Enter due date in format dd/mm/yyyy")
        
        accInfo.append([dLabel.cget("text"), transac.get(), cash.get()])
        
        new_file_path = "C:\\Users\\delll\\OneDrive\\Desktop\\MyApp\\Ledger\\" + ledEntry.get() + ".txt"
        file = open(new_file_path, 'w')
        for a in accInfo:
            for b in a:
                file.write("|\t" + b + "\t ")
            file.write("|\n---------------------------------------------------------------------\n")
        file.write("Total--------------------------------------------|\t\t" + str(total) + "\t\t|")
            

    def prevShow():
        print("")

    #Main menu bar
    menuBar = Menu(mainWin, font=("Arial", 30))
    i=10

    #File drop down menu
    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newP)
    fileMenu.add_command(label="Open", command=Open)
    fileMenu.add_command(label="Save", command=save)
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
    accFrame = Frame(mainWin,bg='#FC4C4F', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    accFrame.grid(row=0, column=0)
    mainWin.grid_rowconfigure(0, weight=1)

    #Date frame
    dFrame = Frame(accFrame, bg='#FC4C4F')
    dFrame.grid(row=1, column=1, rowspan=2)

    #Loan Reminder Frame
    lrFrame = Frame(accFrame, bg='#FC4C4F')
    lrFrame.grid(row=0, column=2, rowspan=3, columnspan=2)

    #Transactions frame
    tFrame = Frame(mainWin, bg='#FC4C4F', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    tFrame.grid(row=1, column=0)
    mainWin.grid_rowconfigure(1, weight=1)

    #Buttons frame
    bFrame = Frame(mainWin, bg='#FC4C4F', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    bFrame.grid(row=2, column=0)
    mainWin.grid_rowconfigure(2, weight=1)

    mainWin.grid_columnconfigure(0, weight=1)
    
    #Ledger name as title
    title = Label(accFrame, text=ledEntry.get(), font=('Arial', 40, 'bold'), bg='#FC4C4F')
    title.grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 10))
    
    #Account title
    accLabel = Label(accFrame, text='Account title', font=('Arial', 20), bg='#FC4C4F')
    accLabel.grid(row=1, column=0, padx=5, pady=5)

    accEntry = Entry(accFrame, font=('Arial', 20))
    accEntry.grid(row=2, column=0, padx=5, pady=5)

    #Date
    dateLabel = Label(dFrame, text='Date', font=('Arial', 20), bg='#FC4C4F')
    dateLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

    def setDate():
        def ok():
            dLabel.config(text=calendar.get_date())

        calWin = Tk()
        calWin.title("Select Date")
        #Calendar to get date
        calendar = Calendar(calWin, selectmode='day', year=2023, month=8, day=12)
        calendar.pack()
        calWin.lift()
        ok = Button(calWin, text='OK', command=ok)
        ok.pack(side='bottom')

    
    dLabel = Label(dFrame, font=('Arial', 20), bg='white', width=10)
    dLabel.grid(row=1, column=0, padx=5, pady=5)

    dateButton = Button(dFrame, text='Select Date', font=('Arial', 15), bg='black', fg='#FC4C4F', width=10, command=setDate)
    dateButton.grid(row=1, column=1, padx=5, pady=5)

    lLabel = Label(lrFrame, text='Loans:', font=('Arial', 20), bg='#FC4C4F')
    lLabel.grid(row=0, column=0, padx=5, pady=5)

    pLabel = Label(lrFrame, text='Payments:', font=('Arial', 20), bg='#FC4C4F')
    pLabel.grid(row=4, column=0, padx=5, pady=5)

    #Transaction
    tLabel = Label(tFrame, text='Select Transaction', font=('Arial', 20), bg='#FC4C4F')
    tLabel.grid(row=0, column=0, padx=5, pady=5)

    transac = ttk.Combobox(tFrame, values=['Cash Recieved', 'Online Recieved', 'Cash Payment', 
                                          'Online Payment', 'Loan Given', 'Loan Recieved',
                                          'Loan Taken', 'Loan Paid', 'Payment Due'],
                                          font=('Arial', 20), width=20)
    transac.grid(row=1, column=0, padx=5, pady=5)

    #Amount of Cash/Payment
    cashLabel = Label(tFrame, text='Amount(Cash)', font=('Arial', 20), bg='#FC4C4F')
    cashLabel.grid(row=0, column=1, padx=5, pady=5)

    cash = Entry(tFrame, font=('Arial', 20), width=20)
    cash.grid(row=1, column=1, padx=5, pady=5)
    
    #Button to add the info to a text file
    add = Button(bFrame, text='Add', font=('Arial', 20), bg='black', fg='#FC4C4F', width=12, command=addInfo)
    add.grid(row=0, column=0, padx=(0, 5))

    #Button to show preview
    preview = Button(bFrame, text='Show Preview', font=('Arial', 20), bg='black', fg='#FC4C4F', width=12, command=prevShow)
    preview.grid(row=0, column=1, padx=(5, 0))

    mainWin.geometry("800x600")
    mainWin.config(background="#FC4C4F", menu=menuBar)

#Welcome window
welcome = Tk()
welcome.title("Finance App")

label1 = Label(welcome, text="Finance App", font=('Arial',50,'bold'),bg='#FC4C4F')
label2 = Label(welcome, text="WELCOME", font=('Arial',50),bg='#FC4C4F')
nextButton = Button(text='NEXT', font=('Arial',40), bg='black', fg='#FC4C4F', command=nexB)

label1.pack()   
label2.pack()
nextButton.place(relx=0.35, rely=0.6)
welcome.geometry("500x500")
welcome.config(background="#FC4C4F")

welcome.mainloop()