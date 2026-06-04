import sqlite3

from config import DATABASE_NAME
from logger import logger

conn = sqlite3.connect(DATABASE_NAME)

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

logger.info("Database Connected")


def add_expense(name, category, amount):

    cursor.execute("""
    INSERT INTO expenses
    (name, category, amount)
    VALUES (?, ?, ?)
    """, (name, category, amount))

    conn.commit()

    logger.info(
        f"Expense Added | {name} | {category} | {amount}"
    )


def view_expenses():

    cursor.execute("""
    SELECT *
    FROM expenses
    """)

    expenses = cursor.fetchall()

    logger.info(
        "Viewed Expenses"
    )

    return expenses


def delete_expense(expense_id):

    cursor.execute("""
    DELETE FROM expenses
    WHERE id = ?
    """, (expense_id,))

    conn.commit()

    logger.info(
        f"Deleted Expense ID {expense_id}"
    )


def update_expense(expense_id, amount):

    cursor.execute("""
    UPDATE expenses
    SET amount = ?
    WHERE id = ?
    """, (amount, expense_id))

    conn.commit()

    logger.info(
        f"Updated Expense ID {expense_id}"
    )


def close_connection():

    conn.close()

    logger.info(
        "Database Connection Closed"
    )