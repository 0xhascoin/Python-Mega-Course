import psycopg2

def connect():
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()

def add(id, title, author, year, isbn):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("INSERT INTO book VALUES (%s, %s, %s, %s, %s)", (id, title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()

    return rows


def search(title="", author="", year=0, isbn=0):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()

    return rows


def delete(title):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("DELETE FROM book WHERE title =%s", (title,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = psycopg2.connect("dbname='books' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()

    cur.execute("UPDATE book SET title =%s, author=%s, year=%s, isbn=%s  WHERE id=%s", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
# add(3, 'Book two', 'Author two', 2020, 122)
# delete('Book two')
update(1, 'New title', 'New author', 1990, 28319073)
print(view())
