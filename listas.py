# Dicionários classes
maior = 3
medio = 2
menor = 1


guerreiro = {"nome": "guerreiro",
             "vantagem": "força",
             "força": maior,
             "inteligência": menor,
             "agilidade": medio,
             "magia": menor}

feiticeiro = {"nome": "feiticeiro",
              "vantagem": "magia",
              "força": medio,
              "inteligência": medio,
              "agilidade": menor,
              "magia": maior}

cacador = {"nome": "caçador",
           "vantagem": "agilidade",
            "força": medio,
            "inteligência": medio,
            "agilidade": maior,
            "magia": menor}

monge = {"nome": "monge",
              "vantagem": "inteligência",
              "força": menor,
              "inteligência": maior,
              "agilidade": medio,
              "magia": medio}

listaClasse = [guerreiro, feiticeiro, cacador, monge]

# Dicionarios inimiogs
morcegos = {"nome": "revoada de morcegos", "fraqueza": "agilidade", "resistência": 'magia', "resistência 2": " - "}
serpente = {"nome": "serpente enfeitiçada", "fraqueza": "agilidade", "resistência": 'magia', "resistência 2": " - "}

diabrete_g = {"nome": "diabrete guerreiro", "fraqueza": "inteligência", "resistência": 'força', "resistência 2": " - "}
orc = {"nome": "orc", "fraqueza": "inteligência", "resistência": 'força', "resistência 2": " - "}

diabrete_s = {"nome": "diabrete sagaz", "fraqueza": "força", "resistência": 'inteligência', "resistência 2": " - "}
duende = {"nome": "duende", "fraqueza": " - ", "resistência": 'inteligência', "resistência 2": " - "}

fantasma = {"nome": "fantasma", "fraqueza": "magia", "resistência": 'agilidade', "resistência 2": " - "}
fantasma_ceifador = {"nome": "fantasma ceifador", "fraqueza": " - ", "resistência": 'agilidade', "resistência 2": " - "}

listaInimigos = [morcegos, serpente, orc, diabrete_g, duende, diabrete_s, fantasma, fantasma_ceifador]

# Dicionário Chefes

# fada = {"nome": "fada das trevas", "fraqueza": " - ", "resistência": 'magia'}
# anjo = {"nome": "anjo renegado", "fraqueza": " - ", "resistência": 'força'}
# genio = {"nome": "gênio corrompido", "fraqueza": " - ", "resistência": 'inteligência'}
# espirito = {"nome": "espírito das legiões", "fraqueza": " - ", "resistência": 'agilidade'}

fada = {"nome": "fada das trevas", "fraqueza": " - ", "resistência": 'magia', "resistência 2": "inteligência"}
anjo = {"nome": "anjo renegado", "fraqueza": " - ", "resistência": 'força', "resistência 2": "agilidade"}
genio = {"nome": "gênio corrompido", "fraqueza": " - ", "resistência": 'inteligência', "resistência 2": "força"}
espirito = {"nome": "espírito dos bruxos", "fraqueza": " - ", "resistência": 'agilidade', "resistência 2": "magia"}


listaChefes = [fada, anjo, genio, espirito]
