from datetime import datetime 

class Movimentaçao:
    def __init__(self, id_movimentaçao, id_produto_movimentado, quantidade, tip_movimentaçao, data_hora):
        self.id_da_movimentaçao = id_movimentaçao
        self.id_do_produto_movimentado = id_produto_movimentado
        self.quantidade = quantidade
        self.tipo_movimentaçao = tip_movimentaçao

        self.data_hora = data_hora if data_hora else datetime.now()

    