# Jogo 1
from random import randint
import listas
import funcoesBase

# 1. Título
funcoesBase.espaco()
funcoesBase.titulo("Jogo")
funcoesBase.espaco()

# 2. Escolher personagem
persona = {}

classe = int(input('Esolha uma classe:\n[1] Guerreiro [2] Feiticeiro [3] Caçador [4] Necromante\n → '))
if classe == 1:
    persona = listas.guerreiro.copy()
elif classe == 2:
    persona = listas.feiticeiro.copy()
elif classe == 3:
    persona = listas.cacador.copy()
elif classe == 4:
    persona = listas.necromante.copy()

print(f'Você escolheu a classe {persona["nome"].title()}.')
print(persona)
funcoesBase.espaco()

# 3. Batalhar
# 3.1 Inimigo
inimigo = listas.listaInimigos[randint(0,3)]
print(f'O inimigo é {inimigo["nome"]}.')

# 3.2 Dados
escolhaAgir = 0
agir = int(input('Esolha como agir:\n[1] Força [2] Inteligência [3] Agilidade [4] Magia\n → '))
if agir == 1:
    escolhaAgir = persona["força"]
elif agir == 2:
    escolhaAgir = persona["inteligência"]
elif agir == 3:
    escolhaAgir = persona["agilidade"]
elif agir == 4:
    escolhaAgir = persona["magia"]



input('Jogue o dado [ENTER]: ')
dado = randint(0,6)
ataque = dado + escolhaAgir
print(f'Valor de ataque: {ataque}.')
if persona["poder"] == inimigo["fraqueza"]:
    print('Bônus de classe: +2 no dado.')
    ataque = ataque + 2

print(f'O ataque do seu personagem {persona["nome"]} foi {ataque}.')

# 3.3 Desfecho
if ataque >= 6:
    print('Vitória!')
else:
    print('Derrota.')
