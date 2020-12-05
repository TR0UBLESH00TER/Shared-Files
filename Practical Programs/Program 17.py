# 17. Write a program to connect with database and store record of employees and to display the records
import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'mysql', database = '12b')
cursor = conn.cursor()
ans = 'y'
while ans.lower() == 'y':
    Empno = int(input("Enter Employee Number: "))
    Name = input("Enter Name: ")
    Dept = input("Enter Department: ")
    Salary = int(input("Enter Salary: "))
    query = f"INSERT INTO Emp VALUES({Empno},\'{Name}\',\'{Dept}\',{Salary})"
    cursor.execute(query)
    conn.commit()
    print("-- Record Added --")
    ans = input("Enter more records? (Y/N) ")

query = "SELECT * FROM Emp"
cursor.execute(query)
data = cursor.fetchall()
for row in data:
    print(row)
