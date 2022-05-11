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

necromante = {"nome": "necromante",
              "vantagem": "inteligência",
              "força": menor,
              "inteligência": maior,
              "agilidade": medio,
              "magia": medio}

# Dicionarios inimiogs
morcegos = {"nome": "revoada de morcegos", "fraqueza": "agilidade", "resistência": 'magia'}

ogro = {"nome": "ogro", "fraqueza": "inteligência", "resistência": 'força'}

duende = {"nome": "duende", "fraqueza": "força", "resistência": 'inteligência'}

fantasma = {"nome": "fantasma", "fraqueza": "magia", "resistência": 'agilidade'}

listaInimigos = [morcegos, ogro, duende, fantasma]
