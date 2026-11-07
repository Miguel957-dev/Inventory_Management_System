import sqlite3

conexao = sqlite3.connect("estoque.db")

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descriçao TEXT,
    preço REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    estoque_minimo INTEGER NOT NULL 
    )

""")

conexao.commit()
conexao.close()