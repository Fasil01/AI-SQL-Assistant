import sqlite3

conn = sqlite3.connect("sample.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    signup_date DATE
)
''')

cur.execute("INSERT INTO users (name, email, signup_date) VALUES ('Alice', 'alice@example.com', '2025-08-01')")
cur.execute("INSERT INTO users (name, email, signup_date) VALUES ('Bob', 'bob@example.com', '2025-08-04')")
cur.execute("INSERT INTO users (name, email, signup_date) VALUES ('Charlie', 'charlie@example.com', '2025-08-07')")

conn.commit()
conn.close()

