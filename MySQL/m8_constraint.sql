CREATE TABLE emp1(
empno	DECIMAL(4)	PRIMARY KEY,
ename	VARCHAR(30)	NOT NULL,
hiredate date		NOT NULL,
email	VARCHAR(30)	UNIQUE,
deptno	DECIMAL(3)	NOT NULL,
salary	INT,
title	VARCHAR(20)	NOT NULL DEFAULT 'engineer',
CONSTRAINT emp_deptno_fk FOREIGN KEY(deptno)
	REFERENCES department(deptno)
);

INSERT INTO dept
VALUES	(600, 'Public Relations', DEFAULT);

UPDATE dept
SET cityno = DEFAULT
WHERE deptno = 500;

INSERT INTO dept (deptno, dname)
VALUES	(700, 'Public Relations');

INSERT INTO emp1
VALUES		(1001, '孫悟空', '2013/11/10', 'gg@mail.com', 100, 56000, 'senior engineer');

INSERT INTO emp1
VALUES		(1002, '孫悟空', '2013/11/10', 'gg1@mail.com', 200, 56000, 'senior engineer');

INSERT INTO emp1
VALUES		(1003, '孫悟空', '2013/11/10', 'gg2@mail.com', 600, 56000, 'senior engineer');

DELETE FROM department WHERE deptno = 100;


ALTER TABLE `db01`.`emp1` 
DROP FOREIGN KEY `emp_deptno_fk`;
ALTER TABLE `db01`.`emp1` 
ADD CONSTRAINT `emp_deptno_fk`
  FOREIGN KEY (`deptno`)
  REFERENCES `db01`.`department` (`deptno`)
  ON UPDATE CASCADE;

update department set deptno = 201 where deptno = 200;
  
  
ALTER TABLE `db01`.`emp1` 
DROP FOREIGN KEY `emp_deptno_fk`;
ALTER TABLE `db01`.`emp1` 
ADD CONSTRAINT `emp_deptno_fk`
  FOREIGN KEY (`deptno`)
  REFERENCES `db01`.`department` (`deptno`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
  
delete from department where deptno = 201;

CREATE TABLE mem(
	memno   int	PRIMARY KEY AUTO_INCREMENT,
    mname	varchar(30) NOT NULL
);

INSERT INTO mem (mname) VALUES ('David Ho'),
	('Maria Wang'),('Pam Pan'),('Tina Lee'),('Jean Tsao');

SELECT LAST_INSERT_ID();

CREATE TABLE mem(
	memno	INT	PRIMARY KEY AUTO_INCREMENT,
    mname	VARCHAR(30)	NOT NULL
)AUTO_INCREMENT = 100;

INSERT INTO mem (mname) VALUES ('David Ho'),
	('Maria Wang'),('Pam Pan'),('Tina Lee'),('Jean Tsao');
    
