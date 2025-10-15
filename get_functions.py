import psycopg

conn = psycopg.connect("dbname=dataduck user=hofst password=postgres host=localhost")
cur = conn.cursor()

cur.execute("SELECT id, name FROM functions;")
rows = cur.fetchall()

for row in rows:
	print(row)

cur.close()
conn.close()
