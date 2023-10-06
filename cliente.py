from select import select


class Cliente:
    def __init__(self, nome, sobrenome, endereco, telefone, email, genero):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero
        
