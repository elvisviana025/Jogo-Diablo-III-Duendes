# Jogo 1
from random import randint
import listas
import funcoes_base
import funcoes_jogo

# 1. Título
funcoes_base.espaco()
funcoes_base.titulo("Jogo")
funcoes_base.espaco()

# 2. Escolher personagem
persona = funcoes_jogo.escolher_classe()

print(f'Você escolheu a classe {persona["nome"].title()}.')
for k, v in persona.items():
    if not k == 'nome':
        print(f'{k.capitalize()}: {v} | ', end='')
print()

funcoes_base.espaco()

# 3. Batalhar
# 3.1 Inimigo
inimigo = funcoes_jogo.sortear_inimigo()
print(f'O inimigo é {inimigo["nome"].title()}.')
for k, v in inimigo.items():
    if not k == 'nome':
        print(f'{k.capitalize()}: {v} | ', end='')
print()

# 3.2 Dados
escolhaAgir = funcoes_jogo.escolher_acao()
ponto_acao = funcoes_jogo.somar_ponto_acao(persona, escolhaAgir)

ataque = funcoes_jogo.jogar_dado_ataque(ponto_acao)
print(f'Valor de ataque: {ataque}.')

ataqueFinal = funcoes_jogo.calcular_vantagens(escolhaAgir, ataque, persona, inimigo)
print(f'O ataque do seu personagem {persona["nome"]} foi {ataqueFinal}.')

# 3.3 Desfecho
funcoes_jogo.calcular_resultado(ataqueFinal)
