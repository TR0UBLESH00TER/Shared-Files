# 15. Write a program to create CSV file and store empno, name,salary and search any empno and to display
# his/her name and salary. If not found , an appropriate message to be displayed
import csv
f = open(".\\data\\emp.csv","a",newline="")
writer = csv.writer(f)
ans = 'y'
while ans.lower() == 'y':
    empno = int(input("Enter the Employee Number: "))
    name = input("Enter the Name           : ")
    salary = input("Enter the Salary         : ")
    data =[empno,name,salary]
    writer.writerow(data)
    ans = input("Enter more records?(Y/N): ")
f.close()

f = open(".\\data\\emp.csv","r")
reader = csv.reader(f)
empid=int(input("Enter the employee ID to search: "))
for data in reader:
    if int(data[0]) == empid:
        print(data)
        break
else:
    print("Data not found.")