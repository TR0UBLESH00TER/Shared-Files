# 10. Write a program to read the content of a file line by line and write it to another file except for 
# the lines containing the word  ‘is’ in it.
f1 = open("Read.txt","r")
f2 = open("Write.txt","w")
#while True:
    #try:
data = f1.readline()
if "is" not in data:
    f2.write(data)
    #except EOFError:
        #break
f1.close()
f2.close()
print("Data added successfully!")
