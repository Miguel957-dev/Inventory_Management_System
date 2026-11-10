import sqlite3

class Historico:
    def __init__(self, id_produto, id_movimentaçao, saida, entrada):
        self.id_produto = id_produto
        self.id_movimentaçao = id_movimentaçao
        self.saida = saida 
        self.entrada = entrada

    def salvar(self):
        self.id_movimentaçao

    def historico_movimentaçao(self):
        pass

    def buscar_por_produto(self,id_produto):
        pass