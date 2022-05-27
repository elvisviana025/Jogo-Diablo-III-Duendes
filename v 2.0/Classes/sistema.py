import lista_classes
import lista_inimigos


class Sistema():

    def __init__(self):
        pass

    def __espaco(self):
        print('-' * 40)

    def imprimir_titulo(self):
        self.__espaco()
        print(f'{"Diablo III : Caça aos Duendes":^40}')
        self.__espaco()

    def exibir_menu(self):
        while True: # MANTER COMENTADO PARA TESTE
            escolha = int(input('Menu:\n[1] Jogar [2] Regras [3] Classes [4] Sair\n → '))
            if escolha == 1:
                self.jogar()
            elif escolha == 2:
                self.__imprimir_regras()
            elif escolha == 3:
                self.__imprimir_classes()
            elif escolha == 4:
                break

    def __imprimir_regras(self):
        print('→ Objetivo: ache e capture o maior número de duendes.\n'
              '→ Você ganha a batalha se tiver 5 ou mais pontos de ataque.\n'
              '→ Você não pode repetir uma ação em duas batalhas seguidas.\n'
              '→ Fraquezas e resistências do inimigo: + 1 ou - 1 ponto de ataque.')
        self.__espaco()

    @staticmethod
    def __imprimir_classes():
        print(f'Lista de classes: ')
        for classe in lista_classes.lista_de_classes:
            classe.imprimir_classe_formatada()

    def escolher_classe(self):
        escolha = int(input('Escolha uma classe:\n[1] Guerreiro [2] Feiticeiro [3] Caçador [4] Monge\n → '))
        personagem = ''
        if escolha == 1:
            personagem = lista_classes.objeto_lista_de_classe.__getitem__(0)
        elif escolha == 2:
            personagem = lista_classes.objeto_lista_de_classe.__getitem__(1)
        elif escolha == 3:
            personagem = lista_classes.objeto_lista_de_classe.__getitem__(2)
        elif escolha == 4:
            personagem = lista_classes.objeto_lista_de_classe.__getitem__(3)
        return personagem

    def sortear_inimigo(self, personagem):
        if personagem.sequencia % 5 == 0:
            inimigo_chefe_sorteado = lista_inimigos.objeto_lista_de_inimigos_chefes.sortear_objeto()
            return inimigo_chefe_sorteado
        else:
            inimigo_comum_sorteado = lista_inimigos.objeto_lista_de_inimigos_comuns.sortear_objeto()
            return inimigo_comum_sorteado

    def validar_acao(self, acao_escolhida, personagem):
        while acao_escolhida == personagem.ultima_escolha:
            print(f'NÃO REPITA')
            acao_escolhida = personagem.escolher_acao()
        personagem.ultima_escolha = acao_escolhida
        return acao_escolhida

    def proibir_repeticao_de_acao(self, escolha_agir, ultima_acao):
        pass

    def calcular_ponto_de_acao(self, personagem, acao_escolhida):
        ponto_acao = 0
        if acao_escolhida == "força":
            ponto_acao = personagem.forca
        elif acao_escolhida == "inteligência":
            ponto_acao = personagem.inteligencia
        elif acao_escolhida == "agilidade":
            ponto_acao = personagem.agilidade
        elif acao_escolhida == "magia":
            ponto_acao = personagem.magia
        return ponto_acao

    def calcular_pontuacao_final(self, ponto_acao, ponto_dado, ponto_modificador):
        ponto_resultado_final = ponto_acao + ponto_dado + ponto_modificador
        return ponto_resultado_final

    def calcular_resultado_final(self, pontuacao_final):
        resultado_final = ''
        if pontuacao_final <= 2:
            resultado_final = 'derrota_destruição'
        elif 3 <= pontuacao_final <= 4:
            resultado_final = 'derrota'
        elif 5 <= pontuacao_final <= 7:
            resultado_final = 'vitória'
        elif 8 <= pontuacao_final:
            resultado_final = 'vitória_destruição'
        return resultado_final

    def contabilizar_vitoria(self, personagem, inimigo):
        personagem.sequencia += 1
        if inimigo.nome == 'duende':
            personagem.duendes_capturados += 1

    def jogar(self):
        personagem = self.escolher_classe()  # ESCOLHA PERSONAGEM
        while True:
            print(personagem)

            inimigo = self.sortear_inimigo(personagem)  # SORTEIO INIMIGO
            print(inimigo)

            ## BATALHA ---------------------------------------
            acao_escolhida = personagem.escolher_acao()  # ESCOLHER AÇÃO
            acao_escolhida_validada = sistema.validar_acao(acao_escolhida, personagem)  # VALIDAR AÇÃO
            print(acao_escolhida_validada)

            ponto_acao = self.calcular_ponto_de_acao(personagem, acao_escolhida_validada)  # CALCULAR PONTO DE AÇÃO
            print(f'Ponto de ação = {ponto_acao}')
            ponto_dado = personagem.jogar_dado()  # JOGAR DADO
            print(f'Ponto de dado = {ponto_dado}')
            ponto_modificador = inimigo.calcular_vantagem_desvantagem(acao_escolhida_validada)  # CALCULAR VANTAGENS E DESVANTAGENS
            print(f'Ponto modificador = {ponto_modificador}')
            pontuacao_final = self.calcular_pontuacao_final(ponto_acao, ponto_dado, ponto_modificador)  # CALCULAR PONTUAÇÃO FINAL
            print(f'Pontuação final = {pontuacao_final}')

            ## DESFECHO ---------------------------------------
            resultado_final = self.calcular_resultado_final(pontuacao_final)
            print(resultado_final)

            ## DESFECHO GANHOU ---------------------------------------
            if resultado_final == 'vitória' or resultado_final == 'vitória_destruição':
                print('Vitória!')
                self.contabilizar_vitoria(personagem, inimigo)  # CONTAR SEQUENCIA E EVENTUAL DUENDE CAPTURADO
                inimigo.agir_na_derrota(personagem)  # ATRIBUIR ITEM OU MALDIÇÃO DEPENDENDO DO INIMIGO
                print(personagem)
                print(personagem.sequencia, personagem.duendes_capturados)
            # CONTINUAR ?
            ## DESFECHO PERDEU ---------------------------------------
            else:
                print('Derrota.')
                break
            # IMPRIMIR RESULTADOS
            # ZERAR SEQUENCIA, DUENDES e ULTIMA_ACAO



## INTRODUÇÃO ---------------------------------------
sistema = Sistema()
sistema.imprimir_titulo()
sistema.exibir_menu()
