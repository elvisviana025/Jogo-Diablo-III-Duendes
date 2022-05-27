from personagem import Personagem
from lista_de_objetos import Lista_de_objetos

maior = 3
medio = 2
menor = 1

guerreiro = personagem = Personagem('guerreiro', 'força', maior, menor, medio, menor)
feiticeiro = Personagem('feiticeiro', 'magia', medio, medio, menor, maior)
cacador = Personagem('caçador', 'agilidade', medio, medio, maior, menor)
monge = Personagem('monge', 'inteligência', menor, maior, medio, medio)

lista_de_classes = [guerreiro, feiticeiro, cacador, monge]
objeto_lista_de_classe = Lista_de_objetos('Lista de Classes', lista_de_classes)
