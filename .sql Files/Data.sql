/*
Type 
mysql> source <path of directory where file is saved>\Data.sql 
in sql commandline to run this file.
*/

/* Create a database 12b before running this */

USE 12b;

CREATE TABLE TEACHER(
    TEACHER_CODE CHAR(4) PRIMARY KEY NOT NULL,
    TEACHER_NAME VARCHAR(15) NOT NULL,
    DOJ DATE
);

INSERT INTO TEACHER VALUES("T001","ANAND" ,'2001-01-30');
INSERT INTO TEACHER VALUES("T002","AMIT"  ,'2007-09-05');
INSERT INTO TEACHER VALUES("T003","ANKIT" ,'2007-09-20');
INSERT INTO TEACHER VALUES("T004","BALBIR",'2010-02-15');
INSERT INTO TEACHER VALUES("T005","JASBIR",'2011-01-20');
INSERT INTO TEACHER VALUES("T006","KULBIR",'2008-07-11');

SELECT "Displaying..." AS "Table created!";
SELECT * FROM TEACHER;

SELECT "SELECT TEACHER_NAME,DOJ FROM TEACHER WHERE TEACHER_NAME LIKE '%I%';" AS "Q2 (i)";
SELECT TEACHER_NAME,DOJ FROM TEACHER WHERE TEACHER_NAME LIKE "%I%";

SELECT "SELECT * FROM TEACHER WHERE DOJ LIKE '%-09-%'" AS "Q2 (ii)";
SELECT * FROM TEACHER WHERE DOJ LIKE "%-09-%";
