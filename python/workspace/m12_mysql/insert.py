import mysql.connector
from mysql.connector import errorcode

cursor = None
conn = None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'tibame')
    cursor = conn.cursor()
    ins = "INSERT INTO employee VALUES(%s, %s, %s, %s, %s, %s)"
    ins_data = (1009, '張子仁', '2019/02/26', 48000, 100, 'engineer')
    cursor.execute(ins, ins_data)
    conn.commit()
    print('insert',cursor.rowcount, 'employees')

    query = "SELECT ename, hiredate, salary FROM employee"
    cursor.execute(query)
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