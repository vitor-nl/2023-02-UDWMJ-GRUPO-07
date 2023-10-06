from unicodedata import name


class produto:
    def __init__(self, nome, descrição, fabricação, ativo, categoria):
        self.nome = nome
        self.descrição = descrição
        self.fabricação = fabricação
        self.ativo = ativo
        self.categoria = categoria
    