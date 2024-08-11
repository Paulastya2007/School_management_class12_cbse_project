CREATE DATABASE IF NOT EXISTS school_management;
USE school_management;

#Create student table
CREATE TABLE student (
    sname VARCHAR(30) NOT NULL,
    admno INT(11) PRIMARY KEY,
    dob DATE,
    cls CHAR(2),
    cty VARCHAR(20)
);

CREATE TABLE emp (
    empno INT(11) PRIMARY KEY,
    ename VARCHAR(20),
    job VARCHAR(20),
    hiredate DATE
);

CREATE TABLE fee (
    admno INT(11),
    fee INT(11),
    month VARCHAR(15)
);

CREATE TABLE exam (
    sname VARCHAR(20),
    admno INT(11),
    per DECIMAL(4,2),
    res VARCHAR(10)
);
