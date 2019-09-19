import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'tibame')
    cursor = conn.cursor()
    query = ("SELECT ename, hiredate, salary FROM employee WHERE deptno = %(deptno)s AND title = %(title)s")
    deptno = 100
    title = 'engineer'
    cursor.execute(query, {'deptno':deptno, 'title':title})

    for ename, hiredate, salary in cursor:
        print('name={}, hiredate={}, salary{}'.format(ename, hiredate, salary))
    print('total', cursor.rowcount, "employees")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('user or password error')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't existed")
    else:
        print(err)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()