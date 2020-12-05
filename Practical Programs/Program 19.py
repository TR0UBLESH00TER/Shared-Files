# 19. Write a program to connect with database and to fetch the record from EMP table based on 
# the condition specified by user.
import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'mysql', database = '12b')
cursor = conn.cursor()
query = "SELECT * FROM Emp"
cursor.execute(query)
data = cursor.fetchall()
search = input("Enter the Department to search: ")
flag = True
for row in data:
    if row[2] == search:
        print(row)
        flag = False
if flag:
    print("Data not found.")