use db01;

BEGIN;
SELECT salary
FROM   employee
WHERE empno = 1001;

UPDATE employee
SET salary = 60002
WHERE empno = 1001;

COMMIT;

SELECT salary
FROM   employee
WHERE empno = 1001;