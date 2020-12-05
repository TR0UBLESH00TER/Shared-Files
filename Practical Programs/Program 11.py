# 11. Write a program to read the content of a text file and to display no of Consonants, Vowels, Uppercase 
# and Lowercase characters in that file
f = open("file.txt","r")
data = f.read()
f.close()
ConsonantsNo,VowelsNo,UppercaseNo,LowercaseNo=0,0,0,0
for i in data:
    if i.isalpha():
        if i.lower() in ("a","e","i","o","u"):
            VowelsNo+=1
        else:
            ConsonantsNo+=1
        if i.isupper():
            UppercaseNo+=1
        else:
            LowercaseNo+=1
print("Number of Consonants          :",ConsonantsNo)
print("Number of Vowels              :",VowelsNo)
print("Number of Uppercase Characters:",UppercaseNo)
print("Number of Lowercase Characters:",LowercaseNo)