import psycopg2

conn = psycopg2.connect("host='localhost' dbname='python_etl' user='postgres' password='root'")
cur = conn.cursor()

cur.execute('DROP TABLE sample_table;')

conn.commit()
cur.close()
conn.close()
