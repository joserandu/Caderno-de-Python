"""
JSON E PICKLE

JSON - JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas e terceiros (nós desenvolvedores).
"""

import json
import jsonpickle

retorno = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

"""
O dumps serve para formatar, perceba que na impressão ele colocou todas as aspas duplas, tirou as tuplas.
"""

print(type(retorno))
print(retorno)

print("Utilizando classes --------------------------------------------------------------------------------------------")


class Animal:

    def __init__(self, nome, tamanho):
        self.__nome = nome
        self.__tamanho = tamanho

    @property
    def nome(self):
        return self.__nome

    @property
    def tamanho(self):
        return self.__tamanho


felix = Animal('Felix', 30)

print(felix.__dict__)

retorno = json.dumps(felix.__dict__)  # Não esqueça o método __dict__
print(retorno)

"""
O arquivo json é um dicionário basicamente
"""

print("Integrando JSON com Pickle ------------------------------------------------------------------------------------")

retorno = jsonpickle.encode(felix)
print(retorno)

"""
{"py/object": "__main__.Animal", "_Animal__nome": "Felix", "_Animal__tamanho": 30}

Isso permite que o arquivo pickle identifique por primeiro que é um objeto python para depois serealizar
"""

# Escrevendo no arquivo pickle
with open('felix.json', 'w', encoding='utf-8') as arquivo:
    retorno = jsonpickle.encode(felix)
    arquivo.write(retorno)

# Lendo o arquivo
with open('felix.json', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    retorno = jsonpickle.decode(conteudo)
    print(retorno)
    print(type(retorno))
    print(retorno.nome)
    print(f"{retorno.tamanho} cm")
