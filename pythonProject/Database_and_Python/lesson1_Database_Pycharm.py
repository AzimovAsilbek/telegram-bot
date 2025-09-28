#Database execut python
import sqlite3

conn = sqlite3.connect("sample-database.db")
cur = conn.cursor()

cur.execute("""
SELECT * FROM employees LIMIT 5
""")

ans = cur.fetchall()
for i in ans:
    print(i)

cur.close()
conn.close()