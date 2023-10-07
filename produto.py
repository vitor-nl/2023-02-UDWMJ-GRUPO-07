class produto:
    def __init__(self, nome, descrição, fabricação, ativo, categoria):
        self.nome = nome
        self.descrição = descrição
        self.fabricação = fabricação
        self.ativo = ativo
        self.categoria = categoria

    def __str__(self):
        return "Produto nome='{}', descrição='{}', fabricação='{}', ativo='{}' categoria='{}'".format(
        
        self.nome,
        self.descrição,
        self.fabricação,
        self.ativo,
        self.categoria,
    
        )
           
        
    