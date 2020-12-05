#### PRACTICAL PROGRAMS
All the pratical programs here.
<br> The questions are mentioned as a comment in every program.

##### The table Emp:
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
