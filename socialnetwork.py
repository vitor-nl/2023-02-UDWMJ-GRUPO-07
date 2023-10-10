class socialnetwork:

    def __init__(self, cliente, network):
        self.cliente = cliente
        self.network = network

    def __str__(self):
        return "Social Cliente='{}', Network='{}'".format(self.cliente, self.network)