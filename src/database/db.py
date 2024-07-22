import sqlite3

def get_db_connection():
    connection = sqlite3.connect('tetris_game.db')
    return connection

def initialize_db():
    connection = sqlite3.connect('tetris_game.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT,
            score INTEGER
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

def save_score(nickname, score):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO scores (nickname, score) VALUES (?, ?)', (nickname, score))
    connection.commit()
    cursor.close()
    connection.close()

def get_top_scores(limit=3):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT nickname, score FROM scores ORDER BY score DESC LIMIT ?', (limit,))
    top_scores = cursor.fetchall()
    cursor.close()
    connection.close()
    return top_scores