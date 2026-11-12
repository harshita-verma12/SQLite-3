import sqlite3


try:
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    print("connected successfully !")
except :
    print("An unknown error occured !!!")       

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Expense(
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      date DATE ,   
      expense  CHAR,
      price INT 
          )
              """)

def add_expense():
    date = input("enter the date:")
    expense = input("where did you spend ???? what was the expense...")
    price = float(input("enter the price.."))
    
    
    cursor.execute(
        'INSERT INTO Expense(date , expense , price)VALUES(?,?,?)' ,
        (date,expense,price)

    )
    conn.commit()
    print("added successfully !!")

def view_expense():
    cursor.execute('SELECT * FROM Expense')
    rows = cursor.fetchall()  
    for i in rows:
        print(i)  
    print("spend thoughfully !!!")  


print("TRACK YOUR EXPENSES !")      

while True :
    print("\n1. Add an expense \n2. view expenses\n3. Exit")   
    choice = input("select an option : ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        break
    else :
        print("invalid choice ! ")    


conn.close()
print("Connection closed. Program exited.")
1