from random import randint
from time import sleep

import listas
from funcoes_base import espaco


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
            print(f'{k.capitalize()}: {v} | ', end='')
    print()
    espaco()
    sleep(1)

def sortear_inimigo():
    inimigo = listas.listaInimigos[randint(0, len(listas.listaInimigos) - 1)]
    return inimigo

def sortear_chefe():
    inimigo = listas.listaChefes[randint(0, len(listas.listaChefes) - 1)]
    return inimigo

def imprimir_inimigo(inimigo):
    print(f'♦ O inimigo é {inimigo["nome"].title()}.')
    for k, v in inimigo.items():
        if not k == 'nome':
            print(f'{k.capitalize()}: {v} | ', end='')
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
    if escolhaAgir == inimigo["resistência"]:
        print('• Desvantagem de resistência do inimigo: - 1 no dado.')
        sleep(1)
        ataqueDesvantagem = ataqueVantagem - 1

    return ataqueDesvantagem

def calcular_resultado(ataqueFinal):
    espaco()
    if ataqueFinal >= 5:
        print('Vitória!')
        sleep(1)
        return True
    else:
        print('Derrota.')
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
            print('• Duende deixou "amuleto de força": + 1 de força.')
        elif item == 1:
            persona['inteligência'] += 1
            print('• Duende deixou "amuleto de inteligência": + 1 de inteligência.')
        elif item == 2:
            persona['agilidade'] += 1
            print('• Duende deixou "amuleto de agilidade": + 1 de agilidade.')
        elif item == 3:
            persona['magia'] += 1
            print('• Duende deixou "amuleto de magia": + 1 de magia.')
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
