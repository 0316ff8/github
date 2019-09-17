import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'tibame')
    cursor = conn.cursor()
    query = "SELECT ename, hiredate, salary FROM employee"
    cursor.execute(query)
    emps = cursor.fetchall()

    for emp in emps:
        print('name={}, hiredate={}, salary{}'.format(emp[0], emp[1], emp[2]))
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