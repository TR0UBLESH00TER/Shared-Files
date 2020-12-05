# 18. Write a program to connect with database and search an employee number in the table EMP and to display record. 
# If  employee number not found then appropriate message to be displayed.
import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'mysql', database = '12b')
cursor = conn.cursor()
query = "SELECT * FROM Emp"
cursor.execute(query)
data = cursor.fetchall()
search = int(input("Enter the Employee Number to search: "))
for row in data:
    if row[0] == search:
        print(row)
        break
else:
    print("Data not found.")
