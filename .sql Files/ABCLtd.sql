CREATE DATABASE ABC;
USE ABC;
CREATE TABLE ABCLtd(
    empno INT PRIMARY KEY, 
    name VARCHAR(20) NOT NULL,
    dept VARCHAR(20) DEFAULT 'Marketing',
    salary INT
);

INSERT INTO ABCLtd VALUES(1,'Freddy','Sales',60000);
INSERT INTO ABCLtd(empno,name,salary) VALUES(2,'Greg',80000);
SELECT * FROM ABCLtd;
DESC ABCLtd;

/* Creating Training using Foreign key */ 
CREATE TABLE Training(
    empno INT, 
    trainingname VARCHAR(20),
    startdate date,
    enddate date,
    CONSTRAINT myfkey FOREIGN KEY(empno) REFERENCES ABCLtd(empno)
);
INSERT INTO Training VALUES(1,'SBSB','2018-11-15','2018-11-17');
SELECT * FROM Training;
DESC Training;