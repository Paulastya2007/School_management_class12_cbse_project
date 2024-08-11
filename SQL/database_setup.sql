CREATE DATABASE school_management;

USE school_management;



CREATE TABLE student (
    sname VARCHAR(30) NOT NULL,
    admno INT PRIMARY KEY,
    dob DATE,
    cls CHAR(2),
    cty VARCHAR(20)
);



CREATE TABLE emp (
    empno INT PRIMARY KEY,
    ename VARCHAR(20),
    job VARCHAR(20),
    hiredate DATE
);


CREATE TABLE fee (
    admno INT,
    fee INT,
    month VARCHAR(15),
    FOREIGN KEY (admno) REFERENCES student(admno)
);


CREATE TABLE exam (
    sname VARCHAR(20),
    admno INT,
    per DECIMAL(4,2),
    res VARCHAR(10),
    FOREIGN KEY (admno) REFERENCES student(admno)
);
