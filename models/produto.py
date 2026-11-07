from abc import abstractmethod

class Produto():
    def __init__(self,id , nome, descrição, preço, quantidade, estoque_min):
        self.id = id
        self.nome = nome
        self.descriçao = descrição
        self.preço = None
        self.quantidade = None
        self.estoque_minimo = None

        if preço <=0 or quantidade < 0 or estoque_min < 0:
            raise ValueError('O preço não pode ser zero ou menor que zero, a quantidade tem que ser maior que o estoque minimo e o estoque minimo tem que ser positivo!')
        else:
            self.preço = preço
            self.quantidade = quantidade
            self.estoque_minimo = self.estoque_minimo

    @property.getter
    def preço(self):
        print(self.preço)

    
    @property.setter
    def mudar_preço(self, preço):
        if preço <= 0:
            self.preço = preço

