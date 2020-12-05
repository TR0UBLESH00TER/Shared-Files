CREATE DATABASE DUMMY;
USE DUMMY;
CREATE TABLE STATIONERY(
    ItemNo INT(4) NOT NULL,
    Item VARCHAR(25) NOT NULL,
    Dcode INT(3),
    Qty INT(3),
    UnitPrice INT(3),
    StockDate DATE
);

INSERT INTO STATIONERY VALUES(
    5005,"Ball Pen 0.5"     ,102 ,100,16,"2018-03-10"
);
INSERT INTO STATIONERY VALUES(
    5003,"Ball Pen 0.25"    ,102 ,150,20,"2017-05-17"
);
INSERT INTO STATIONERY VALUES(
    5002,"Gel Pen Premium"  ,101 ,125,14,"2018-04-20"
);
INSERT INTO STATIONERY VALUES(
    5006,"Gel Pen Classic"  ,101 ,200,22,"2018-10-08"
);
INSERT INTO STATIONERY VALUES(
    5001,"Eraser Small"     ,102 ,210,5 ,"2018-03-11"
);
INSERT INTO STATIONERY VALUES(
    5004,"Eraser Big"       ,102 ,60 ,10,"2017-11-18"
);
INSERT INTO STATIONERY VALUES(
    5009,"Sharpener Classic",NULL,160,8 ,"2017-06-12"
);

/*1. Select all record of table */
SELECT "Select all record of table" AS "Q1";
SELECT * FROM STATIONERY;

/*2. Select ItemNo, name and Unitprice */
SELECT "Select ItemNo, name and Unitprice" AS "Q2";
SELECT ItemNo,Item name,Unitprice FROM STATIONERY;

/*3. Select all records where Unitprice is more than 20 */
SELECT "Select all records where Unitprice is more than 20" AS "Q3";
SELECT * FROM STATIONERY WHERE UnitPrice > 20;

/*4. Select Item name of those items which are quantity between 100-200 */
SELECT "Select Item name of those items which are quantity between 100-200" AS "Q4";
SELECT  Item FROM STATIONERY WHERE Qty BETWEEN 100 AND 200;

/*5. Select all record of Items which contains Pen word in it */
SELECT "Select all record of Items which contains Pen word in it" AS "Q5";
SELECT * FROM STATIONERY WHERE Item LIKE "%Pen%";

/*6. Select unique Dcode of all items */
SELECT "Select unique Dcode of all items" AS "Q6";
SELECT DISTINCT Dcode FROM STATIONERY;

/*7. Display all records in the descending order of UnitPrice */
SELECT "Display all records in the descending order of UnitPrice" AS "Q7";
SELECT * FROM STATIONERY ORDER BY UnitPrice DESC;

/*8. Display all items which are stocked in the month March */\
SELECT "Display all items which are stocked in the month March" AS "Q8";
SELECT Item FROM STATIONERY WHERE StockDate LIKE "%-03-%";

/*11. Change the UnitPrice to 20 for ItemNo 5005 */
SELECT "Change the UnitPrice to 20 for ItemNo 5005" AS "Q11";
UPDATE STATIONERY SET UnitPrice = 20 WHERE ItemNo = 5005;
SELECT * FROM STATIONERY;
UPDATE STATIONERY SET UnitPrice = 16 WHERE ItemNo = 5005;

/*12. Delete the record of ItemNo 5001 */
SELECT "Delete the record of ItemNo 5001" AS "Q12";
DELETE FROM STATIONERY WHERE ItemNo = 5001;
SELECT * FROM STATIONERY;
TRUNCATE TABLE STATIONERY;
INSERT INTO STATIONERY VALUES(5005,"Ball Pen 0.5"     ,102 ,100,16,"2018-03-10");
INSERT INTO STATIONERY VALUES(5003,"Ball Pen 0.25"    ,102 ,150,20,"2017-05-17");
INSERT INTO STATIONERY VALUES(5002,"Gel Pen Premium"  ,101 ,125,14,"2018-04-20");
INSERT INTO STATIONERY VALUES(5006,"Gel Pen Classic"  ,101 ,200,22,"2018-10-08");
INSERT INTO STATIONERY VALUES(5001,"Eraser Small"     ,102 ,210,5 ,"2018-03-11");
INSERT INTO STATIONERY VALUES(5004,"Eraser Big"       ,102 ,60 ,10,"2017-11-18");
INSERT INTO STATIONERY VALUES(5009,"Sharpener Classic",NULL,160,8 ,"2017-06-12");

/*13. Display all the item name in capital letters */
SELECT "Display all the item name in capital letters" AS "Q13";
SELECT UPPER(Item) AS "ITEM IN UPPERCASE" FROM STATIONERY;

/*14. Display first 4 character of every item name */
SELECT "Display first 4 character of every item name" AS "Q14";
SELECT SUBSTRING(Item,1,4) AS "First 4 characters of item name" FROM STATIONERY;

/*15. Display all records whose Dcode is not assigned */
SELECT "Display all records whose Dcode is not assigned" AS "Q15";
SELECT * FROM STATIONERY WHERE Dcode IS NULL;

/*DROP DATABASE DUMMY;*/
