from random import randint
from time import sleep

import listas
from funcoes_base import espaco

def imprime_regras():
    print('→ Objetivo: ache e capture o maior número de duendes.\n'
          '→ Você ganha a batalha se tiver 5 ou mais pontos de ataque.\n'
          '→ Você não pode repetir uma ação em duas batalhas seguidas.\n'
          '→ Fraquezas e resistências do inimigo: + 1 ou - 1 ponto de ataque.')
    espaco()

def imprime_classes():
    print('Veja as classes que você pode escolher:')
    for classe in listas.listaClasse:
        for k, v in classe.items():
            if k == 'nome':
                print(f'→ {v.title():10} | ', end='')
            elif k == 'vantagem':
                print(f'{k.title()}: {v:12} | ', end='')
            else:
                print(f'{k.title()}: {v} | ', end='')
        print()
    espaco()

def escolher_classe():
    global persona
    classe = int(input('Escolha uma classe:\n[1] Guerreiro [2] Feiticeiro [3] Caçador [4] Monge\n → '))
    if classe == 1:
        persona = listas.guerreiro.copy()
    elif classe == 2:
        persona = listas.feiticeiro.copy()
    elif classe == 3:
        persona = listas.cacador.copy()
    elif classe == 4:
        persona = listas.monge.copy()
    return persona

def imprimir_personagem(mensagem, persona):
    print(f'{mensagem} {persona["nome"].title()}.')
    for k, v in persona.items():
        if not k == 'nome':
            print(f'{k.title()}: {v} | ', end='')
    print()
    espaco()
    sleep(1)

def sortear_inimigo_padrao():
    inimigo = listas.listaInimigos[randint(0, len(listas.listaInimigos) - 1)]
    return inimigo

def sortear_inimigo_chefe():
    inimigo = listas.listaChefes[randint(0, len(listas.listaChefes) - 1)]
    return inimigo

def sortear_inimigo(sequencia):
    chefe = sequencia % 5 == 0 and sequencia != 0
    if chefe:
        print('Chefão!')
        inimigo = sortear_inimigo_chefe()  # jogo sorteia chefão
    else:
        inimigo = sortear_inimigo_padrao()  # jogo sorteia inimigo

    imprimir_inimigo(inimigo)  # jogo imprime dados do inimigo
    return inimigo

def imprimir_inimigo(inimigo):
    print(f'♦ O inimigo é {inimigo["nome"].title()}.')
    for k, v in inimigo.items():
        if k != 'nome':
            if not (k == 'resistência 2' and v == ' - '):
                print(f'{k.title()}: {v} | ', end='')
    print()
    espaco()
    sleep(1)

def escolher_acao():
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

def proibe_repeticao_de_acao(escolhaAgir, ultima_acao):
    while escolhaAgir == ultima_acao:
        print(f'** Sua habilidade está se recuperando. Escolha outra.')
        sleep(1)
        escolhaAgir = escolher_acao()
    ultima_acao = escolhaAgir
    return escolhaAgir, ultima_acao

def somar_ponto_acao(persona, escolhaAgir):
    ponto = 0
    for k, v in persona.items():
        if k == escolhaAgir:
            ponto = v
    print(f'• {ponto} pontos de ataque.')
    sleep(1)
    return ponto


def jogar_dado_ataque(ponto_acao):
    input('Jogue o dado de 1 a 6 [ENTER]: ')
    dado = randint(1, 6)
    print(f'• {dado} pontos de ataque.')
    sleep(1)
    ataque = dado + ponto_acao
    print(f'• Valor de ataque: {ataque}.')
    sleep(1)
    return ataque

def calcular_vantagens(escolhaAgir, ataque, inimigo):
    ataqueVantagem = ataque

    if escolhaAgir == inimigo["fraqueza"]:
        print('• Bônus de fraqueza do inimigo: + 1 no dado.')
        sleep(1)
        ataqueVantagem = ataque + 1

    return ataqueVantagem

def calcular_desvantagens(ataqueVantagem, persona, escolhaAgir, inimigo):
    ataqueDesvantagem = ataqueVantagem

    # if persona["vantagem"] == inimigo["resistência"]:
    if escolhaAgir == inimigo["resistência"] or escolhaAgir == inimigo["resistência 2"]:
        print('• Desvantagem de resistência do inimigo: - 1 no dado.')
        sleep(1)
        ataqueDesvantagem = ataqueVantagem - 1

    return ataqueDesvantagem

def imprime_ataque_final(persona, ataqueFinal):
    print(f'O ataque do seu personagem {persona["nome"]} foi {ataqueFinal}.')
    sleep(1)

def imprime_texto_batalha(ataqueFinal, inimigo, escolhaAgir):
    nome_inimigo = inimigo["nome"].title()
    seu_ataque = escolhaAgir
    ataque_inimigo = inimigo["resistência"]
    if nome_inimigo == 'Duende' and ataqueFinal >= 5:
        print(f'• O {nome_inimigo} foi capturado após seu ataque de {seu_ataque}.')
    elif nome_inimigo == 'Duende' and ataqueFinal <= 4:
        print(f'• O {nome_inimigo} fugiu dando uma grande gargalhada.')
    elif ataqueFinal <= 2:
        print(f'• O inimigo {nome_inimigo} te derrotou com um ataque de {ataque_inimigo}.')
    elif ataqueFinal >= 3 and ataqueFinal <= 4:
        print(f'• O inimigo {nome_inimigo} resistiu ao seu ataque de {seu_ataque} com uso de {ataque_inimigo}.')
    elif ataqueFinal >= 5 and ataqueFinal <= 7:
        print(f'• O inimigo {nome_inimigo} fugiu após seu ataque de {seu_ataque}.')
    elif ataqueFinal >= 8:
        print(f'• O inimigo {nome_inimigo} foi destruído por seu ataque de {seu_ataque}.')

def calcular_resultado(ataqueFinal, inimigo, escolhaAgir):
    espaco()
    if ataqueFinal >= 5:
        print('Vitória!')
        imprime_texto_batalha(ataqueFinal, inimigo, escolhaAgir)
        sleep(1)
        return True
    else:
        print('Derrota.')
        imprime_texto_batalha(ataqueFinal, inimigo, escolhaAgir)
        sleep(1)
        return False

def captura_duende(inimigo, duendes_capturados):
    if inimigo['nome'] == 'duende':
        duendes_capturados += 1
    return duendes_capturados

def duende_deixa_item(inimigo, persona):
    item = randint(0, 3)
    if inimigo["nome"] == 'duende':
        if item == 0:
            persona['força'] += 1
            print('• O Duende deixou cair um "amuleto de força": + 1 de força.')
        elif item == 1:
            persona['inteligência'] += 1
            print('• O Duende deixou cair um "amuleto de inteligência": + 1 de inteligência.')
        elif item == 2:
            persona['agilidade'] += 1
            print('• O Duende deixou cair um "amuleto de agilidade": + 1 de agilidade.')
        elif item == 3:
            persona['magia'] += 1
            print('• O Duende deixou cair um "amuleto de magia": + 1 de magia.')
        sleep(1)


def ceifador_amaldicoa(inimigo, persona):
    item = randint(0, 3)
    if inimigo["nome"] == 'fantasma ceifador':
        if item == 0:
            persona['força'] -= 1
            print('• Ceifador jogou uma maldição: - 1 de força.')
        elif item == 1:
            persona['inteligência'] -= 1
            print('• Ceifador jogou uma maldição: - 1 de inteligência.')
        elif item == 2:
            persona['agilidade'] -= 1
            print('• Ceifador jogou uma maldição: - 1 de agilidade.')
        elif item == 3:
            persona['magia'] -= 1
            print('• Ceifador jogou uma maldição: - 1 de magia.')
        sleep(1)

def escolha_continuar():
    escolha = int(input('Continuar? [1] Sim [2] Não\n→ '))
    while escolha > 2 or escolha < 1:
        escolha = int(input('→ '))
    sleep(1)

    if escolha == 2:
        print('Fim do jogo')
        return False
    else:
        return True
