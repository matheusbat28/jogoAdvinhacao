import sys
from telas.login.login import *
from util.geradorUtil import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from controle.cadastro.cadastro import Cadastro
from dao.jogador.jogadorDao import JogadorDao
from controle.jogo.jogo import Jogo
from entidade.jogador import Jogador
from PyQt5.QtWidgets import QLineEdit


class Login(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.cadastro = Cadastro()
        self.jogadorDao = JogadorDao()
        self.jogo = None
        self.btEntrar.clicked.connect(self.varificarLogin)
        self.btCadastro.clicked.connect(self.entrarCadatro)
        self.varSenha.setEchoMode(QLineEdit.Password)

    def varificarLogin(self):
        usuario = self.varUsuario.text().strip()
        senha = self.varSenha.text().strip()
        pesquisaBanco = self.jogadorDao.posquisarPorNomeSenha(usuario, senha)

        if not varificarStr(usuario):
            QMessageBox.critical(self, 'ops erro!!', 'usuario incorreto')
        elif not varificarStr(senha):
            QMessageBox.critical(self, 'ops!! erro', 'senha incorreta')
        elif pesquisaBanco is None:
            QMessageBox.critical(self, 'ops!! erro', 'usuario não existe')
        else:
            jogador = Jogador(pesquisaBanco['nome'],
                              pesquisaBanco['usuario'],
                              pesquisaBanco['senha'],
                              pesquisaBanco['ponto'])
            jogador.id = pesquisaBanco['id']
            self.jogo = Jogo(jogador)
            self.jogo.show()
            self.close()


    def entrarCadatro(self):
        self.cadastro.show()


app = QApplication(sys.argv)
login = Login()
login.centralWidget()
login.show()
app.exec_()
