import psycopg2

DSN = {
    'host': 'localhost',
    'database': 'posts_db',
    'user': 'postgres',
    'password': 'outback15'
}

conn = psycopg2.connect("host='localhost' dbname='posts_db' user='postgres' password='outback15'")

cur = conn.cursor()
cur.execute('SELECT * from posts')
print(cur.fetchone())

cur.close()
conn.close()
