from inimigo import Inimigo_Comum, Inimigo_Chefe
from lista_de_objetos import Lista_de_objetos

# INIMIGOS COMUNS
voador_agil = Inimigo_Comum(["revoada de morcegos", "gárgula enfeitiçada", "revoada de vespas", "revoada de morcegos"], "agilidade", 'magia')
rastejante_agil = Inimigo_Comum(["serpente enfeitiçada", "ratazana enfeitiçada", "verme da areia", "aranha enfeitiçada"], "agilidade", 'magia')

diabrete_g = Inimigo_Comum(["diabrete guerreiro", "diabrete guerreiro", "diabrete guerreiro", "diabrete guerreiro"], "inteligência", 'força')
orc = Inimigo_Comum(["orc da floresta", "orc pilhador", "orc das dunas", "orc das cavernas"], "inteligência", 'força')

diabrete_s = Inimigo_Comum(["diabrete sagaz", "diabrete sagaz", "diabrete sagaz", "diabrete sagaz"], "força", 'inteligência')
duende = Inimigo_Comum(["duende", "duende", "duende", "duende"], " - ", 'inteligência')

fantasma = Inimigo_Comum(["fantama do pântano", "fantasma do cavaleiro", "fantasma ghoul", "fantasma do abismo"], "magia", 'agilidade')
fantasma_ceifador = Inimigo_Comum(["fantasma ceifador", "fantasma ceifador", "fantasma ceifador", "fantasma ceifador"], " - ", 'agilidade')

lista_inimigos_comuns = [voador_agil, rastejante_agil, orc, diabrete_g, duende, diabrete_s, fantasma, fantasma_ceifador]
objeto_lista_de_inimigos_comuns = Lista_de_objetos('Lista de Inimigos Comuns', lista_inimigos_comuns)

# INIMIGOS CHEFES
magia_inteligencia = Inimigo_Chefe(["fada das trevas", "sacerdote das trevas", "sacerdote dos escaravelhos", "harpia das trevas"], " - ", 'magia', "inteligência")
forte_agil = Inimigo_Chefe(["lobo gigante", "anjo renegado", "escorpião gigante", "urso gigante"], " - ", 'força', "agilidade")
forte_inteligente = Inimigo_Chefe(["orc supremo", "paladino corrompido", "gênio corrompido", "dragão dourado"], " - ", 'inteligência', "força")
magia_agil = Inimigo_Chefe(["bruxa da vassoura", "bruxo das alcovas", "verme da areia supremo", "rainha das aranhas"], " - ", 'agilidade', "magia")

listaChefes = [magia_inteligencia, forte_agil, forte_inteligente, magia_agil]
objeto_lista_de_inimigos_chefes = Lista_de_objetos('Lista de Inimigos Chefes', listaChefes)
