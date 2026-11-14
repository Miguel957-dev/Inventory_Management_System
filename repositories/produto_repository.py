import sqlite3
from models.movimentçao import *
from models.produto import *

class Historico:
    def __init__(self, db_path="estoque.db"):
        self.db_path = db_path

    def _executar_busca_em_lotes(self, comando_do_sql_parametro, parametros=()):
        
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        comando_sql = comando_do_sql_parametro
        cursor.execute(comando_sql, parametros)
        try:

            while True:
                quanti = cursor.fetchmany(50)

                if not quanti:
                    break
                for linha in quanti:
                    yield Movimentaçao (* linha)

        finally:
            conexao.close()

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
       
        comando_sql = "SELECT id, produto_id, quantidade, tipo, data_hora FROM movimentacoes ORDER BY data_hora DESC"
        yield from self._executar_busca_em_lotes(comando_sql)

    def buscar_por_produto(self, id_produto):
        
        comando_sql = "SELECT id, produto_id, quantidade, tipo, data_hora FROM movimentacoes WHERE produto_id = ? ORDER BY data_hora DESC"
        yield from self._executar_busca_em_lotes(comando_sql, (id_produto,))
        
    def buscar_entrada(self):

        comando_sql = "SELECT id, produto_id, quantidade, tipo, data_hora FROM movimentacoes WHERE tipo = 'ENTRADA' ORDER BY data_hora  DESC"
        yield from self._executar_busca_em_lotes(comando_sql)

    def buscar_saida(self):
        comando_sql = "SELECT id, produto_id, quantidade, tipo, data_hora FROM movimentacoes WHERE tipo = 'SAIDA' ORDER BY data_hora  DESC"
        yield from self._executar_busca_em_lotes(comando_sql)
