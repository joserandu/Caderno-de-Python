"""
ZIP

Ele cria um iterável chamado zip object que agrega elementos de cada um dos iteráveis passados como entrada em pares.
"""

print('Modo de uso do zip ------------------------------------------------------------------zip(lista1, lista2, "abc")')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(list(zip1))
print(type(zip1))

print('Economia de dados ------------------------------------------------------------------------list(zip1) tuple(zip)')

"""
Sempre podemos gerar uma lista, tupla, set ou dicionário.
"""

print(list(zip1))
print(tuple(zip1))
print(set(zip1))

"""
Em lista, ele fez uma lista de tuplas com os elementos de índices correspondentes entre sí encaixados dentro das tuplas.
Depois do primeiro uso, os dados são apagados.
"""

print('Formando outros iteráveis ----------------------------------------------------------dict(zip([1, 2, 3], "abc"))')

zip_tupla = zip(lista1, lista2, 'abc')
print(tuple(zip_tupla))

zip_set = zip(lista1, lista2, 'abc')
print(set(zip_set))

zip_dict = zip(lista1, 'abc')  # chave/valor
print(dict(zip_dict))

# Outra forma
print(dict(zip([1, 2, 3], "abc")))

print('Elementos sobrantes ---------------------------------------------------------------------zip(1, [2, 3], [4, 5])')

lista3 = [7, 8, 9, 10, 11]

zip2 = zip(lista1, lista2, lista3)
print(list(zip2))

"""
Não será impresso os elementos sobrantes da lista3.

OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver trabalhando com
iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.
"""

print('Podemos utilizar diferentes iteráveis com zip ---------------------------zip(tupla, lista, dicionario.values())')

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14}

zip_final = zip(tupla, lista, dicionario.values())
print(list(zip_final))

zip_final = zip(tupla, lista, dicionario.keys())
print(list(zip_final))

print('Utilizando o desempacotador -----------------------------------------------------------------------------*dados')

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""
O * serve para desempacotar.
"""

print('Tirando valores específicos -----------{dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}')

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

"""
Isso vai imprimir um dicionario com o nome dos alunos e a maior nota de cada um deles.
"""

# Podemos usar o map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

"""
Entenda cada uma dessas partes para entender o que está sendo feito, se for preciso, vá executando parte por parte.
"""

print('Exercício 1 ------------------------------------------------------[x + y for x, y in list(zip(lista1, lista2))]')

"""
Considere duas listas de números, lista1 e lista2, cada uma com pelo menos 5 elementos. Escreva um programa que utilize 
a função zip para criar uma nova lista que contenha a soma dos elementos correspondentes das duas listas originais.
"""

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]

nova_lista = list(zip(lista1, lista2))

somas = []

for tupla in nova_lista:
    somas.append(tupla[0] + tupla[1])

print(somas)

# Jeito mais fácil
somas2 = [x + y for x, y in list(zip(lista1, lista2))]
print(somas2)

print('Exercício 2 ---------------------------------------------------------------------------dict(zip(nomes, idades))')

"""
Você tem uma lista de nomes e uma lista de idades. Escreva um programa que utilize a função zip para criar um 
dicionário onde as chaves são os nomes e os valores são as idades correspondentes.
"""

nomes = ['André', 'Bruno', 'Carlos', 'Daniel', 'Eduardo']
idades = [23, 32, 56, 32, 29]

equipe = dict(zip(nomes, idades))
print(equipe)

print('Exercício 3 -------------------------------------------f"O triangulo {triangulo[0]} tem medidas: {triangulo[1]}')

"""
Considere uma lista de comprimentos de lados de triângulos e uma lista de seus respectivos tipos (equilátero, isósceles, 
escaleno). Escreva um programa que utilize a função zip para criar um dicionário onde as chaves são os tipos de 
triângulos e os valores são listas dos comprimentos dos lados correspondentes.
"""

tipos_de_triangulos = ['equilátero', 'isoceles', 'escaleno']
medida_dos_lados = [(4, 4, 4), (5, 5, 3), (3, 4, 5)]

triangulos = list(zip(tipos_de_triangulos, medida_dos_lados))

for triangulo in triangulos:
    print(f'O triangulo {triangulo[0]} tem medidas: {triangulo[1]}')
