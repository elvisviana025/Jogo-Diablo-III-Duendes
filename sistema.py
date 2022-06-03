from random import randint
from time import sleep
import copy

import lista_classes
import lista_inimigos


class Sistema():

    def __init__(self):
        pass

    def __espaco(self):
        print('-' * 80)

    def __pausa(self):
        sleep(1)

    def imprimir_titulo(self):
        self.__espaco()
        print(f'{"Diablo III : Caça aos Duendes":^80}')
        self.__espaco()

    def exibir_menu(self):
        while True:
            escolha = int(input('Menu:\n[1] Jogar [2] Regras [3] Classes [4] Sair\n → '))
            if escolha == 1:
                self.__jogar()
            elif escolha == 2:
                self.__imprimir_regras()
            elif escolha == 3:
                self.__imprimir_classes()
            elif escolha == 4:
                break

    def __imprimir_regras(self):
        print('→ Objetivo: ache e capture o maior número de duendes.\n'
              '→ Você irá enfrentar até 21 inimigos na sua busca.'
              '→ Você ganha a batalha se tiver 5 ou mais pontos de ataque.\n'
              '→ Você não pode repetir uma ação em duas batalhas seguidas.\n'
              '→ Fraquezas e resistências do inimigo: + 1 ou - 1 ponto de ataque.')
        self.__espaco()

    @staticmethod
    def __imprimir_classes():
        print(f'Lista de classes: ')
        for classe in lista_classes.lista_de_classes:
            classe.imprimir_classe_formatada()

    def __escolher_caminho(self):
        caminho = int(input('Escolha um caminho:\n[1] Floresta [2] Cidadela [3] Deserto [4] Caminho Montanhoso\n → '))
        if caminho == 1:
            print(f'• Floresta: você adentra um caminho de árvores, pântanos, grutas e clareiras.')
            return 0
        if caminho == 2:
            print(f'• Cidadela: você adentra um caminho de becos, vielas, criptas e tavernas.')
            return 1
        if caminho == 3:
            print(f'• Deserto: você adentra um caminho de dunas, povoados, caravanas e ruínas.')
            return 2
        if caminho == 4:
            print(f'• Caminho Montanhoso: você adentra um caminho de cavernas, desfiladeiros e rochas.')
            return 3

    def __escolher_classe(self):
        self.__espaco()
        escolha = int(input('Escolha uma classe:\n[1] Guerreiro [2] Feiticeiro [3] Caçador [4] Monge\n → '))
        personagem = ''
        if escolha == 1:
            personagem = copy.deepcopy(lista_classes.objeto_lista_de_classe.__getitem__(0))
        elif escolha == 2:
            personagem = copy.deepcopy(lista_classes.objeto_lista_de_classe.__getitem__(1))
        elif escolha == 3:
            personagem = copy.deepcopy(lista_classes.objeto_lista_de_classe.__getitem__(2))
        elif escolha == 4:
            personagem = copy.deepcopy(lista_classes.objeto_lista_de_classe.__getitem__(3))
        print(f'Você escolheu a classe {personagem.nome.title()}.')
        print(personagem)
        self.__espaco()
        return personagem

    def __sortear_inimigo(self, personagem, caminho):
        if personagem.sequencia % 5 == 0 and personagem.sequencia != 0:
            inimigo_chefe_sorteado = lista_inimigos.objeto_lista_de_inimigos_chefes.sortear_objeto()
            print(f'Chefão! O inimigo é {inimigo_chefe_sorteado.retornar_nome(caminho)}.')
            print(inimigo_chefe_sorteado.retornar_informacoes(caminho))
            self.__espaco()
            return inimigo_chefe_sorteado
        else:
            inimigo_comum_sorteado = lista_inimigos.objeto_lista_de_inimigos_comuns.sortear_objeto()
            print(f'O inimigo é {inimigo_comum_sorteado.retornar_nome(caminho)}.')
            print(inimigo_comum_sorteado.retornar_informacoes(caminho))
            self.__espaco()
            return inimigo_comum_sorteado

    def __validar_acao(self, acao_escolhida, personagem):
        while acao_escolhida == personagem.ultima_escolha:
            print(f'* Sua habilidade está se recuperando. Escolha outra.')
            self.__pausa()
            acao_escolhida = personagem.escolher_acao()
        personagem.ultima_escolha = acao_escolhida
        print(f'• O {personagem.nome.title()} agiu com {acao_escolhida}.')
        return acao_escolhida

    def __calcular_ponto_de_acao(self, personagem, acao_escolhida):
        ponto_acao = 0
        if acao_escolhida == "força":
            ponto_acao = personagem.forca
        elif acao_escolhida == "inteligência":
            ponto_acao = personagem.inteligencia
        elif acao_escolhida == "agilidade":
            ponto_acao = personagem.agilidade
        elif acao_escolhida == "magia":
            ponto_acao = personagem.magia
        print(f'• Pontos de ação = {ponto_acao}')
        return ponto_acao

    def __calcular_pontuacao_final(self, ponto_acao, ponto_dado, ponto_modificador):
        ponto_resultado_final = ponto_acao + ponto_dado + ponto_modificador
        print(f'Pontuação final = {ponto_resultado_final}')
        self.__espaco()
        return ponto_resultado_final

    def __calcular_resultado_final(self, pontuacao_final):
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

    def __contabilizar_vitoria(self, personagem, inimigo, caminho, resultado_final):
        personagem.sequencia += 1
        if inimigo.retornar_nome(caminho) == 'Duende':
            personagem.duendes_capturados += 1
        if resultado_final == 'vitória_destruição' and inimigo.retornar_nome(caminho) != 'Duende':
            personagem.inimigos_destruidos += 1

    def __continuar_batalhas(self):
        escolha = int(input('Continuar? [1] Sim [2] Não\n→ '))
        while escolha > 2 or escolha < 1:
            escolha = int(input('→ '))
        if escolha == 2:
            return False
        else:
            return True

    def __imprimir_resultados_das_batalhas(self, personagem):
        print(f'Sequência: {personagem.sequencia}/21 vitória(s) | Duendes capturados: {personagem.duendes_capturados}')
        self.__pausa()
        print(personagem)
        self.__espaco()

    def __imprimir_resultados_finais(self, personagem):
        print('Fim de jogo!')
        self.__pausa()
        print(f'Sequência: {personagem.sequencia}/21 batalhas vencidas'
              f' | Duendes capturados: {personagem.duendes_capturados}'
              f' | Inimigos destruídos: {personagem.inimigos_destruidos}' )
        self.__pausa()

    def __imprimir_texto_batalha(self, personagem, inimigo, resultado_final, caminho):
        numero_sorteado = randint(1,3)

        if resultado_final ==  "derrota_destruição":
            if numero_sorteado == 1:
                print(f'• Você foi derrotado após um ataque trapaceiro de {inimigo.resistencia} do inimigo {inimigo.retornar_nome(caminho)}.')
            elif numero_sorteado == 2:
                print(f'• Você foi derrotado após um rápido ataque de {inimigo.resistencia} do inimigo {inimigo.retornar_nome(caminho)}.')
            elif numero_sorteado == 3:
                print(f'• Você foi emboscado pelo inimigo {inimigo.retornar_nome(caminho)} com um ataque de {inimigo.resistencia}.')
        elif resultado_final ==  "derrota":
            if numero_sorteado == 1:
                print(f'• O inimigo {inimigo.retornar_nome(caminho)} resistiu ao seu ataque com o uso de {inimigo.resistencia}.')
            elif numero_sorteado == 2:
                print(f'• O inimigo {inimigo.retornar_nome(caminho)} escapou para as sombras com o uso de {inimigo.resistencia}.')
            elif numero_sorteado == 3:
                print(f'• O inimigo {inimigo.retornar_nome(caminho)} desviou do seu ataque {personagem.ultima_escolha}.')
        elif resultado_final == "vitória":
            if inimigo.retornar_nome(caminho) == "Duende":
                print(f'• Você capturou o Duende com um ataque de {personagem.ultima_escolha}.')
            else:
                if numero_sorteado == 1:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} fugiu após seu ataque de {personagem.ultima_escolha}.')
                elif numero_sorteado == 2:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} ficou imobilizado após seu ataque de {personagem.ultima_escolha}.')
                elif numero_sorteado == 3:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} ficou atordoado após seu ataque de {personagem.ultima_escolha}.')
        elif resultado_final ==  "vitória_destruição":
            if inimigo.retornar_nome(caminho) == "Duende":
                print(f'• Você capturou o Duende com um ataque de {personagem.ultima_escolha}.')
            else:
                if numero_sorteado == 1:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} foi destruído após seu rápido ataque de {personagem.ultima_escolha}.')
                elif numero_sorteado == 2:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} foi destruído após seu golpe crítico de {personagem.ultima_escolha}.')
                elif numero_sorteado == 3:
                    print(f'• O inimigo {inimigo.retornar_nome(caminho)} foi destruído após seu ataque surpresa de {personagem.ultima_escolha}.')

    def __terminar_aventura(self, personagem, caminho):
        cenarios = ['na Floresta', 'na Cidadela', 'no Deserto', 'no Caminho Montanhoso']
        if personagem.sequencia == 21:
            print(f'\nParabéns! Você concluiu as 21 batalhas dessa aventura {cenarios[caminho]}!')
            return True
        else:
            return False

    def __jogar(self):
        caminho = self.__escolher_caminho() # ESCOLHA O CAMINHO A PERCORRER
        self.__pausa()
        personagem = self.__escolher_classe()  # ESCOLHA PERSONAGEM
        while True:
            self.__pausa()
            inimigo = self.__sortear_inimigo(personagem, caminho)  # SORTEIO INIMIGO
            self.__pausa()

            ## BATALHA ---------------------------------------
            acao_escolhida = personagem.escolher_acao()  # ESCOLHER AÇÃO
            acao_escolhida_validada = self.__validar_acao(acao_escolhida, personagem)  # VALIDAR AÇÃO
            self.__pausa()
            ponto_acao = self.__calcular_ponto_de_acao(personagem, acao_escolhida_validada)  # CALCULAR PONTO DE AÇÃO
            self.__pausa()
            ponto_dado = personagem.jogar_dado()  # JOGAR DADO
            self.__pausa()
            ponto_modificador = inimigo.calcular_vantagem_desvantagem(acao_escolhida_validada)  # CALCULAR VANTAGENS E DESVANTAGENS
            pontuacao_final = self.__calcular_pontuacao_final(ponto_acao, ponto_dado, ponto_modificador)  # CALCULAR PONTUAÇÃO FINAL
            self.__pausa()


            ## DESFECHO ---------------------------------------
            resultado_final = self.__calcular_resultado_final(pontuacao_final)

            ## DESFECHO GANHOU ---------------------------------------
            if resultado_final == 'vitória' or resultado_final == 'vitória_destruição':
                print('Vitória!')
                self.__imprimir_texto_batalha(personagem, inimigo, resultado_final, caminho) # ESCREVE TEXTO BATALHA
                self.__contabilizar_vitoria(personagem, inimigo, caminho, resultado_final)  # CONTAR SEQUENCIA E EVENTUAL DUENDE CAPTURADO
                self.__pausa()
                inimigo.agir_na_derrota(personagem, resultado_final, caminho)  # ATRIBUIR ITEM OU MALDIÇÃO DEPENDENDO DO INIMIGO

                terminar_aventura = self.__terminar_aventura(personagem, caminho)
                if terminar_aventura == True:
                    break

                continuar = self.__continuar_batalhas() # OPÇÃO DE CONTINAR BATALHAS OU FINALIZAR1
                self.__pausa()
                print('')
                if continuar == False:
                    break
                self.__imprimir_resultados_das_batalhas(personagem)

            ## DESFECHO PERDEU ---------------------------------------
            else:
                print('Derrota.')
                self.__imprimir_texto_batalha(personagem, inimigo, resultado_final, caminho) # ESCREVE TEXTO BATALHA
                self.__pausa()
                break
        self.__imprimir_resultados_finais(personagem)
        self.__espaco()


## INTRODUÇÃO ---------------------------------------
# sistema = Sistema()
# sistema.imprimir_titulo()
# sistema.exibir_menu()
