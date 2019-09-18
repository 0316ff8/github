# 連接MySQL資料庫

import mysql.connector
conn = mysql.connector.connect(database = 'db01',  user = 'root',  password = 'tibame')
conn.close()

from mysql.connector import connection
conn = connection.MySQLConnection(database = 'db01',  user = 'root',  password = 'tibame')
conn.close()


import mysql.connector
config = {
    'database':'db01',
    'user':'root',
    'password':'tibame'
}
conn = mysql.connector.connect(**config)
conn.close()