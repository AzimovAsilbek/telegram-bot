import sqlite3

conn = sqlite3.connect("p_transactions.db")
cursor = conn.cursor()

# Create accounts table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS accounts(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     balance REAL NOT NULL
# );
# """)
#
# # Create transactions table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS transactions(
#     id INTEGER PRIMARY KEY,
#     from_account_id INTEGER,
#     to_account_id INTEGER,
#     amount REAL NOT NULL,
#     FOREIGN KEY (from_account_id) REFERENCES accounts(id),
#     FOREIGN KEY (to_account_id) REFERENCES accounts(id)
# );
# """)
#
# # Insert data into accounts
# cursor.execute("""INSERT INTO accounts(name, balance) VALUES ('Ali Bob', 1000);""")
# cursor.execute("""INSERT INTO accounts(name, balance) VALUES ('Nena Kochhar', 5000);""")
# cursor.execute("""INSERT INTO accounts(name, balance) VALUES ('Potsan Ne Plachet', 5000);""")

try:
    cursor.execute("""BEGIN;""")
    cursor.execute(""" INSERT INTO transactions (from_account_id, to_account_id, amount) VALUES (2,3,2000);""")
    cursor.execute("""UPDATE accounts SET balance = balance - 2000 WHERE id=2;""")
    cursor.execute("""UPDATE accounts SET balance = balance + 2000 WHERE id=3;""")
    conn.commit()
except sqlite3.Error as error:
    print(f"xato chiqdi: {error}")

# Close the cursor and connection
cursor.close()
conn.close()
