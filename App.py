from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
from tkcalendar import *
from tkinter import simpledialog
from time import *
import mysql.connector
from datetime import datetime
import bcrypt

def hash_password(password):
    # Hash a password using bcrypt
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


def convert_date(date_string):
    # Assuming the date format is 'mm/dd/yyyy'
    date_object = datetime.strptime(date_string, '%m/%d/%y')
    return date_object.strftime('%Y-%m-%d')


#connecting code to server
mydb_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld",
    auth_plugin="mysql_native_password"
)

mcursor = mydb_connect.cursor()

mcursor.execute("CREATE DATABASE IF NOT EXISTS dbsproject")
mcursor.execute("USE dbsproject")

#connecting code to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld",
    database="dbsproject",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

# Table creation queries
ledger_table = "CREATE TABLE IF NOT EXISTS ledgers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), total_cash DECIMAL(10, 2))"
transaction_table = "CREATE TABLE IF NOT EXISTS transactions (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, account_title VARCHAR(255), transaction_type VARCHAR(255), cash_amount DECIMAL(10, 2), total_cash_after DECIMAL(10, 2))"
reminder_table = "CREATE TABLE IF NOT EXISTS reminders (id INT AUTO_INCREMENT PRIMARY KEY, loan_title VARCHAR(255), due_date DATE, reminder_type VARCHAR(255))"
users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        username VARCHAR(255) UNIQUE,
        email VARCHAR(255) UNIQUE,
        password_hash VARCHAR(255)
    )
"""
# Execute table creation queries
mycursor.execute(users_table)
mycursor.execute(ledger_table)
mycursor.execute(transaction_table)
mycursor.execute(reminder_table)

# Commit changes
mydb.commit()


#Data array to store data temporarily for showing in the preview window
data = [["Date", "Account title", "Transaction", "Cash(Rs.)", "Total Cash(Rs.)"]]


#Function to close a window
def close(window):
    window.destroy()


#Function to get the total amount of cash left after every transaction
def getTotal(total):
    int(total)
    c = int(cash.get())
    if(transac.get() == 'Cash Recieved' or transac.get() == 'Online Recieved' or transac.get() == 'Loan Recieved' or transac.get() == 'Loan Taken'):
        total += c
    elif(transac.get() == 'Cash Payment' or transac.get() == 'Online Payment' or transac.get() == 'Loan Given' or transac.get() == 'Loan Paid'):
        total -= c


    yield str(total)
   
#Function for reminders
def add_loan_reminder_to_db(title, due_date):
    sql = "INSERT INTO reminders (loan_title, due_date, reminder_type) VALUES (%s, %s, %s)"
    val = (title, due_date, "Loan")
    mycursor.execute(sql, val)
    mydb.commit()


def add_payment_reminder_to_db(title, due_date):
    sql = "INSERT INTO reminders (loan_title, due_date, reminder_type) VALUES (%s, %s, %s)"
    val = (title,due_date, "Payment")
    mycursor.execute(sql, val)
    mydb.commit()


def reminder(frame):
    if transac.get() == "Loan Taken" or transac.get() == "Loan Given":
        if messagebox.askyesno(message='Would you like to add a reminder for the loan?'):
            lbox = simpledialog.askstring("Loan Title", "Enter the name of recipient/donor")
            lbox1 = simpledialog.askstring("Due date", "Enter due date in format dd/mm/yyyy")
            lbox1 = datetime.strptime(lbox1, '%d/%m/%Y').strftime('%Y-%m-%d')
            add_loan_reminder_to_db(lbox, lbox1)  # Inserting data into 'reminders' table for loan
            lplace = 1
            tk.Button(frame, text=lbox).grid(row=lplace, column=0)
            lplace += 1

    if transac.get() == "Payment Due":
        if messagebox.askyesno(message='Would you like to add a reminder for the payment?'):
            pbox = simpledialog.askstring("Payment Title", "Enter the name of recipient/payer")
            pbox1 = simpledialog.askstring("Due date", "Enter due date in format dd/mm/yyyy")
            pbox1 = datetime.strptime(pbox1, '%d/%m/%Y').strftime('%Y-%m-%d')
            add_payment_reminder_to_db(pbox, pbox1)  # Inserting data into 'reminders' table for payment
            pplace = 4
            tk.Button(frame, text=pbox).grid(row=pplace, column=0)
            pplace += 1

            
            


def nexB():
    #Opens the ledger made already
    def openLedger():
        nextB()
   
    global row;  row=2
    #Function to check if the ledger entry box is empty or not
    def add_ledger_to_db(name, total_cash):
        sql = "INSERT INTO ledgers (name, total_cash) VALUES (%s, %s)"
        val = (name, total_cash)
        mycursor.execute(sql, val)
        mydb.commit()
        
    def checkLedger():
        global row
        row += 1
        if ledEntry.index("end") != 0 and tcEntry.index("end") != 0:
            add_ledger_to_db(ledEntry.get(), tcEntry.get())
            nextB()
            tk.Button(ledgerWin, text=ledEntry.get(), font=('Courier New', 20), bg='black', fg='#F0E442',
                    width=30, command=openLedger).grid(row=row, column=0, padx=5, pady=5)
        elif ledEntry.index("end") == 0:
            messagebox.showerror(parent=ledgerWin, title='Error', message='Please enter a valid Ledger name')
        elif tcEntry.index("end") == 0:
            messagebox.showerror(parent=ledgerWin, title='Error', message='Please enter a valid cash amount')
    


    ledgerWin = Tk()
    ledgerWin.title("FinEase")
   
    #Total Available Cash
    global tcEntry
    tcEntry = Entry(ledgerWin, font=('Book Antiqua', 25), width=22)
    tcEntry.insert(0, "Enter starting cash")
    tcEntry.bind("<FocusIn>", lambda e: tcEntry.delete(0, "end"))
    tcEntry.grid(row=0, column=0, padx=5, pady=5)
   
    #Ledger Title
    global ledEntry
    ledEntry = Entry(ledgerWin, font=('Book Antiqua', 25), width=22)
    ledEntry.insert(0, "Enter The Desired Name")
    ledEntry.bind("<FocusIn>", lambda e: ledEntry.delete(0, "end"))
    ledEntry.grid(row=1, column=0, padx=5, pady=5)


    #Add Ledger Button
    tk.Button(ledgerWin, text='+ Add Ledger', font=('Courier New', 20), bg='black', fg='#F0E442',
              width=30, command =checkLedger).grid(row=2, column=0, padx=5, pady=5)
   
    ledgerWin.geometry("500x600")
    ledgerWin.config(background='#212121')
    welcome.destroy()
    ledgerWin.mainloop()




#Code for the main window (after next button is pressed)
def nextB():
    mainWin = Tk()
    mainWin.title("FinEase")

    # Function to display the views
    def show_views():
        query_transaction_summary = "SELECT * FROM user_transaction_summary"
        query_ledger_reminders = "SELECT * FROM user_ledger_reminders"

        mycursor = mydb.cursor()
        mycursor.execute(query_transaction_summary)
        transaction_summary = mycursor.fetchall()

        mycursor.execute(query_ledger_reminders)
        ledger_reminders = mycursor.fetchall()

        mycursor.close()
        mydb.close()

        view_window = tk.Toplevel()
        view_window.title("Financial Overview")

        tk.Label(view_window, text="User Transaction Summary").pack()
        for row in transaction_summary:
            tk.Label(view_window, text=row).pack()

        tk.Label(view_window, text="\nUser Ledger Reminders").pack()
        for row in ledger_reminders:
            tk.Label(view_window, text=row).pack()


        
    #Function for opening a new file
    def newP():
        pass


    #Function for opening an already existing file
    def Open():
        pass


    #Function for saving file
    def save():
        pass


    #Function for changing background color
    def bGround():
        back = colorchooser.askcolor()[1]
        mainWin.config(bg=back)
        accFrame.config(bg=back)
        tFrame.config(bg=back)
        dFrame.config(bg=back)
        lrFrame.config(bg=back)
   
    def addInfo():
        reminder(lrFrame)
        if (dLabel.cget("text") != "" and accEntry.index("end") != 0 and transac.index("end") != 0 and cash.index("end") != 0):
            data.append([dLabel.cget("text"),
                         accEntry.get(),
                         transac.get(),
                         cash.get(),
                         next(getTotal(int(tcEntry.get())))])

        sql = "INSERT INTO transactions (date, account_title, transaction_type, cash_amount, total_cash_after) VALUES (%s, %s, %s, %s, %s)"
        val = (convert_date(dLabel.cget("text")), accEntry.get(), transac.get(), cash.get(), next(getTotal(int(tcEntry.get()))))
    
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo(message="Data added successfully")
        
        
           


    def prevShow():
        #New window for showing preview
        previewWin = Tk()
        previewWin.title("FinEase")


        r = 0;  c = 0
        for elist in data:
            for entry in elist:
                tk.Label(previewWin, text=entry, font=('Arial', 20),
                         bg='#212121',fg='#F5F5F5').grid(row=r, column=c, padx=20, pady=20)
                c+=1
            c=0;  r+=1
       
        tk.Button(previewWin, text='OK', font=('Courier New', 20), bg='black', fg='#F0E442',
                  width=12, command=lambda: close(previewWin)).grid(row=100, column=4, padx=5, pady=5)
       
        previewWin.config(bg='#212121', borderwidth=10, relief='solid')
        previewWin.mainloop()


    #Main menu bar
    menuBar = Menu(mainWin, font=("Book Antiqua", 30));  i=10


    #File drop down menu
    fileMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newP)
    fileMenu.add_command(label="Open", command=Open)
    fileMenu.add_command(label="Save", command=save)
    fileMenu.add_command(label="Save As")#, command=SaveAs)
    fileMenu.add_command(label="Exit", command=lambda: close(mainWin))


    #Edit drop down menu
    editMenu = Menu(menuBar, tearoff=0, font=("Arial", 10))
    menuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Background", command=bGround)
   
    #Font Size menu in Edit Menu
    fsMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font Size', menu=fsMenu)
    while(i<=50):
        fsMenu.add_command(label=str(i));  i+=2
   
    #Font menu in Edit Menu
    fontMenu = Menu(editMenu, tearoff=0, font=('Arial', 10))
    editMenu.add_cascade(label='Font', menu=fontMenu)
    fontMenu.add_command(label="Arial")
    fontMenu.add_command(label="Times New Roman")
    fontMenu.add_command(label="Calibri")


    #Frame to hold the account details
    accFrame = Frame(mainWin,bg='#212121', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    accFrame.grid(row=0, column=0)
    mainWin.grid_rowconfigure(0, weight=1)


    #Date frame
    dFrame = Frame(accFrame, bg='#212121')
    dFrame.grid(row=1, column=1, rowspan=2)


    #Loan Reminder Frame
    lrFrame = Frame(accFrame, bg='#212121')
    lrFrame.grid(row=0, column=2, rowspan=3, columnspan=2)


    #Transactions frame
    tFrame = Frame(mainWin, bg='#212121', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    tFrame.grid(row=1, column=0)
    mainWin.grid_rowconfigure(1, weight=1)


    #Buttons frame
    bFrame = Frame(mainWin, bg='#212121', width=mainWin.winfo_width(), height=mainWin.winfo_height()/3)
    bFrame.grid(row=2, column=0)
    mainWin.grid_rowconfigure(2, weight=1)


    mainWin.grid_columnconfigure(0, weight=1)
   
    #Ledger name as title
    tk.Label(accFrame, text=ledEntry.get(), font=('Book Antiqua', 40, 'bold'),
             bg='#212121',fg='#76C40D').grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 10))
   
    #Account title
    tk.Label(accFrame, text='Account title', font=('Times New Roman', 20),
             bg='#212121',fg='#F5F5F5').grid(row=1, column=0, padx=5, pady=5)


    accEntry = Entry(accFrame, font=('Arial', 20))
    accEntry.grid(row=2, column=0, padx=5, pady=5)


    #Date
    tk.Label(dFrame, text='Date', font=('Arial', 20),
             bg='#212121',fg='#F5F5F5').grid(row=0, column=0, columnspan=3, padx=5, pady=5)


    def setDate():
        def okButton():
            dLabel.config(text=calendar.get_date())
            close(calWin)
       
        calWin = Tk()
        calWin.title("Calendar")
        calWin.title("Select Date")
        #Calendar to get date
        calendar = Calendar(calWin, selectmode='day', year=2023, month=int(strftime("%m")), day=1)
        calendar.pack()
        calWin.lift()
        tk.Button(calWin, text='OK', command=okButton).pack(side='bottom')


   
    dLabel = Label(dFrame, text="", font=('Arial', 20), bg='white', width=10)
    dLabel.grid(row=1, column=0, padx=5, pady=5)


    tk.Button(dFrame, text='Select Date', font=('Times New Roman', 15), bg='black', fg='#FC4C4F',
              width=10, command=setDate).grid(row=1, column=1, padx=5, pady=5)


    tk.Label(lrFrame, text='Loans:', font=('Times New Roman', 20), bg='#212121',fg='#F5F5F5').grid(row=0, column=0, padx=5, pady=5)


    tk.Label(lrFrame, text='Payments:', font=('Times New Roman', 20), bg='#212121',fg='#F5F5F5').grid(row=4, column=0, padx=5, pady=5)


    #Transaction
    tk.Label(tFrame, text='Select Transaction', font=('Times New Roman', 20), bg='#212121',fg='#F5F5F5').grid(row=0, column=0, padx=5, pady=5)


    global transac
    transac = ttk.Combobox(tFrame, values=['Cash Recieved', 'Online Recieved', 'Cash Payment',
                                          'Online Payment', 'Loan Given', 'Loan Recieved',
                                          'Loan Taken', 'Loan Paid', 'Payment Due'],
                                          font=('Arial', 20), width=20)
    transac.grid(row=1, column=0, padx=5, pady=5)


    #Amount of Cash/Payment
    tk.Label(tFrame, text='Amount(Cash)', font=('Times New Roman', 20),
             bg='#212121',fg='#F5F5F5').grid(row=0, column=1, padx=5, pady=5)


    global cash
    cash = Entry(tFrame, font=('Arial', 20), width=20)
    cash.grid(row=1, column=1, padx=5, pady=5)
    
    #Button to add the info to a text file
    add_button = tk.Button(bFrame, text='Add', font=('Courier New', 20), bg='black', fg='#F0E442',
                        width=12, command=addInfo)
    add_button.grid(row=0, column=0, padx=(0, 5))

    #Button to show preview
    preview_button = tk.Button(bFrame, text='Show Preview', font=('Courier New', 20), bg='black', fg='#F0E442',
                            width=12, command=prevShow)
    preview_button.grid(row=0, column=1, padx=(5, 0))

    #Button to show views
    show_views_button = tk.Button(bFrame, text='Financials', font=('Courier New', 20), bg='black', fg='#F0E442',
                                width=12, command=show_views)  
    show_views_button.grid(row=0, column=2, padx=(5, 0))


    mainWin.geometry("800x600")
    mainWin.config(background="#212121", menu=menuBar)




def login():
    def add_user_to_db(name, username, email, password):
        hashed_password = hash_password(password)
        sql = "INSERT INTO users (name, username, email, password_hash) VALUES (%s, %s, %s, %s)"
        val = (name, username, email, hashed_password)
        mycursor.execute(sql, val)
        mydb.commit()
        
    def collect_signup_data_and_add_to_db():
        name = name_entry.get()
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        add_user_to_db(name, username, email, password)
        nexB()  # Open the next window

    Login = Tk()
    Login.title("FinEase")
   
    tk.Label(Login, text="Log In", font=('Book Antiqua', 30, 'bold'), bg='#212121',fg='#76C40D').grid(row=0, column=0, padx=5, pady=5, columnspan=2)
   
    tk.Label(Login, text="Name: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=1, column=0, padx=5, pady=5)
    name_entry = tk.Entry(Login, font=('Arial', 20, 'bold'))
    name_entry.grid(row=2, column=0, padx=5, pady=5)

    tk.Label(Login, text="User name: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=1, column=1, padx=5, pady=5)
    username_entry = tk.Entry(Login, font=('Arial', 20, 'bold'))
    username_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(Login, text="E-mail: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=3, column=0, padx=5, pady=5)
    email_entry = tk.Entry(Login, font=('Arial', 20, 'bold'))
    email_entry.grid(row=4, column=0, padx=5, pady=5)

    tk.Label(Login, text="Password: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=3, column=1, padx=5, pady=5)
    password_entry = tk.Entry(Login, font=('Arial', 20, 'bold'), show='*')
    password_entry.grid(row=4, column=1, padx=5, pady=5)
   
    signup_button = tk.Button(Login, text='Sign Up', font=('Courier New', 30), bg='black', fg='#F0E442', command=collect_signup_data_and_add_to_db)
    signup_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
   
    Login.resizable(False, False)
    Login.config(background="#212121")
    Login.mainloop()
    
    
    

def check_user_credentials(username, password):
    # MySQL query to retrieve the hashed password for the provided username
    query = "SELECT password_hash FROM users WHERE username = %s"
    cursor = mydb.cursor()
    cursor.execute(query, (username,))
    stored_hash = cursor.fetchone()

    if stored_hash:
        stored_hash = stored_hash[0].encode('utf-8')
        input_password = password.encode('utf-8')

        # Compare the input password with the stored hashed password using bcrypt
        if bcrypt.checkpw(input_password, stored_hash):
            return True

    return False


def signin():
    def open_new_window():
        nexB()

    def verify_credentials():
        # Get username and password from the entry widgets
        username = username_entry.get()
        password = password_entry.get()

        # Verify credentials against the database
        if check_user_credentials(username, password):
            print("Credentials verified")
            open_new_window()  # Open a new window on successful verification
        else:
            print("Invalid credentials")  # Replace this with your logic for invalid credentials

    Signin = tk.Tk()
    Signin.title("FinEase")

    tk.Label(Signin, text="Sign In", font=('Book Antiqua', 30, 'bold'), bg='#212121',fg='#76C40D').grid(row=0, column=0, padx=5, pady=5)

    tk.Label(Signin, text="User name: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=1, column=0, padx=5, pady=5)
    username_entry = tk.Entry(Signin, font=('Arial', 20, 'bold'))
    username_entry.grid(row=2, column=0, padx=5, pady=5)

    tk.Label(Signin, text="Password: ", font=('Times New Roman', 20, 'bold'), bg='#212121',fg='#F5F5F5').grid(row=3, column=0, padx=5, pady=5)
    password_entry = tk.Entry(Signin, font=('Arial', 20, 'bold'), show='*')
    password_entry.grid(row=4, column=0, padx=5, pady=5)

    tk.Button(Signin, text='NEXT', font=('Courier New', 30), bg='black', fg='#F0E442', command=verify_credentials).grid(row=5, column=0, padx=5, pady=5)

    Signin.resizable(False, False)
    Signin.config(background="#212121")
    Signin.mainloop()



#Welcome window
welcome = Tk()
welcome.title("FinEase")


tk.Label(welcome, text="FINEASE", font=('Book Antiqua',50,'bold'),bg='#212121',fg='#76C40D').pack()
tk.Label(welcome, text="WELCOME", font=('Times New Roman',48),bg='#212121',fg='#F5F5F5').pack()


tk.Button(text='LOGIN', font=('Courier New',40), bg='black', fg='#F0E442', command=login).pack()
tk.Button(text='SIGN IN', font=('Courier New',40), bg='black', fg='#F0E442', command=signin).pack()


welcome.geometry("500x500")
welcome.config(background="#212121")


welcome.mainloop()

mydb.close()