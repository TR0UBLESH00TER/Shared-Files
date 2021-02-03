# 18. Write a program to connect with database and search an employee number in the table EMP and to display record. 
# If  employee number not found then appropriate message to be displayed.
import mysql.connector as sql
db = sql.connect(host = "localhost", user ="root", password="mysql",database ="12b_practical",charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT * FROM EMP;")
data = cursor.fetchall()
Emp_ID = int(input("Enter Employee ID to search: "))
for i in data:
    if i[0] == Emp_ID:
        print("Record found!")
        print(i)
        break
else:
    print("Record not found.")