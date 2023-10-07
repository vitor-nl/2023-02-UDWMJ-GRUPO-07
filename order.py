class order:
    def __init__(self, preco_total, status, cliente):
        self.total_price = preco_total
        self.status = status
        self.client = cliente   

    def __str__(self):
        return "order(preco_total= '{}', status = '{}', cliente = '{}')".format(
            self.preco_total, self.status, self.cliente 
        )      