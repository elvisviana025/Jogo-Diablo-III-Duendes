from random import randint


class Inimigo():
    def __init__(self, nome, fraqueza, resistencia):
        self._nome = nome
        self._fraqueza = fraqueza
        self._resistencia = resistencia

    def __str__(self):
        return f'Nome: {self._nome.title()} ' \
               f'| Fraqueza: {self._fraqueza.title()} ' \
               f'| Resistência: {self._resistencia.title()}'

    @property
    def nome(self):
        return self._nome

    @property
    def fraqueza(self):
        return self._fraqueza

    @property
    def resistencia(self):
        return self._resistencia

    def calcular_vantagem_desvantagem(self, acao_escolhida):
        ponto_modificador = 0
        if acao_escolhida == self.fraqueza:
            ponto_modificador = 1
        elif acao_escolhida == self.resistencia:
            ponto_modificador = -1
        return ponto_modificador

    def agir_na_derrota(self, personagem):
        atributos = ['força', 'inteligência', 'agilidade', 'magia']
        atributo_sorteado = atributos[randint(0, (len(atributos) - 1))]

        if self.nome == 'duende':
            if atributo_sorteado == 'força':
                print(f'amuleto de {atributo_sorteado}')
                personagem.forca += 1
            elif atributo_sorteado == 'inteligência':
                print(f'amuleto de {atributo_sorteado}')
                personagem.inteligencia += 1
            elif atributo_sorteado == 'agilidade':
                print(f'amuleto de {atributo_sorteado}')
                personagem.agilidade += 1
            elif atributo_sorteado == 'magia':
                print(f'amuleto de {atributo_sorteado}')
                personagem.magia += 1

        elif self.nome == 'fantasma ceifador':
            if atributo_sorteado == 'força':
                print(f'maldição de {atributo_sorteado}')
                personagem.forca -= 1
            elif atributo_sorteado == 'inteligência':
                print(f'maldição de {atributo_sorteado}')
                personagem.inteligencia -= 1
            elif atributo_sorteado == 'agilidade':
                print(f'maldição de {atributo_sorteado}')
                personagem.agilidade -= 1
            elif atributo_sorteado == 'magia':
                print(f'maldição de {atributo_sorteado}')
                personagem.magia -= 1


class Inimigo_Comum(Inimigo):
    def __init__(self, nome, fraqueza, resistencia):
        super().__init__(nome, fraqueza, resistencia)

class Inimigo_Chefe(Inimigo):
    def __init__(self, nome, fraqueza, resistencia, resistencia2):
        super().__init__(nome, fraqueza, resistencia)
        self._resistencia2 = resistencia2

    def __str__(self):
        return f'{self._nome.title()} ' \
               f'| Fraqueza: {self._fraqueza.title()} ' \
               f'| Resistência: {self._resistencia.title()} ' \
               f'| Resistência 2: {self._resistencia2.title()}'

    @property
    def resistencia2(self):
        return self._resistencia2

    def calcular_vantagem_desvantagem(self, acao_escolhida):
        ponto_modificador = 0
        if acao_escolhida == self.fraqueza:
            ponto_modificador = 1
        elif acao_escolhida == self.resistencia:
            ponto_modificador = -1
        elif acao_escolhida == self.resistencia2:
            ponto_modificador = -1
        return ponto_modificador

