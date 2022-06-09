from personagem import Personagem
from lista_de_objetos import Lista_de_objetos

maior = 3
medio = 2
menor = 1

guerreiro = Personagem('guerreiro', 'força', maior, menor, medio, menor, 'Javaré')
feiticeiro = Personagem('feiticeiro', 'magia', medio, medio, menor, maior, 'Gatoruja')
cacador = Personagem('caçador', 'agilidade', medio, medio, maior, menor, 'Cachorráguia')
monge = Personagem('monge', 'inteligência', menor, maior, medio, medio, 'Dracobra')

lista_de_classes = [guerreiro, feiticeiro, cacador, monge]
objeto_lista_de_classe = Lista_de_objetos('Lista de Classes', lista_de_classes)
