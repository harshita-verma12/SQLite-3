import sqlite3


try:
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    print("connected successfully !")
except :
    print("connection wasn't done !")    
finally :
    print("everything is donee !")    

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
      ID INT PRIMARY KEY AUTOINCREMENT,
      name VARCHAR(50),
      age INT NOT NULL
          )
              """)
cursor.executemany(
       "INSERT INTO students(name,age) VALUES(?,?)",
       [
       ("harshita verma" , 18),
       ("anu" , 20),
       ("shefali",21)
       ]
         )
cursor.execute(" SELECT * FROM students ")

rows = cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()    