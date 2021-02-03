# 11. Write a program to read the content of a text file and to display no of Consonants, Vowels, Uppercase 
# and Lowercase characters in that file
constants = vowels= uppercase = lowercase = 0
with open(".\\data\\read-me.txt","r") as f:
    data = f.read()
    f.close()
for i in data:
    if i.isdigit():
        constants += 1
    if i.lower() in ("a","e","i","o","u"):
        vowels += 1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase += 1
print(f"Number of constants = {constants}\nNumber of vowels = {vowels}\nNumber of uppercase = {uppercase}\n Number of lowercase = {lowercase}")