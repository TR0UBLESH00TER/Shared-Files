# 9.	Write a program to read and display the file content line by line with each word separated by “#”
File = open("data.txt","r")
data = File.read()
for i in data:
    if i == " ":
        print("#",end="")
    else:
        print(i,end="")
File.close()