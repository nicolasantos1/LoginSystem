import sqlite3 

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name text NOT NULL,
    Email text NOT NULL, 
    User text NOT NULL,
    Password text NOT NULL
);
""")

print("Conectado ao banco de dados com sucesso!") 