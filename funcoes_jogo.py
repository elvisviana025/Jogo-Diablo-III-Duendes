from random import randint

import listas

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

def sortear_inimigo():
    inimigo = listas.listaInimigos[randint(0, 3)]
    return inimigo

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
    print(ponto)
    return ponto


def jogar_dado_ataque(ponto_acao):
    input('Jogue o dado [ENTER]: ')
    dado = randint(0, 6)
    ataque = dado + ponto_acao
    return ataque

def calcular_vantagens(escolhaAgir, ataque, persona, inimigo):
    ataqueFinal = ataque

    if escolhaAgir == inimigo["fraqueza"]:
        print('Bônus de ação: +2 no dado.')
        ataqueFinal = ataque + 2
    if persona["vantagem"] == inimigo["resistência"]:
        print('Desvantagem de classe: -2 no dado.')
        ataqueFinal = ataque - 2

    return ataqueFinal

def calcular_resultado(ataqueFinal):
    if ataqueFinal >= 6:
        print('Vitória!')
    else:
        print('Derrota.')
