class Produto():
    """Classe produto cria um produto com todas as suas caracteristicas necessaria para movimentação e organização do estoque."""
    def __init__(self,id , nome, descrição, preço, quantidade, estoque_min):
        self.id = id
        self.nome = nome
        self.descriçao = descrição
        self._preço = None
        self.quantidade = None
        self.estoque_minimo = estoque_min

        if preço <=0 or quantidade < 0 or estoque_min < 0:
            raise ValueError('O preço não pode ser zero ou menor que zero, a quantidade tem que ser maior que o estoque minimo e o estoque minimo tem que ser positivo!')
        else:
            self._preço = preço
            self.quantidade = quantidade
            self.estoque_minimo = self.estoque_minimo

    def __repr__(self):
        return f"Produto (id={self.id}, nome={self.nome}, descrição={self.descriçao}, preço={self.preço})"

    @property
    def preço(self):
        return f"O preço é {self._preço}"

    
    @preço.setter
    def mudar_preço(self, preço):
        if preço <= 0:
            raise ValueError('O preço tem que ser maior que zero!')

        else: 
            self._preço = preço

    def mudar_descrição(self, descriçao:str):
        self.descriçao = descriçao
        
    def mudar_quanti_mini(self, quantida_minima):
        self.estoque_minimo = quantida_minima