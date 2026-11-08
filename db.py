import sqlite3


try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    print("connected successfully !")
except :
    print("connection wasn't done !")    
finally :
    print("everything is donee !")    
