# 9. Write a program to read and display the file content line by line with each word separated by "#"
with open(".\\data\\word-hash.txt","r") as f:
    data = f.read()
    for i in data:
        if i == " ":
            print("#",end="")
        else:
            print(i,end="")
    f.close()