import psycopg2

conn = psycopg2.connect("host='localhost' dbname='python_etl' user='postgres' password='root'")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE public.sample_table
    (
      id integer NOT NULL,
      match_time timestamp without time zone,
      status text,
      home text,
      score text,
      link text,
      away text,
      CONSTRAINT sample_table_pkey PRIMARY KEY (id)
    )
    WITH (
      OIDS=FALSE
    );
    ALTER TABLE public.sample_table
      OWNER TO postgres;
""")

conn.commit()
cur.close()
conn.close()
