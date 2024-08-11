-- Insert dummy data into the student table
INSERT INTO student (sname, admno, dob, cls, cty)
VALUES 
('John Doe', 1001, '2005-06-15', '10', 'New York'),
('Jane Smith', 1002, '2006-04-22', '9', 'Los Angeles'),
('Michael Brown', 1003, '2004-11-30', '12', 'Chicago'),
('Emily Davis', 1004, '2005-02-19', '11', 'Houston');

-- Insert dummy data into the emp table
INSERT INTO emp (empno, ename, job, hiredate)
VALUES 
(1, 'Alice Johnson', 'Teacher', '2015-08-01'),
(2, 'Bob Williams', 'Principal', '2010-01-15'),
(3, 'Carol Miller', 'Clerk', '2018-06-23'),
(4, 'David Wilson', 'Teacher', '2017-09-10');

-- Insert dummy data into the fee table
INSERT INTO fee (admno, fee, month)
VALUES 
(1001, 500, 'January'),
(1002, 550, 'February'),
(1003, 520, 'March'),
(1004, 510, 'April');

-- Insert dummy data into the exam table
INSERT INTO exam (sname, admno, per, res)
VALUES 
('John Doe', 1001, 88.50, 'Pass'),
('Jane Smith', 1002, 91.00, 'Pass'),
('Michael Brown', 1003, 76.30, 'Pass'),
('Emily Davis', 1004, 84.75, 'Pass');
