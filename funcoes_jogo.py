from random import randint

import listas
from funcoes_base import espaco


def escolher_classe():
    global persona
    classe = int(input('Esolha uma classe:\n[1] Guerreiro [2] Feiticeiro [3] Caçador [4] Necromante\n → '))
    if classe == 1:
        persona = listas.guerreiro.copy()
    elif classe == 2:
        persona = listas.feiticeiro.copy()
    elif classe == 3:
        persona = listas.cacador.copy()
    elif classe == 4:
        persona = listas.necromante.copy()
    return persona

def imprimir_personagem(mensagem, persona):
    print(f'{mensagem} {persona["nome"].title()}.')
    for k, v in persona.items():
        if not k == 'nome':
            print(f'{k.capitalize()}: {v} | ', end='')
    print()
    espaco()

def sortear_inimigo():
    inimigo = listas.listaInimigos[randint(0, 3)]
    return inimigo

def imprimir_inimigo(inimigo):
    print(f'♦ O inimigo é {inimigo["nome"].title()}.')
    for k, v in inimigo.items():
        if not k == 'nome':
            print(f'{k.capitalize()}: {v} | ', end='')
    print()
    espaco()

def escolher_acao():
    escolhaAgir = ''
    agir = int(input('Esolha como agir:\n[1] Força [2] Inteligência [3] Agilidade [4] Magia\n → '))
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
    return ponto


def jogar_dado_ataque(ponto_acao):
    input('Jogue o dado [ENTER]: ')
    dado = randint(0, 6)
    print(f'• {dado} pontos de ataque.')
    ataque = dado + ponto_acao
    print(f'• Valor de ataque: {ataque}.')
    return ataque

def calcular_vantagens(escolhaAgir, ataque, inimigo):
    ataqueVantagem = ataque

    if escolhaAgir == inimigo["fraqueza"]:
        print('• Bônus de ação: +2 no dado.')
        ataqueVantagem = ataque + 2

    return ataqueVantagem

def calcular_desvantagens(ataqueVantagem, persona, inimigo):
    ataqueDesvantagem = ataqueVantagem

    if persona["vantagem"] == inimigo["resistência"]:
        print('• Desvantagem de classe: -2 no dado.')
        ataqueDesvantagem = ataqueVantagem - 2

    return ataqueDesvantagem

def calcular_resultado(ataqueFinal):
    espaco()
    if ataqueFinal >= 6:
        print('Vitória!')
        return True
    else:
        print('Derrota.')
        return False

def escolha_continuar():
    escolha = int(input('Continuar? [1] Sim [2] Não\n→ '))
    while escolha > 2 or escolha < 1:
        escolha = int(input('→ '))

    if escolha == 2:
        print('Fim do jogo')
        return False
    else:
        return True