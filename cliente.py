class Cliente:
    def __init__(self, nome, sobrenome, endereco, telefone, email, genero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero
    
    def __str__(self):
        return "Clientenome= {}, sobrenome= {}, endereço= {}, telefone= {}, e-mail= {}, gênero={}".format(
            self.nome, self.sobrenome, self.endereco, self.telefone, self.email, self.genero
    )