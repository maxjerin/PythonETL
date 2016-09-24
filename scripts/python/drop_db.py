import psycopg2

conn = psycopg2.connect("host='localhost' user='postgres' password='root'")
conn.autocommit = True

cur = conn.cursor()

cur.execute("DROP DATABASE python_etl")

cur.close()
conn.close()
