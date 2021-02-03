# 10. Write a program to read the content of a file line by line and write it to another file except for 
# the lines containing the word  ‘is’ in it.
f1 = open(".\\data\\read-me.txt","r")
data = f1.readlines()
f1.close()
f2 = open(".\\data\\write-me.txt","w")
for i in data:
    if "is" not in i.split():
        f2.write(i)
f2.close()
print("Data copied successfully!")
