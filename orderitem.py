class orderItem:

    def __init__(self, quantidade, preco_unitario):
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def __str__(self):
        return "Quantidade:'{}', Preço Unitario:'{}'".format(
            self.quantidade, self.preco_unitario
        )