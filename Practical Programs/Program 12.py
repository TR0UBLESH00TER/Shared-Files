# 12. Write a program to create a binary file to store Roll no and Name , search any Roll no and display name 
# if Roll no is found otherwise, displays message “Roll no not found” 

from pickle import dump
File = open('studentData.dat','wb')
data=[]
ans = 'y'
while ans.lower() == 'y':
    roll_no = int(input("Enter the Roll No.: "))
    name = input("Enter the Name    : ")
    data.append((roll_no,name))
    ans = input("Enter more records?(Y?N): ")
dump(data,File)
File.close()
check = int(input("Enter the Roll No to find: "))
for i in data:
    if i[0] == check:
        print("Roll No found. Name of student:",i[1])
        break
else:
    print("Record not found.")

#OR

from pickle import dump
file = open('studentData.dat','wb')
data={}
ans = 'y'
while ans.lower() == 'y':
    roll_no = int(input("Enter the Roll No.: "))
    name = input("Enter the Name    : ")
    data[roll_no] = name
    ans = input("Enter more records?(Y?N): ")
dump(data,file)
file.close()
check = int(input("Enter the Roll No to find: "))
for i in data:
    if i == check:
        print("Roll No found. Name of student:",data[i])
        break
else:
    print("Record not found.")