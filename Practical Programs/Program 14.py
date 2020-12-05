# 14. WAP to create a CSV file Stud.csv with records to store roll no, name and marks. It reads the contents, 
# count and display only those records whose marks > 90
import csv
f = open("Stud.csv","a",newline="")
writer = csv.writer(f)
ans = 'y'
while ans.lower() == 'y':
    rollno = int(input("Enter the Roll Number: "))
    name   = input("Enter the Name       : ")
    marks  = int(input("Enter the Marks      : "))
    data =[rollno,name,marks]
    writer.writerow(data)
    ans = input("Enter more records?(Y?N): ")
f.close()

f = open("Stud.csv","r")
reader = csv.reader(f)
count = 0
for line in reader:
    if line[2] > 90:
        print(line)
        count+=1
print("Number of records whose marks > 90 is",count)