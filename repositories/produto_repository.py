import sqlite3
from models.movimentçao import *
from models.produto import *

class Historico:
    def __init__(self, db_path="estoque.db"):
        self.db_path = db_path

    def salvar(self, movimentaçao: Movimentaçao):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()
        
        dados_movimentaçao = ( 
                              movimentaçao.id_do_produto_movimentado, movimentaçao.quantidade, movimentaçao.tipo_movimentaçao, movimentaçao.data_hora)

        comando_sql = "INSERT INTO movimentacoes( produto_id, quantidade, tipo, data_hora) VALUES (?, ?, ?, ?)"
        
        cursor.execute(comando_sql, dados_movimentaçao)

        conexao.commit()
        conexao.close()

    def historico_movimentaçao(self):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = "SELECT id, produto_id, quantidade, tipo, data_hora FROM movimentacoes ORDER BY data_hora DESC"
        cursor.execute(comando_sql)
        try:

            while True:
                    quanti = cursor.fetchmany(50)

                    if not quanti:
                        break

                    for linha in quanti:
                        yield Movimentaçao(* linha)

        finally:
            conexao.close()

    def buscar_por_produto(self,id_produto):
        pass

    def buscar_entrada(self):
        pass

    def buscar_saida(self):
        pass

