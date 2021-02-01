# 📂 Practical Programs 📚
⭐ *Just some simple programs* ⭐
##### 💻 All programs are written in Python 3 🐍

<br /> **Questions:**
1.	Write a function to find factorial of a number.
2.	Write a function to accept a number from user and to check whether it Prime or not.
3.	Write a Python program  `remdup( l )` to remove duplicates from a list.
4.	Write a function to search a given word in a string.
5.	Write a function to check whether a string is Palindrome or not.
6.	Write a function to find the occurance of a word in a string.
7.	Write a function to compute n terms of Fibonacci number.
8.	Write a function to display sum of even numbers or sum of odd numbers in a list, based on users choice.
9.	Write a program to read and display the file content line by line with each word separated by “#”
10.	Write a program to read the content of a file line by line and write it to another file except for the lines containing the word ‘is’ in it.
11.	Write a program to read the content of a text file and to display no of Consonants, Vowels, Uppercase and Lowercase characters in that file.
12.	Write a program to create a binary file to store Roll no and Name , search any Roll no and display name if Roll no is found otherwise, displays message “Roll no not found” .
13.	Write a program to create a binary file to store Rollno, Name and Marks of students and to update the marks of an entered Roll no, if found otherwise display appropriate message.
14.	WAP to create a CSV file Stud.csv with records to store roll no, name and marks. It reads the contents, count and display only those records whose marks > 90.
15.	Write a program to create CSV file and store empno, name,salary and search any empno and to display his/her name and salary. If not found , an appropriate message to be displayed.
16.	Write a program to perform operations on stack in python using list.
17.	Write a program to connect with database and store record of employees and to display the records.
18.	Write a program to connect with database and search an employee number in the table EMP and to display record. If  employee number not found then appropriate message to be displayed.
19.	Write a program to connect with database and to fetch the record from EMP table based on the condition specified by user.
20.	Write a program to connect with database and to delete the record from EMP table based on the entered Emp no (if found).

<br /> *The table Emp used in 17, 18, 19, 20:*
```mysql
mysql> DESC Emp;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| Empno  | int(2)      | NO   | PRI | NULL    |       | 
| Name   | varchar(20) | NO   |     | NULL    |       | 
| Dept   | varchar(10) | YES  |     | NULL    |       | 
| Salary | int(9)      | YES  |     | NULL    |       | 
+--------+-------------+------+-----+---------+-------+

mysql> SELECT * FROM Emp;
+-------+--------+-------+--------+ 
| Empno | Name   | Dept  | Salary | 
+-------+--------+-------+--------+ 
|     1 | Ravi   | Sales |  24000 | 
|     2 | Sunny  | Sales |  35000 | 
|     3 | Shobit | IT    |  30000 | 
|     4 | Vikram | IT    |  40000 | 
|     5 | Adam   | HR    |  50000 | 
+-------+--------+-------+--------+ 
```
