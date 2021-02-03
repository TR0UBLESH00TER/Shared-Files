# 20. Write a program to connect with database and to delete the record from EMP table based on the entered 
# Emp no (if found).
import mysql.connector as sql
db = sql.connect(host = "localhost", user ="root", password="mysql",database ="12b_practical",charset="utf8")
cursor = db.cursor()
Emp_ID = int(input("Enter Employee ID to delete: "))
cursor.execute(f"DELETE FROM EMP where Employee_ID = {Emp_ID};")
db.commit()
if cursor.rowcount == 0:
    print("Record not found.")
else:
    print("Record deleted successfully.")