import psycopg2
import json
from datetime import datetime
import time

with open('../data/2015-08-15.all-epl-games.json') as match_data_file:
    match_data = json.load(match_data_file)
match_data_file.close()

conn = psycopg2.connect("host='localhost' dbname='python_etl' user='postgres' password='root'")
cur = conn.cursor()

query = "INSERT INTO sample_table (id, match_time, status, home, score, link, away) VALUES (%s, %s, %s, %s, %s, %s, %s);"

for record in match_data:
    data = (record['id'], time.ctime(int(record['time'])), record['status'], record['home'], record['score'], record['link'], record['away'])
    cur.execute(query, data)

conn.commit()
cur.close()
conn.close()
