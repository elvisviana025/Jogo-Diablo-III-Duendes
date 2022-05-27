from inimigo import Inimigo_Comum, Inimigo_Chefe
from lista_de_objetos import Lista_de_objetos

# INIMIGOS COMUNS
morcegos = Inimigo_Comum("revoada de morcegos", "agilidade", 'magia')
serpente = Inimigo_Comum("serpente enfeitiçada", "agilidade", 'magia')

diabrete_g = Inimigo_Comum("diabrete guerreiro", "inteligência", 'força')
orc = Inimigo_Comum("orc", "inteligência", 'força')

diabrete_s = Inimigo_Comum("diabrete sagaz", "força", 'inteligência')
duende = Inimigo_Comum("duende", " - ", 'inteligência')

fantasma = Inimigo_Comum("fantasma", "magia", 'agilidade')
fantasma_ceifador = Inimigo_Comum("fantasma ceifador", " - ", 'agilidade')

lista_inimigos_comuns = [morcegos, serpente, orc, diabrete_g, duende, diabrete_s, fantasma, fantasma_ceifador]
objeto_lista_de_inimigos_comuns = Lista_de_objetos('Lista de Inimigos Comuns', lista_inimigos_comuns)

# INIMIGOS CHEFES
fada = Inimigo_Chefe("fada das trevas", " - ", 'magia', "inteligência")
anjo = Inimigo_Chefe("anjo renegado", " - ", 'força', "agilidade")
genio = Inimigo_Chefe("gênio corrompido", " - ", 'inteligência', "força")
espirito = Inimigo_Chefe("espírito dos bruxos", " - ", 'agilidade', "magia")

listaChefes = [fada, anjo, genio, espirito]
objeto_lista_de_inimigos_chefes = Lista_de_objetos('Lista de Inimigos Chefes', listaChefes)
