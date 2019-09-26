-- CROSS JOIN
SELECT ename, dname FROM emp, dept;-- 兩個表格的所有列相乘，8x4=32
SELECT ename, dname FROM emp CROSS JOIN dept;-- ANSI Join Type

SELECT emp.ename, dept.deptno 
FROM emp, dept
WHERE emp.deptno = dept.deptno;

-- INNER JOIN - EQUAL JOIN
-- 找出所有員工的姓名`部門編號`部門名稱
SELECT ename, emp.deptno, dname 
FROM emp, dept
WHERE emp.deptno = dept.deptno;

SELECT ename, emp.deptno, dname 
FROM emp JOIN dept
ON emp.deptno = dept.deptno;-- ANSI Join Type

-- JOIN USING
-- 指定表格之同名欄位作為連結條件，USING()中的欄位，不可使用alias.column
SELECT ename, emp.deptno, dname 
FROM emp JOIN dept
USING (deptno);

-- NATURAL JOIN
-- 自動找兩個表格中名稱相同的欄位做連結條件，若沒相同欄位名稱，會產生CROSS JOIN的結果
SELECT ename, emp.deptno, dname 
FROM emp NATURAL JOIN dept;

-- 加入AND運算子增加JOIN的條件
-- 找出所有員工職稱為manager的姓名、部門編號和部門名稱
SELECT ename, emp.deptno, dname 
FROM emp, dept
WHERE emp.deptno = dept.deptno
AND title = 'manager';

SELECT ename, emp.deptno, dname 
FROM emp JOIN dept
ON emp.deptno = dept.deptno
WHERE title = 'manager';-- ANSI Join Type

-- 表格別名
SELECT e.ename, e.deptno, d.dname 
FROM emp e, dept d
WHERE e.deptno = d.deptno;

SELECT e.ename, e.deptno, d.dname 
FROM emp e JOIN dept d
ON e.deptno = d.deptno;-- ANSI Join Type

-- 三個表格 Equal join
-- JOIN N個表格必須最少需要N-1個JOIN的條件
-- 找出所有員工的姓名、部門名稱和城市名稱
SELECT e.ename, d.dname, c.cname 
FROM emp e, dept d, city c
WHERE e.deptno = d.deptno
AND d.cityno = c.cityno;

SELECT e.ename, d.dname, c.cname 
FROM emp e JOIN dept d
ON e.deptno = d.deptno
JOIN city c
ON d.cityno = c.cityno;-- ANSI Join Type

-- Non Equal join 
-- 不使用=運算子來設定JOIN條件
-- 找出所有員工的姓名、薪資和薪資等級
SELECT e.ename, e.salary, g.level 
FROM emp e, grade g
WHERE e.salary BETWEEN g.lowest AND g.highest;

-- 混和Equal join與Non Equal join
SELECT e.ename,d.dname, e.salary, g.level 
FROM emp e, dept d, grade g
WHERE e.deptno = d.deptno 
AND e.salary BETWEEN g.lowest AND g.highest;

-- Outer Join
-- 找出左邊沒顯示出來的資料
SELECT e.ename, e.deptno, d.dname 
FROM emp e LEFT JOIN dept d
ON e.deptno = d.deptno;

-- 找出右邊沒顯示出來的資料
SELECT e.ename, e.deptno, d.dname 
FROM emp e RIGHT JOIN dept d
ON e.deptno = d.deptno;

-- 找出左邊跟右邊沒顯示出來的資料
SELECT e.ename, e.deptno, d.dname 
FROM emp e LEFT JOIN dept d
ON e.deptno = d.deptno
UNION
SELECT e.ename, e.deptno, d.dname 
FROM emp e RIGHT JOIN dept d
ON e.deptno = d.deptno;

-- Self join 
-- 同一表格自己JOIN自己
-- 找出每個員工的主管是誰，沒有主管的員工部會表列出來
SELECT worker.ename 'worker ename', manager.ename 'manager ename'
FROM emp worker, emp manager -- 一定要有別名
WHERE worker.mgrno = manager.empno;-- 員工的主管代號等於主管的員工編號
