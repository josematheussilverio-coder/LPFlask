
class Contato:

    def __init__(self, nome, celular, email, data_nasc, id=None):
        self.nome = nome
        self.celular = celular
        self.email = email
        self.data_nasc = data_nasc
        self.id = id

    def __str__(self):
        return self.nome