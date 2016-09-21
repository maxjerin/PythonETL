import MySQLdb
import settings

db1 = MySQLdb.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWORD)
cursor = db1.cursor()
sql = 'CREATE DATABASE python_etl'
cursor.execute(sql)
