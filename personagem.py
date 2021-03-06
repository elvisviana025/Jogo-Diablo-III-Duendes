from random import randint
from time import sleep


class Personagem():
    def __init__(self, nome, vantagem, forca, inteligencia, agilidade, magia, companheiro):
        self._nome = nome
        self._vantagem = vantagem
        self._forca = forca
        self._inteligencia = inteligencia
        self._agilidade = agilidade
        self._magia = magia
        self._ultima_escolha = ''
        self._sequencia = 0
        self._duendes_capturados = 0
        self._inimigos_destruidos = 0
        self._companheiros = [companheiro]

    @property
    def nome(self):
        return self._nome
    @property
    def vantagem(self):
        return self._vantagem
    @property
    def forca(self):
        return self._forca
    @property
    def inteligencia(self):
        return self._inteligencia
    @property
    def agilidade(self):
        return self._agilidade
    @property
    def magia(self):
        return self._magia
    @property
    def ultima_escolha(self):
        return self._ultima_escolha
    @property
    def sequencia(self):
        return self._sequencia
    @property
    def duendes_capturados(self):
        return self._duendes_capturados
    @property
    def inimigos_destruidos(self):
        return self._inimigos_destruidos
    @property
    def companheiros(self):
        return self._companheiros

    @forca.setter
    def forca(self, ponto):
        self._forca = ponto
    @inteligencia.setter
    def inteligencia(self, ponto):
        self._inteligencia = ponto
    @agilidade.setter
    def agilidade(self, ponto):
        self._agilidade = ponto
    @magia.setter
    def magia(self, ponto):
        self._magia = ponto
    @sequencia.setter
    def sequencia(self, vitoria):
        self._sequencia = vitoria
    @ultima_escolha.setter
    def ultima_escolha(self, acao_escolhida):
        self._ultima_escolha = acao_escolhida
    @duendes_capturados.setter
    def duendes_capturados(self, duende_capturado):
        self._duendes_capturados = duende_capturado
    @inimigos_destruidos.setter
    def inimigos_destruidos(self, inimigo_destruido):
        self._inimigos_destruidos = inimigo_destruido


    def __str__(self):
        return f'??? {self._nome.title()} ' \
               f'| [1] For??a: {self._forca} ' \
               f'| [2] Intelig??ncia: {self._inteligencia} ' \
               f'| [3] Agilidade: {self._agilidade} ' \
               f'| [4] Magia: {self._magia} '

    def imprimir_classe_formatada(self):
        print( f'{self._nome.title():10} '
               # f'| Vantagem: {self._vantagem.title():12} '
               f'| [1] For??a: {self._forca} '
               f'| [2] Intelig??ncia: {self._inteligencia} '
               f'| [3] Agilidade: {self._agilidade} '
               f'| [4] Magia: {self._magia} ')

    def escolher_acao(self):
        escolhaAgir = ''
        agir = int(input('Escolha como agir:\n[1] For??a [2] Intelig??ncia [3] Agilidade [4] Magia\n ??? '))
        if agir == 1:
            escolhaAgir = "for??a"
        elif agir == 2:
            escolhaAgir = "intelig??ncia"
        elif agir == 3:
            escolhaAgir = "agilidade"
        elif agir == 4:
            escolhaAgir = "magia"
        return escolhaAgir

    def jogar_dado(self):
        input('Jogue o dado de 1 a 6 [ENTER]: ')
        dado = randint(1, 6)
        print(f'??? Pontos de dado = {dado}')
        return dado

    def imprimir_companheiros(self):
        if len(self.companheiros) > 0:
            sleep(1)
            print(f'??? Seus companheiros: ', end='')
            for companheiro in self.companheiros:
                if self.companheiros.index(companheiro) == (len(self.companheiros) - 1):
                    print(f'{companheiro}', end='')
                else:
                    print(f'{companheiro}, ', end='')
            print('.')

    def companheiro_sacrificar(self, resultado_final):
        if (resultado_final == 'derrota' or resultado_final == 'derrota_destrui????o') and len(self.companheiros) > 0:
            # sacrificar companheiro
            companheiro = self.companheiros[0]
            print(f'??? Seu companheiro(a) {companheiro} distraiu o inimigo para voc?? continuar.')
            sleep(1)
            self.companheiros.pop(0)

            # remover vantagem do companheiro
            if companheiro == 'Javali Furioso':
                self.forca -= 1
            elif companheiro == 'Aranha Estrategista':
                self.inteligencia -= 1
            elif companheiro == 'Morcego Veloz':
                self.agilidade -= 1
            elif companheiro == 'Galinha Feiticeira':
                self.magia -= 1

            return 'vit??ria'
        else:
            return resultado_final

    def imprimir_estado_do_personagem(self):
        print(self)
        self.imprimir_companheiros()