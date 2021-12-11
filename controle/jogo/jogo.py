from PyQt5.QtWidgets import QMainWindow, QMessageBox
from telas.jogo.jogo import *
from random import randint


class Jogo(QMainWindow, Ui_MainWindow):
    def __init__(self, jogador, parent=None, ):
        super().__init__(parent, )
        super().setupUi(self)
        self.jogador = jogador
        self.lbNome.setText(jogador.nome)
        self.lbUsuario.setText(jogador.usuario)
        self.lbPonto.setText(jogador.ponto)
        self.tentativa = 3
        self.lbTentativa.setText(f'3')
        self.btJogaNovamente.clicked.connect(self.jogarNovamente)
        self.btEnvair.clicked.connect(self.jogabilidade)
        self.numeroCerto = randint(0, 100)
        print(self.numeroCerto)

    def jogabilidade(self):
        try:
            numero = int(self.varNumero.text().strip())
        except:
            QMessageBox.critical(self, 'ops!! erro', 'sou pode ser numero inteiro')
        finally:
            if numero is self.numeroCerto:
                self.tentativa = 3
                self.lbTentativa.setText(f'{self.tentativa}')
                self.lbResposta.setText('parabens vc acerto o numero')
                self.label_5.close()
                self.varNumero.close()
                self.btEnvair.close()
            elif self.tentativa == 0:
                self.lbResposta.setText('acabou suas tentativa')
                self.varNumero.close()
                self.btEnvair.close()
                self.label_5.close()
            else:
                self.tentativa -= 1
                self.lbTentativa.setText(f'{self.tentativa}')
                self.lbResposta.setText('vc errou o numero')
            self.varNumero.clear()

    def jogarNovamente(self):
        self.varNumero.show()
        self.btEnvair.show()
        self.label_5.show()
        self.tentativa = 3
        self.lbTentativa.setText(f'{self.tentativa}')
        self.lbResposta.clear()
        self.numeroCerto = randint(0, 100)
        print(self.numeroCerto)
        self.jogabilidade


