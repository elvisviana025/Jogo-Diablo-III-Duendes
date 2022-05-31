from random import randint


class Personagem():
    def __init__(self, nome, vantagem, forca, inteligencia, agilidade, magia):
        self._nome = nome
        self._vantagem = vantagem
        self._forca = forca
        self._inteligencia = inteligencia
        self._agilidade = agilidade
        self._magia = magia
        self._ultima_escolha = ''
        self._sequencia = 0
        self._duendes_capturados = 0

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


    def __str__(self):
        return f'♣ {self._nome.title()} ' \
               f'| [1] Força: {self._forca} ' \
               f'| [2] Inteligência: {self._inteligencia} ' \
               f'| [3] Agilidade: {self._agilidade} ' \
               f'| [4] Magia: {self._magia} '

    def imprimir_classe_formatada(self):
        print( f'{self._nome.title():10} '
               f'| Vantagem: {self._vantagem.title():12} '
               f'| [1] Força: {self._forca} '
               f'| [2] Inteligência: {self._inteligencia} '
               f'| [3] Agilidade: {self._agilidade} '
               f'| [4] Magia: {self._magia} ')

    def escolher_acao(self):
        escolhaAgir = ''
        agir = int(input('Escolha como agir:\n[1] Força [2] Inteligência [3] Agilidade [4] Magia\n → '))
        if agir == 1:
            escolhaAgir = "força"
        elif agir == 2:
            escolhaAgir = "inteligência"
        elif agir == 3:
            escolhaAgir = "agilidade"
        elif agir == 4:
            escolhaAgir = "magia"
        return escolhaAgir

    def jogar_dado(self):
        input('Jogue o dado de 1 a 6 [ENTER]: ')
        dado = randint(1, 6)
        print(f'• Pontos de dado = {dado}')
        return dado