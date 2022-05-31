from random import randint
from time import sleep


class Inimigo():
    def __init__(self, lista_de_nomes, fraqueza, resistencia):
        self._lista_de_nomes = lista_de_nomes
        self._fraqueza = fraqueza
        self._resistencia = resistencia

    def __str__(self):
        return f'♦ {self._lista_de_nomes.title()} ' \
               f'| Fraqueza: {self._fraqueza.title()} ' \
               f'| Resistência: {self._resistencia.title()}'

    def retornar_nome(self, caminho):
        return self._lista_de_nomes[caminho].title()

    def retornar_informacoes(self, caminho):
        return f'♦ {self.retornar_nome(caminho)} ' \
               f'| Fraqueza: {self._fraqueza.title()} ' \
               f'| Resistência: {self._resistencia.title()}'

    @property
    def nome(self):
        return self._lista_de_nomes

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
            print(f'• Ponto modificador = + 1 de fraqueza do inimigo.')
            sleep(1)
        elif acao_escolhida == self.resistencia:
            ponto_modificador = -1
            print(f'• Ponto modificador = - 1 de resistência do inimigo.')
            sleep(1)
        return ponto_modificador

    def agir_na_derrota(self, personagem, resultado_final, caminho):
        atributos = ['força', 'inteligência', 'agilidade', 'magia']
        atributo_sorteado = atributos[randint(0, (len(atributos) - 1))]

        if self.retornar_nome(caminho) == 'Duende':
            if atributo_sorteado == 'força':
                personagem.forca += 1
            elif atributo_sorteado == 'inteligência':
                personagem.inteligencia += 1
            elif atributo_sorteado == 'agilidade':
                personagem.agilidade += 1
            elif atributo_sorteado == 'magia':
                personagem.magia += 1
            print(f'• O Duende deixou cair um "amuleto de {atributo_sorteado}": + 1 de {atributo_sorteado}.')
            sleep(1)

        elif self.retornar_nome(caminho) == 'Fantasma Ceifador':
            if resultado_final == "vitória_destruição":
                print(f'• Você evitou a maldição ao destruí-lo.')
                sleep(1)
            else:
                if atributo_sorteado == 'força':
                    personagem.forca -= 1
                elif atributo_sorteado == 'inteligência':
                    personagem.inteligencia -= 1
                elif atributo_sorteado == 'agilidade':
                    personagem.agilidade -= 1
                elif atributo_sorteado == 'magia':
                    personagem.magia -= 1
                print(f'• Ceifador jogou uma maldição: - 1 de {atributo_sorteado}.')
                sleep(1)


class Inimigo_Comum(Inimigo):
    def __init__(self, nome, fraqueza, resistencia):
        super().__init__(nome, fraqueza, resistencia)

class Inimigo_Chefe(Inimigo):
    def __init__(self, nome, fraqueza, resistencia, resistencia2):
        super().__init__(nome, fraqueza, resistencia)
        self._resistencia2 = resistencia2

    def __str__(self):
        return f'♦♦ {self._lista_de_nomes.title()} ' \
               f'| Fraqueza: {self._fraqueza.title()} ' \
               f'| Resistência: {self._resistencia.title()} ' \
               f'| Resistência 2: {self._resistencia2.title()}'

    def retornar_informacoes(self, caminho):
        return f'♦♦ {self.retornar_nome(caminho)} ' \
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
            print(f'• Ponto modificador = + 1 de fraqueza do inimigo.')
            sleep(1)
        elif acao_escolhida == self.resistencia:
            ponto_modificador = -1
            print(f'• Ponto modificador = - 1 de resistência do inimigo.')
            sleep(1)
        elif acao_escolhida == self.resistencia2:
            ponto_modificador = -1
            print(f'• Ponto modificador = - 1 de resistência do inimigo.')
            sleep(1)
        return ponto_modificador


