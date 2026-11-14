from datetime import datetime 

class Movimentaçao:
    """Classe Movimentaçao define todos as caracteristicas que tem que ter uma movimentação para organização e gerenciamento de um estoque."""
    def __init__(self, id_movimentaçao:int | None, id_produto_movimentado:int, quantidade:float, tip_movimentaçao:str, data_hora=None):
        self.id_da_movimentaçao = id_movimentaçao
        self.id_do_produto_movimentado = id_produto_movimentado
        self.quantidade = quantidade
        self.tipo_movimentaçao = tip_movimentaçao

        self.data_hora = data_hora if data_hora else datetime.now()

    def __repr__(self):
        return f"Movimentação(id={self.id_da_movimentaçao}, tipo={self.tipo_movimentaçao}, quantidade={self.quantidade}, data e hora={self.data_hora})"