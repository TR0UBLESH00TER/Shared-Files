# 12. Write a program to create a binary file to store Roll no and Name , search any Roll no and display name 
# if Roll no is found otherwise, displays message “Roll no not found” 

import pickle
with open(".\\data\\roll-stud.dat","wb") as f:
    ans = "y"
    while ans.lower() == "y":
        Roll = int(input("Enter Roll No.: "))
        Name = input("Enter Student\'s Name: ")
        pickle.dump([Roll,Name],f)
        print("Data added successfully.")
        ans = input("Add more record? (y/n): ")
    f.close()
    
with open(".\\data\\roll-stud.dat","rb") as f:
    data = []
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            f.close()
            break

check_roll = int(input("Enter Roll No. to search: "))
for record in data:
    if record[0] == check_roll:
        print("Roll no found!\n Name:",record[1])
        break
else:
    print("Roll No. not found")