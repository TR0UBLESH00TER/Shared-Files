# 17. Write a program to connect with database and store record of employees and to display the records
import mysql.connector as sql
db = sql.connect(host = "localhost", user ="root", password="mysql",database ="12b_practical",charset="utf8")
cursor = db.cursor()
ans = "y"
while ans.lower() == "y":
    Emp_ID = int(input("Enter Employee ID: "))
    Name = input("Enter Employee Name: ")
    Salary = int(input("Enter Salary: "))
    Dept = input("Enter Department: ")
    try:
        cursor.execute(f"INSERT INTO EMP VALUES({Emp_ID},\'{Name}\',{Salary},\'{Dept}\');")
        db.commit()
        print("Data added successfully.")
    except Exception as e:
        print(f"Error occured: {e}")
    ans = input("Enter more records? (y/n): ")
cursor.execute("SELECT * FROM EMP;")
data = cursor.fetchall()
for i in data:
    print(i)
