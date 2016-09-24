import psycopg2

conn = psycopg2.connect("host='localhost' user='postgres' password='root'")
conn.autocommit = True
cur = conn.cursor()

cur.execute(
    """
        CREATE DATABASE python_etl
          WITH OWNER = postgres
           ENCODING = 'UTF8'
           TABLESPACE = pg_default
           LC_COLLATE = 'en_US.utf8'
           LC_CTYPE = 'en_US.utf8'
           CONNECTION LIMIT = -1;
""")

cur.close()
conn.close()
