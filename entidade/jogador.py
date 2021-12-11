class Jogador:
    def __init__(self, nome, usuario, senha, ponto=None):
        self.__id = None
        self.__nome = nome
        self.__usuario = usuario
        self.__senha = senha
        if ponto is None:
            self.__ponto = 1000
        else:
            self.__ponto = ponto

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def ponto(self):
        return self.__ponto

    @ponto.setter
    def ponto(self, ponto):
        self.__ponto = ponto

    def __str__(self):
        return f'id: {self.id}\nnome: {self.nome}\nusuario: {self.usuario}\nponto: {self.ponto}'

