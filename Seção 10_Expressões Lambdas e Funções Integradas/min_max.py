"""
MIN E MAX

Já vimos antes essas funções, mas é bom revisar

Max() retorna o maior valor em um iterável ou o maior em dois ou mais elementos.
Min() retorna o menor valor em um iterável ou em dois ou mais elementos.
"""

print('Relembando as funções Max e min --------------------------------------------------------------------max() min()')

lista = [1, 2, 5, 2, 63, 634, 484]
print(max(lista))
tupla = 1, 2, 5, 2, 63, 634, 484
print(max(tupla))
seter = {1, 2, 5, 2, 63, 634, 484}
print(max(seter))

print('Utilizando Max e min em dicionários ---------------------------------------------------max(dicionario.values())')

# Em dicionário é diferente
dictionary = {"a": 1, "b": 2, "c": 5, "d": 2, "e": 63, "f": 634, "g": 484}
print(max(dictionary.values()))
print(max(dictionary.keys()))

print('Trazendo dados do usuário --------------------------------------------------------------------{max(val1, val2)}')

print(max(1, 6))

"""
Faça um programa que receba dois valores do usuário e mostre o maior.
"""

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f"O maior valor é {max(val1, val2)}")

# Podemos colocar quantos valores nós quisermos.

print(max('a', 'ab', 'abc'))
print(max('g', 'h', 't'))

"""
Nem preciso dizer essa função aceita números do tipo float.
"""

print('Min -------------------------------------------------------------------------------------------------min(lista)')

lista = [1, 2, 5, 2, 63, 634, 484]
print(min(lista))
tupla = 1, 2, 5, 2, 63, 634, 484
print(min(tupla))
conjunto = {1, 2, 5, 2, 63, 634, 484}
print(min(conjunto))

print('Min em dicionários --------------------------------------------------------------------min(dicionario.values())')
# Em dicionário é diferente
dictionary = {"a": 1, "b": 2, "c": 5, "d": 2, "e": 63, "f": 634, "g": 484}
print(min(dictionary.values()))
print(min(dictionary.keys()))

print('Trazendo dados do usuário com min() ------------------------------------------------------------min(val1, val2)')

print(min(1, 6))

"""
Faça um programa que receba dois valores do usuário e mostre o maior.
"""

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(f"O maior valor é {min(val1, val2)}")

# Podemos colocar quantos valores nós quisermos.

print(min('a', 'ab', 'abc'))
print(min('g', 'h', 't'))

"""
nem preciso dizer essa função aceita números do tipo float.
"""

print('Ordenação de strings com max e min----------------------------------------max(nomes, key=lamba nome: len(nome))')

nomes = ['Mc Kevin', 'Mc Bruninho da Baixada', 'Mc Ig']

print(max(nomes))
print(min(nomes))

"""
Aqui não vai ser a maior string, será em ordem alfabética.
"""

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

"""
Mudamos a lógica da função max e min porque a função max() é escrita assim:


def max(*args, key=None): # known special case of max  <------
   
    "
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
    "
    pass
"""

print('Max e min em dicionários -------------------------------max(musicas, key=lambda musica1: musica1["reproduções])')

musicas = [
    {"título": "Vida Loka", "reproduções": 1234710},
    {"título": "Vida Loka pt.2", "reproduções": 23098457043},
    {"título": "Fórmula mágica da paz", "reproduções": 1093285643},
    {"título": "Diário de um detento", "reproduções": 1948243},
]

"""
A partir daqui eu mudei de musica para música1 e musica2 por conta de já terem sido declaradas em outro escopo e 
informar correção da PEP8
"""

print(max(musicas, key=lambda musica1: musica1['reproduções']))
print(min(musicas, key=lambda musica1: musica1['reproduções']))

print('Imprimindo somente o título -------------------max(musicas, key=lambda musica: musica["reproducoes"])["titulo"]')

"""
Imprimir somente o título da música
"""

print(f'A música mais tocada é {max(musicas, key=lambda musica2: musica2["reproduções"])["título"]}')
print(f'A música menos tocada é {min(musicas, key=lambda musica2: musica2["reproduções"])["título"]}')

# Desafio 2

"""
Como fazer esse processo todo sem o max e sem o min.
No dia a dia, em python pelo menos, você não vai precisar fazer isso, mas a lógica é interessante.
"""

maximo = 0
for musica in musicas:
    if musica['reproduções'] > maximo:
        maximo = musica['reproduções']

for musica in musicas:
    if musica['reproduções'] == maximo:
        print(musica['título'])

minimo = 9999999999999999999999999

for musica in musicas:
    if musica['reproduções'] < minimo:
        minimo = musica['reproduções']

for musica in musicas:
    if musica['reproduções'] == minimo:
        print(musica['título'])

print('Exercício 1 -------------------------------------------------------------------max(primeiro, segundo, terceiro)')

"""
Comparação de valores
Escreva um programa que receba três números do usuário e mostre o maior e o menor número entre eles.

Exemplo de Saída:

Informe o primeiro número: 10
Informe o segundo número: 5
Informe o terceiro número: 8
O maior número é 10
O menor número é 5
"""

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

print(f'O maior número é o {max(primeiro, segundo, terceiro)}')
print(f'O menor número é o {min(primeiro, segundo, terceiro)}')

print('Exercício 2 ------------------------------------------------------max(nome1, nome2, key=lambda nome: len(nome))')

"""
Maior nome

Escreva um programa que receba uma lista de nomes do usuário e determine o nome mais longo e o nome mais curto da lista.

Exemplo de Saída:

Informe um nome: João
Informe um nome: Maria
Informe um nome: Ana Carolina
Informe um nome: Pedro
O nome mais longo é Ana Carolina
O nome mais curto é João
"""

nome1 = input('Cadastre o primeiro nome: ')
nome2 = input('Cadastre o segundo nome: ')
nome3 = input('Cadastre o terceiro nome: ')
nome4 = input('Cadastre o quarto nome: ')

print(f'O nome mais longo é {max(nome1, nome2, nome3, nome4, key=lambda nome: len(nome))}')
print(f'O nome mais curto é {min(nome1, nome2, nome3, nome4, key=lambda nome: len(nome))}')

print('Exercício 3 --------------------------------------max(playlist, key=lambda musica: musica["duração"])["título"]')

"""
Maior e menor duração de músicas

Considere uma lista de dicionários, em que cada dicionário representa uma música com seu título e duração em 
segundos. Escreva um programa que determine o título da música mais longa e o título da música mais curta dessa lista.

Exemplo de Saída:

A música mais longa é "Bohemian Rhapsody"
A música mais curta é "Yesterday"
"""

playlist = [
    {'titulo': 'Bohemian Rhapsody', 'duracao': 365},
    {'titulo': 'Yesterday', 'duracao': 130}
]

print(f'A música mais longa é {max(playlist, key=lambda musica1: musica1["duracao"])["titulo"]}')
print(f'A música mais curta é {min(playlist, key=lambda musica1: musica1["duracao"])["titulo"]}')
