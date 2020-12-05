# 13. Write a program to create a binary file to store Rollno, Name and Marks of students and to update the 
# marks of an entered Roll no, if found otherwise display appropriate message.
from pickle import dump, load
file = open('studentData.dat','wb')
data=[]
ans = 'y'
while ans.lower() == 'y':
    roll_no = int(input("Enter the Roll No.: "))
    name = input("Enter the Name    : ")
    marks = input("Enter the Marks   : ")
    data.append([roll_no,name,marks])
    ans = input("Enter more records?(Y?N): ")
dump(data,file)
file.close()
file = open('StudentData.dat','rb+')
data = load(file)
check = int(input("Enter the Roll No to update Marks: "))
for i in data:
    if i[0] == check:
        update = int(input("Enter the new marks: "))
        i[2] = update
        dump(data,file)
        break
else:
    print("Record not found.")