CREATE TABLE employee(
	empno		decimal(4)		PRIMARY KEY,
    ename		varchar(30)		NOT NULL,
    hiredate	date			NOT NULL,
    salary		int				NOT NULL,
    deptno		decimal(3)		NOT NULL,
    title		varchar(20)		NOT NULL
);

CREATE TABLE `db01`.`department` (
  `deptno` DECIMAL(3) NOT NULL,
  `dname` VARCHAR(30) NOT NULL,
  `mgrno` DECIMAL(4) NULL,
  PRIMARY KEY (`deptno`));

SHOW TABLE STATUS IN db01;-- 顯示所有表格狀態
SHOW TABLES;-- 顯示表格
DESC employee;-- 查看當初設計的表格欄位

DESC gg;-- 查看當初設計的表格欄位
CREATE TABLE CC(a decimal(10),b char(30),c int);-- 創建CC資料表相關欄位
ALTER TABLE CC ADD d varchar(30);-- 新增d欄位定義為varchar(30)
ALTER TABLE CC MODIFY d char(10);-- 定義d欄位為char(10)
ALTER TABLE CC CHANGE d e decimal(8,2);-- 更改d欄位名稱為e decimal(8,2)
ALTER TABLE CC DROP c;-- 刪除欄位c
ALTER TABLE CC RENAME GG;-- 修改表格名稱CC為GG
ALTER TABLE gg ADD f int FIRST;-- 新增f欄位在定義為int在第一欄
ALTER TABLE gg ADD g char(50) AFTER b;-- 新增g欄位定義為char(50)在b欄位後面
DROP TABLE gg;-- 刪除表格gg

CREATE TABLE emp LIKE employee;-- 複製表格employee結構到新表格emp