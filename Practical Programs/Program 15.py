# 15. Write a program to create CSV file and store empno, name,salary and search any empno and to display
# his/her name and salary. If not found , an appropriate message to be displayed
import csv
f = open("emp.csv","a",newline="")
writer = csv.writer(f)
ans = 'y'
while ans.lower() == 'y':
    empno = int(input("Enter the Employee Number: "))
    name = input("Enter the Name           : ")
    salary = input("Enter the Salary         : ")
    data =[empno,name,salary]
    writer.writerow(data)
    ans = input("Enter more records?(Y?N): ")
f.close()
