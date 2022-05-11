# Jogo 1
import funcoes_base
import funcoes_jogo

# 1. Título
funcoes_base.titulo("Jogo")

# 2. Escolher personagem
persona = funcoes_jogo.escolher_classe()
funcoes_jogo.imprimir_personagem('♣ Você escolheu a classe', persona)

sequencia = 0
while True:
    # 3. Batalhar
    # 3.1 Inimigo
    inimigo = funcoes_jogo.sortear_inimigo()
    funcoes_jogo.imprimir_inimigo(inimigo)

    # 3.2 Dados
    escolhaAgir = funcoes_jogo.escolher_acao()
    ponto_acao = funcoes_jogo.somar_ponto_acao(persona, escolhaAgir)

    ataque = funcoes_jogo.jogar_dado_ataque(ponto_acao)

    ataqueVantagem = funcoes_jogo.calcular_vantagens(escolhaAgir, ataque, inimigo)
    ataqueFinal = funcoes_jogo.calcular_desvantagens(ataqueVantagem, persona, inimigo)

    print(f'O ataque do seu personagem {persona["nome"]} foi {ataqueFinal}.')

    # 3.3 Desfecho
    resultado = funcoes_jogo.calcular_resultado(ataqueFinal)

    if resultado == False:
        break

    sequencia = sequencia + 1
    continuar = funcoes_jogo.escolha_continuar()
    if continuar == False:
        break

    funcoes_jogo.imprimir_personagem(f'♣ Sequência de {sequencia} vitória(s) com', persona)

print(f'Você derrotou uma sequência de {sequencia} inimigos!')