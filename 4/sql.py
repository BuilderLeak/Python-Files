import sqlite3

connection = sqlite3.connect("example.db")

#connection.execute("CREATE TABLE student (Rno VARCHAR(16), Name TEXT, Marks INTEGER)")

#connection.execute("CREATE TABLE student (Rno VARCHAR(16), Name TEXT, Marks INTEGER)")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('101', 'Jyothi', 46)")
connection.execute("UPDATE student SET Marks = 40 WHERE Marks = 46")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('102', 'Kumar', 86)")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('103', 'Siddarth', 26)")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('104', 'Riya', 75)")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('105', 'King', 43)")
connection.execute("INSERT INTO student (Rno, Name, Marks) VALUES ('106', 'Leela', 43)")

connection.execute("DELETE FROM student WHERE Rno =105")

connection.commit()
cursor= connection.execute("SELECT * FROM student")

for row in cursor:
  print(row)