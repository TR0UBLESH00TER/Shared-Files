# 20. Write a program to connect with database and to delete the record from EMP table based on the entered 
# Emp no (if found).
import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'mysql', database = '12b')
cursor = conn.cursor()
delete = input("Enter the Employee Number to delete: ")
query = "DELETE FROM Emp WHERE Empno = "+delete
cursor.execute(query)
conn.commit()
print("Record deleted!")