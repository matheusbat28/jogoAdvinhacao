from telas.cadastro.cadastro import *
from util.geradorUtil import *
from entidade.jogador import Jogador
from dao.jogador.jogadorDao import JogadorDao
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QLineEdit


class Cadastro(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.jogadorDao = JogadorDao()
        self.btCriar.clicked.connect(self.cadastrar)
        self.btLimpar.clicked.connect(self.limpar)
        self.varSenha.setEchoMode(QLineEdit.Password)
        self.varSenhaNV.setEchoMode(QLineEdit.Password)

    def cadastrar(self):
        nome = self.varNme.text().strip()
        usuiario = self.varUsuario.text().strip()
        senha = self.varSenha.text().strip()
        senhaNV = self.varSenhaNV.text().strip()

        if not varificarStr(nome):
            QMessageBox.critical(self, 'ops erro!!', 'nome icorreto')
        elif not varificarStr(usuiario):
            QMessageBox.critical(self, 'ops erro!!', 'usuario incorreto')
        elif not varificarStr(senha):
            QMessageBox.critical(self, 'ops erro!!', 'senha incorreto')
        elif not varificarStr(senhaNV):
            QMessageBox.critical(self, 'ops erro!!', 'senha novamente incorreto')
        elif not senha == senhaNV:
            QMessageBox.critical(self, 'ops erro!!', 'as senhas não são iguais')
        else:
            jogador = Jogador(nome, usuiario, senha)
            self.jogadorDao.salvar(jogador)
            self.close()

    def limpar(self):
        self.varNme.clear()
        self.varUsuario.clear()
        self.varSenha.clear()
        self.varSenhaNV.clear()
