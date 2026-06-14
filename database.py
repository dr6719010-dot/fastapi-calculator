import sqlite3
from datetime import datetime

DB_NAME = "calcx.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            operation   TEXT NOT NULL,
            result      REAL NOT NULL,
            created_at  TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_calculation(operation, result):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO calculations (operation, result, created_at)
        VALUES (?, ?, ?)
    """, (operation, str(result), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_history(limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT operation, result, created_at
        FROM calculations
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {"operation": row[0], "result": row[1], "created_at": row[2]}
        for row in rows
    ]