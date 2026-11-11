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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    data_hora TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES  produto (id)
    )
""")

conexao.commit()
conexao.close()