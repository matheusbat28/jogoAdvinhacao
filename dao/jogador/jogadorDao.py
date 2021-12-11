from dao.conexao import conecta
class JogadorDao:

    def salvar(self, jogador):
         with conecta() as conexao:
             with conexao.cursor() as cursor:
                 sql = 'INSERT INTO jogador (nome, usuario, senha, ponto) VALUES ' \
                       '(%s, %s, %s, %s)'
                 cursor.execute(sql, (jogador.nome,
                                      jogador.usuario,
                                      jogador.senha,
                                      jogador.ponto,))
                 conexao.commit()

    def posquisarPorNomeSenha(self, usuario, senha):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM jogador WHERE usuario LIKE %s and senha LIKE %s',
                               (f'%{usuario}%',
                                f'%{senha}%'))

                return cursor.fetchone()
