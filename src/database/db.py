import sqlite3

def get_db_connection():
    conn = sqlite3.connect('tetris_game.db')
    return conn

def initialize_db():
    conn = sqlite3.connect('tetris_game.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def save_score(score):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
    conn.commit()
    cursor.close()
    conn.close()

def get_top_scores(limit=3):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    top_scores = cursor.fetchall()
    cursor.close()
    conn.close()
    return top_scores