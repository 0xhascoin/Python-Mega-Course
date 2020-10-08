import psycopg2

def connect():
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()

connect()

def add(title, author, year, isbn):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()