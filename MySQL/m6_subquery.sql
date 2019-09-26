-- 找出所有薪資比'潘麗珍'高的員工
SELECT ename, salary
FROM employee
WHERE salary > (SELECT salary
				FROM employee
                WHERE ename = '潘麗珍');

-- 找出所有職稱和員工編號為1002相同且薪資比員工編號為1005高的員工                
SELECT ename, title, salary
FROM employee
WHERE title = (SELECT title
               FROM employee
			   WHERE empno = 1002)
AND   salary > (SELECT salary
				FROM employee
                WHERE empno = 1005);
 
-- 122找出
SELECT deptno, MIN(salary) 'Minimum Salary'
FROM employee
GROUP BY deptno
HAVING MIN(salary) > (SELECT MIN(salary)
					  FROM employee
                      WHERE deptno = 200);

-- 123
SELECT ename, title, salary,
	   ROUND(salary * 100 / 
			(SELECT SUM(salary)
             FROM employee
             WHERE deptno = 100),1) 'Percentage'
FROM employee
WHERE deptno = 100;

-- 124
SELECT ename, title, salary,
	   ROUND(salary * 100 / t.total, 1) 'Percentage'
FROM   employee, (SELECT SUM(salary) 'total'
                  FROM employee
                  WHERE deptno = 100) t
WHERE deptno = 100;

SELECT ename, title, salary,
	   ROUND(salary * 100 / t.total, 1) 'Percentage'
FROM   employee, (SELECT deptno d, SUM(salary) 'total'
                  FROM employee
                  WHERE deptno = 100) t
WHERE deptno = t.d;

-- 
SELECT ROUND(123456.789) 'num';
SELECT ROUND(123456.789, 1) 'num';
SELECT ROUND(123456.789, 2) 'num';
SELECT ROUND(123456.789, -1) 'num';
SELECT ROUND(123456.789, -2) 'num';
SELECT ROUND(123456.789, -3) 'num';

-- Error Code: 1242. Subquery returns more than 1 row
SELECT empno, ename
FROM employee
WHERE salary = (SELECT MIN(salary)
				FROM employee
                GROUP BY deptno);
                
-- 128                
SELECT ename, title, salary
FROM employee
WHERE salary < ANY
         (SELECT salary
          FROM employee
          WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

SELECT ename, title, salary
FROM employee
WHERE salary < (SELECT MAX(salary)
                   FROM employee
                   WHERE title = 'senior engineer')
AND   title <> 'senior engineer';


SELECT ename, title, salary
FROM employee
WHERE salary > ANY
         (SELECT salary
          FROM employee
          WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

SELECT ename, title, salary
FROM employee
WHERE salary > (SELECT MIN(salary)
                   FROM employee
                   WHERE title = 'senior engineer')
AND   title <> 'senior engineer';


SELECT ename, title, salary
FROM employee
WHERE salary < ALL
         (SELECT salary
          FROM employee
          WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

SELECT ename, title, salary
FROM employee
WHERE salary < (SELECT MIN(salary)
                   FROM employee
                   WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

SELECT ename, title, salary
FROM employee
WHERE salary > ALL
         (SELECT salary
          FROM employee
          WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

SELECT ename, title, salary
FROM employee
WHERE salary > (SELECT MAX(salary)
                   FROM employee
                   WHERE title = 'senior engineer')
AND   title <> 'senior engineer';

-- 130找出所有是主管的員工
SELECT ename
FROM emp
WHERE empno IN
			(SELECT DISTINCT mgrno
            FROM emp);
         
-- 131找出所有不是主管的員工          
SELECT ename
FROM emp
WHERE empno NOT IN
			(SELECT DISTINCT mgrno
            FROM emp
            WHERE mgrno IS NOT NULL);
            
-- 132            
SELECT e.ename, e.title, e.salary,
	   ROUND(salary * 100 / 
			(SELECT SUM(salary)
             FROM employee
             WHERE deptno = e.deptno),1) 'Percentage'
FROM employee e
WHERE deptno = 100;

-- 133
SELECT ename, salary, deptno
FROM employee e
WHERE salary IN
		  (SELECT MIN(salary)
          FROM employee
          GROUP BY deptno
          HAVING deptno = e.deptno);

-- 134          
SELECT ename, salary, deptno
FROM employee e
WHERE salary =
		  (SELECT MIN(salary)
          FROM employee
          WHERE deptno = e.deptno);

-- 136          
CREATE TABLE emp100 AS
	SELECT empno, ename, salary*12 'annualSalary', hiredate
    FROM employee
    WHERE deptno = 100;
