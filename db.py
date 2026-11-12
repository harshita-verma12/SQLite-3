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
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS parents(
     Id INTEGER PRIMARY KEY AUTOINCREMENT,
     M.NAME VARCHAR(50) ,
     F.NAME VARCHAR(50)
)
    
        """)



cursor.executemany(
     "INSERT INTO parents(M.NAME , F.NAME)VALUES(?,?)",
     [
     ("MOTHER1","FATHER1") ,
     ("MOTHER2" , "FATHER2") ,
     ("MOTHER3" , "FATHER3")

         
     ]



      )
cursor.execute("SELECT * FROM parents")
newtable = cursor.fetchall()
for i in newtable:
    print(i)
conn.commit()    