import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL
)
""")

conn.commit()


def add_expense(name, category, amount):
    cursor.execute("""
    INSERT INTO expenses
    (name, category, amount)
    VALUES (?, ?, ?)
    """, (name, category, amount))

    conn.commit()


def view_expenses():
    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    for expense in expenses:
        print(expense)


def close_connection():
    conn.close()