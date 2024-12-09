import sqlite3

def conn():
    conn = sqlite3.connect('keys.db')  # Jeśli plik nie istnieje, zostanie utworzony
    return conn

def add_key(key):
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS key (
            id INTEGER PRIMARY KEY,
            keyy TEXT
        )
    ''')
    con.commit()
    cursor.execute('''
    INSERT INTO key (keyy)
    VALUES (?)
    ''', (key,))
    con.commit()
    new_id = cursor.lastrowid
    con.close()
    return new_id

def fetch():
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS key (
            id INTEGER PRIMARY KEY,
            keyy TEXT
        )
    ''')
    con.commit()
    cursor.execute('SELECT * FROM key')
    fetch = cursor.fetchall()
    con.close()
    return fetch
    
def ret_text(indeks):
    con = conn()
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS key (
            id INTEGER PRIMARY KEY,
            keyy TEXT
        )
    ''')
    con.commit()
    cursor.execute('SELECT * FROM key')
    fetch = cursor.fetchall()
    con.close()
    return fetch[indeks][1]