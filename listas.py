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

# Dicionarios inimiogs
morcegos = {"nome": "revoada de morcegos", "fraqueza": "agilidade", "resistência": 'magia'}
serpente = {"nome": "serpente enfeitiçada", "fraqueza": "agilidade", "resistência": 'magia'}

diabrete_g = {"nome": "diabrete guerreiro", "fraqueza": "inteligência", "resistência": 'força'}
orc = {"nome": "orc", "fraqueza": "inteligência", "resistência": 'força'}

diabrete_s = {"nome": "diabrete sagaz", "fraqueza": "força", "resistência": 'inteligência'}
duende = {"nome": "duende", "fraqueza": "nenhuma", "resistência": 'inteligência'}

fantasma = {"nome": "fantasma", "fraqueza": "magia", "resistência": 'agilidade'}
fantasma_ceifador = {"nome": "fantasma ceifador", "fraqueza": "nenhuma", "resistência": 'agilidade'}

listaInimigos = [morcegos, serpente, orc, diabrete_g, duende, diabrete_s, fantasma, fantasma_ceifador]

# Dicionário Chefes

fada = {"nome": "fada das trevas", "fraqueza": "nenhuma", "resistência": 'magia'}
anjo = {"nome": "anjo renegado", "fraqueza": "nenhuma", "resistência": 'força'}
genio = {"nome": "gênio corrompido", "fraqueza": "nenhuma", "resistência": 'inteligência'}
espirito = {"nome": "espírito das legiões", "fraqueza": "nenhuma", "resistência": 'agilidade'}

listaChefes = [fada, anjo, genio, espirito]
