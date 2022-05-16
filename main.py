# Jogo 1
from time import sleep

import funcoes_base
import funcoes_jogo

def jogar():

    # 1 Variáveis
    duendes_capturados = 0
    sequencia = 0
    ultima_acao = ''

    # 2. Escolher personagem
    persona = funcoes_jogo.escolher_classe() # jogador escolhe classe
    funcoes_jogo.imprimir_personagem('♣ Você escolheu a classe', persona) # jogo imprime dados do personagem

    while True:
        # 3. Batalhar
        # 3.1 Inimigo
        inimigo = funcoes_jogo.sortear_inimigo(sequencia)

        # 3.2 Dados
        escolhaAgir = funcoes_jogo.escolher_acao() # jogador escolhe a ação

        validacao = funcoes_jogo.proibe_repeticao_de_acao(escolhaAgir, ultima_acao) # jogo proibe repetir ação
        escolhaAgir = validacao[0]
        ultima_acao = validacao[1]

        ponto_acao = funcoes_jogo.somar_ponto_acao(persona, escolhaAgir) # jogo calcula o ponto da ação

        ataque = funcoes_jogo.jogar_dado_ataque(ponto_acao) # jogador joga dado para somar ao ponto de ação

        ataqueVantagem = funcoes_jogo.calcular_vantagens(escolhaAgir, ataque, inimigo) # jogo calcula vantagens
        ataqueFinal = funcoes_jogo.calcular_desvantagens(ataqueVantagem, persona, escolhaAgir, inimigo) # jogo calcula desvantagens

        funcoes_jogo.imprime_ataque_final(persona, ataqueFinal) # jogo imprime resultado final


        # 3.3 Desfecho
        resultado = funcoes_jogo.calcular_resultado(ataqueFinal, inimigo, escolhaAgir) # jogo calcula se os pontos dão vitória ou derrota

        if resultado == False:
            break

        sequencia = sequencia + 1

        funcoes_jogo.duende_deixa_item(inimigo, persona) # jogo calcula item
        duendes_capturados = funcoes_jogo.captura_duende(inimigo, duendes_capturados) # jogo calcula duendes capturados
        funcoes_jogo.ceifador_amaldicoa(inimigo, persona) # jogo calcula maldição

        continuar = funcoes_jogo.escolha_continuar() # jogador escolhe continuar ou não
        if continuar == False:
            break

        funcoes_jogo.imprimir_personagem(f'\n♣ Sequência de {sequencia} vitória(s) com', persona) # jogo imprime o personagem e a sequência

    print(f'Você derrotou uma sequência de {sequencia} inimigo(s) e capturou {duendes_capturados} duende(s)!\n')
    sleep(1)


# 0.0 O INÍCIO
funcoes_base.titulo("Diablo III : Caça aos Duendes")
while True:
    escolha = int(input('Menu:\n[1] Jogar [2] Regras [3] Classes [4] Sair\n → '))
    if escolha == 1:
        funcoes_base.espaco()
        jogar()
    elif escolha == 2:
        funcoes_jogo.imprime_regras()
    elif escolha == 3:
        funcoes_jogo.imprime_classes()
    elif escolha == 4:
        break