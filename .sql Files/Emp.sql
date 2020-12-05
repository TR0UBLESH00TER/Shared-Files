/*Type mysql>source F:\Computer Science\SQL\Emp.sql in sql commandline to run this file.*/
/*Write mysql -u root -p in cmd to open mysql*/
CREATE DATABASE 12b;
USE 12b;
CREATE TABLE Emp(
    Empno int(2) NOT NULL PRIMARY KEY,
    Name varchar(20) NOT NULL,
    Dept varchar(10),
    Salary int(9)
    );

INSERT INTO Emp VALUES(1,"Ravi","Sales",24000);
INSERT INTO Emp VALUES(2,"Sunny","Sales",35000);
INSERT INTO Emp VALUES(3,"Shobit","IT",30000);
INSERT INTO Emp VALUES(4,"Vikram","IT",27000);
INSERT INTO Emp VALUES(5,"nitin","HR",45000);

SELECT * FROM Emp;
SELECT "Table created!" FROM DUAL;

