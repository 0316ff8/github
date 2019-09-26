SELECT * FROM employee;-- 查詢employee表格所有欄位資料
SELECT ename, salary, deptno FROM employee;-- 查詢employee表格內的ename, salary, deptno欄位

SELECT 17/4, 17 div 4, 17%4, 17*null;-- 算術運算子範例 / 算出有小數位答案, div算出商, %算出餘數, *運算元為null算出結果一樣為null

SELECT ename AS '員工姓名', salary*12 AS '年薪' FROM employee;-- 查詢ename欄位顯示別名為員工姓名、計算salary欄位*12個月顯示別名為年薪
SELECT ename AS 'Empolyee Name', salary*12 AS 'Annual Salary' FROM employee;-- 用英文別名有特殊字元或空格一定要有單引號
SELECT ename 'Empolyee Name', salary*12 'Annual Salary' FROM employee;-- AS可寫可不寫

SELECT SUBSTRING(ename, 1, 1) '姓名' FROM employee;-- 從employee表格從ename的第一個字擷取一個字(姓)
SELECT SUBSTRING(ename, 2) '姓名' FROM employee;-- 從employee表格擷取從第二個字到後面所有的字(名子)
SELECT SUBSTRING('David Wang', 1, 5) 'substring';-- 擷取David Wang字串從第一個字開始往右邊數五個字
SELECT SUBSTRING('David Wang', 7, 4) 'substring';-- 擷取David Wang字串從第七個字開始往右數四個字
SELECT SUBSTRING('David Wang', 7) 'substring';-- 擷取David Wang字串從第七個字開始到最後
SELECT SUBSTRING('David Wang', -4) 'substring';-- 擷取David Wang字串從右邊數過來第四個字開始往右數到最後
SELECT SUBSTRING('David Wang', -4, 2) 'substring';-- 擷取David Wang字串從右邊數過來第四個字開始往右數兩個字

SELECT CONCAT(ename, ' is a ',title) '員工' FROM employee;-- 從employee表格將'員工姓名 is a 職稱'串接
SELECT LENGTH('我是一個student') 'length';-- 計算字串長度佔多少Bytes, utf8字元集一個中文佔3 Bytes
SELECT CHAR_LENGTH('我是一個student') 'character';-- 計算字串總共佔多少字元

SELECT SYSDATE() + interval 5 day;-- 查尋系統時間加5天結果
SELECT SYSDATE() + interval 20 minute;-- 查尋系統時間加20分鐘結果
SELECT SYSDATE() + interval 3 year;-- 查尋系統時間加3年結果
SELECT SYSDATE() - interval 5 hour;-- 查尋系統時間減5小時結果
SELECT hiredate '到職日', hiredate + interval 3 month '試用期' FROM employee;-- 從empolyee查尋到職日與試用期過後時間

SELECT SYSDATE(), SLEEP(2), SYSDATE();-- 傳回正在執行的日期時間,測試等兩秒後系統時間會多數兩秒
SELECT NOW(), SLEEP(2), NOW();-- 傳回正在執行的日期時間,測試等兩秒後系統時間會不變,第二次就不在抓取時間

SELECT ADDDATE(SYSDATE(), interval 5 day);-- 查詢系統時間加5天
SELECT ADDDATE(SYSDATE(), interval 20 minute);-- 查詢系統時間加20分鐘
SELECT SUBDATE(SYSDATE(), interval 5 year);-- 查詢系統時間減5年
SELECT SUBDATE(SYSDATE(), interval 3 month);-- 查詢系統時間減3個月

-- 從employee表格查詢員工編號, 員工姓名, 到職日期, 並將到職日期分為年月日顯示
SELECT empno, ename, hiredate, YEAR(hiredate) 'year', MONTH(hiredate) 'month', DAY(hiredate) 'day' FROM employee;
SELECT NOW(), YEAR(NOW()) 'year', MONTH(NOW()) 'month', DAY(NOW()) 'day';-- 查詢現在時間, 以年月日顯示

SELECT empno, ename, hiredate, -- 查詢員工編號, 員工姓名, 到職日期
		DATEDIFF(NOW(), hiredate) div 365 'year',-- 查詢到職多少年(商)
        DATEDIFF(NOW(), hiredate) % 365 'day',-- 查詢扣除到職年份後剩下多少日(餘數)
        (DATEDIFF(NOW(), hiredate) % 365) div 30 'month',-- 查詢到職多少月(商)
        DATEDIFF(NOW(), hiredate) / 365 'year',-- 查詢到職多少年(商算到整除)
        round(DATEDIFF(NOW(), hiredate) / 365) 'year',-- 四捨五入查詢到的到職年
        round(DATEDIFF(NOW(), hiredate) / 365,1) 'year'-- 四捨五入查詢到的到職年到小數第一位
        FROM employee;
        
SELECT empno, ename, salary,-- 查詢工號,名子,薪資
	salary *IF(salary >= 50000, 2, 1.5) 'bonus'-- 如果薪資大於等於50000, 薪資x2, 反之x1.5
FROM employee;

SELECT empno, ename, salary,-- 查詢工號,名子,薪資
	CASE
	  WHEN salary > 100000 THEN 'A'-- 當薪資大於100000為A
      WHEN salary BETWEEN 70000 AND 100000 THEN 'B'-- 當薪資大於等於70000到100000之間為B
	  WHEN salary BETWEEN 50000 AND 69999 THEN 'C'-- 當薪資大於等於50000到69999之間為C
      WHEN salary BETWEEN 30000 AND 49999 THEN 'D'-- 當薪資大於等於30000到49999之間為D
      ELSE 'E'-- 其他為E
	END 'Grade'-- 別名
FROM employee;

SELECT DISTINCT deptno FROM employee;-- 查詢 employee 表格 deptno 欄位並將重複資料刪除
SELECT DISTINCT deptno, title FROM employee;-- 查詢 employee 表格 deptno, title 欄位並將重複資料刪除
SELECT * FROM employee WHERE deptno = 100;-- 查詢 employee 表格所有欄位, 條件為 deptno = 100
SELECT * FROM employee WHERE title = 'engineer';-- 查詢 employee 表格所有欄位, 條件為 title = 'engineer'
SELECT * FROM employee WHERE hiredate = '2007/07/06';-- 查詢 employee 表格所有欄位, 條件為 hiredate = '2007/07/06'
SELECT * FROM employee WHERE salary >= 50000;-- 查詢 employee 表格所有欄位, 條件為 salary 欄位>= 50000
SELECT * FROM employee WHERE salary BETWEEN 30000 AND 50000;-- 查詢 employee 表格所有欄位, 條件為 salary 欄位介於30000到50000
SELECT * FROM employee WHERE title IN ('manager', 'engineer');-- 查詢 employee 表格所有欄位, 條件為 title 欄位為有manager與engineer
SELECT * FROM department WHERE mgrno IS NULL;-- 查詢 department 表格所有欄位, 條件為mgrno欄位為NULL值

SELECT * FROM employee WHERE ename LIKE '林%';-- 查詢 employee 表格所有欄位, 條件為 ename 為林開頭的名子
SELECT * FROM employee WHERE ename LIKE '%生';-- 查詢 employee 表格所有欄位, 條件為 ename 為生結尾的名子
SELECT * FROM employee WHERE ename LIKE '%麗%';-- 查詢 employee 表格所有欄位, 條件為 ename 為有麗字眼的名子
SELECT * FROM employee WHERE ename LIKE '_麗%';-- 查詢 employee 表格所有欄位, 條件為 ename 為第二個字為麗的名子
SELECT * FROM employee WHERE title LIKE 'SA%';-- 查詢 employee 表格所有欄位, 條件為 title 欄位為SA開頭
SELECT * FROM employee WHERE title LIKE 'SA_%';-- 查詢 employee 表格所有欄位, 條件為 title 欄位為SA後面至少一個字
SELECT * FROM employee WHERE title LIKE '%SA\_%';-- 查詢 employee 表格所有欄位, 條件為 title 欄位為SA_(\強制要有底線)
SELECT * FROM employee WHERE title LIKE '%SA#_%' ESCAPE '#';-- 查詢 employee 表格所有欄位, 條件為 title 欄位為%SA#_%(\改成#)

SELECT * FROM employee WHERE salary >= 45000 AND ename LIKE '林%';-- 查詢 employee 表格所有欄位, 條件為 salary >= 45000 與 ename 為林開頭
SELECT * FROM employee WHERE salary >= 45000 OR ename LIKE '林%';-- 查詢 employee 表格所有欄位, 條件為 salary >= 45000 或 ename 為林開頭
SELECT * FROM employee WHERE title LIKE 'manager' OR title LIKE 'engineer';-- 查詢 employee 表格所有欄位, 條件為 title 為 manager 或 engineer
SELECT * FROM employee WHERE salary >= 30000 AND salary <= 50000;-- 查詢 employee 表格所有欄位, 條件為 salary >= 30000 與 salary <= 50000

SELECT * FROM employee WHERE title NOT IN ('manager', 'engineer');-- 查詢 employee 表格所有欄位, 條件為 title 不是 manager 或 engineer
SELECT * FROM department WHERE mgrno IS NOT NULL;-- 查詢 department 表格所有欄位, 條件為 mgrno 不是 NULL值
SELECT * FROM employee WHERE salary NOT BETWEEN 30000 AND 50000;-- 查詢 employee 表格所有欄位, 條件為 salary 不介於 30000 到 50000
SELECT * FROM employee WHERE ename NOT LIKE '林%';-- 查詢 employee 表格所有欄位, 條件為 ename 不是林開頭的名子

SELECT * FROM employee  ORDER BY hiredate DESC;-- 查詢 employee 表格所有欄位, 用 hiredate 降冪來排序
SELECT * FROM employee  ORDER BY salary;-- 查詢 employee 表格所有欄位, 用 salary 升冪(預設)來排序
SELECT ename, deptno, salary FROM employee ORDER BY deptno, salary DESC;-- 查詢 employee 表格 ename, deptno, salary 欄位, 用 salary 降冪、deptno 升冪(預設)來排序
SELECT ename, deptno, salary FROM employee ORDER BY deptno DESC, salary DESC;-- 查詢 employee 表格 ename, deptno, salary 欄位, 用 deptno與salary 降冪排序
SELECT ename, salary*12 'Annual' FROM employee ORDER BY Annual;-- 查詢 employee 表格 ename, salary*12 欄位, 用別名 Annual 升冪(預設)來排序
SELECT ename, salary*12 'Annual' FROM employee ORDER BY salary*12;-- 查詢 employee 表格 ename, salary*12 欄位, 用運算式 salary*12 升冪(預設)來排序, 不建議!!
SELECT ename, deptno, salary FROM employee ORDER BY 3;-- 查詢 employee 表格 ename, deptno, salary 欄位, 用欄位編號3來升冪(預設)排序
SELECT * FROM employee  ORDER BY 3;-- 查詢 employee 表格所有欄位, 用欄位編號3來升冪(預設)排序
SELECT * FROM employee  LIMIT 3;-- 查詢 employee 表格所有欄位, 只取前3筆資料
SELECT * FROM employee  LIMIT 4, 3;-- 查詢 employee 表格所有欄位, 跳過前4筆後取3筆資料
SELECT * FROM employee  ORDER BY hiredate LIMIT 3;-- 查詢 employee 表格所有欄位, 用 hiredate 欄位升冪(預設)排序只取前3筆資料
SELECT * FROM employee  ORDER BY salary DESC LIMIT 3;-- 查詢 employee 表格所有欄位, 用 salary 欄位降冪排序取前3筆資料

SELECT SUM(salary), AVG(salary), MAX(salary), MIN(salary) FROM employee;-- 查詢 employee 表格薪資的總和,平均,最大及最小值
SELECT COUNT(*) FROM employee;
SELECT COUNT(ename) FROM employee;
SELECT COUNT(deptno) FROM employee;
SELECT COUNT(distinct deptno) FROM employee;-- 計算出公司部門數
SELECT COUNT(mgrno) 'Count' FROM department;-- 計算出主管的部門數

SELECT deptno, COUNT(*), SUM(salary), AVG(salary), MAX(salary), MIN(salary) 
FROM employee
GROUP BY deptno;-- 計算出各部門的人數,薪資總和、平均、最高及最低薪資

SELECT deptno, COUNT(*), SUM(salary), AVG(salary), MAX(salary), MIN(salary) 
FROM employee
GROUP BY deptno
ORDER BY AVG(salary);-- 計算出各部門的人數、薪資總和、平均薪資(升冪排序)、最高及最低薪資

SELECT deptno, title, SUM(salary) 'Total' FROM employee
GROUP BY deptno, title;-- 計算出不同部門不同職稱的薪資總和

SELECT deptno, title, SUM(salary) 'Total' FROM employee
GROUP BY deptno, title WITH ROLLUP;-- 計算出不同部門不同職稱的薪資總和，每一群組多一列統計資料(小計、總計)

-- 找出不同職稱的總薪資，但不包含有'SA'這些字的職稱，且總薪資必須超過100000，最後結果並以總薪資排序
SELECT title, SUM(salary) 'Total'-- 查詢 title 與 SUM(salary)別名Total
FROM employee
WHERE title NOT LIKE '%SA%'-- 篩選 title 不是SA這些字
GROUP BY title
HAVING SUM(salary) > 100000 -- 總薪資大於 100000
ORDER BY SUM(salary) DESC;-- 總薪資按由大到小排列


