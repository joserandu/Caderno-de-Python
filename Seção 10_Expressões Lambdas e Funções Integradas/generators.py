"""
GENERATORS

Em aulas anteriores nós estudamos list comprehension, dictionary comprehension, Set comprehension. Mas não vimos
Tuple comprehension, e não vimos porque elas se chamam generators.

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']
print(any([nome[0] == 'c' for nome in nomes])
Poderiamos ter usado generators
"""

from sys import getsizeof

"""
Foi importado essa biblioteca para podermos usar a função getsizeof para vermos o quanto bytes alguns elementos do 
código ocupam a memória.
"""

print('Sitaxe ----------------------------------------------------------------------(nome[0] == "C" for nome in nomes)')

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

"""
Se colocasse chaves any([]), ficaria uma list comprehension, e imprimiria uma lista de valores booleanos.

Assim como map() e filter(), a partir do uso, o resultado é apagado da memória.
"""

print('Comparando list comprehension com generator ---------------------------[] != (nome[0] == "C" for nome in nomes)')

# list comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

"""
Se você só precisa saber se tem algo em uma lista, o generator é mais performático, pois não vai formar um valor
de lista, ocupando menos espaço em memória.
"""

print('Medindo os bytes de um elemento do código ----------------------------------------------------------getsizeof()')

print(getsizeof('Geek'))

"""
Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
Nesse caso mostra quantos bytes a string "geek" está ocupando na memória.
"""

print(getsizeof(9))

print(getsizeof(9087654))

print(getsizeof(True))

print(getsizeof(res))

print('Gerando uma lista de números com diferentes tipos de compreensions -----------------x * 10 for x in range(1000)')

list_comprehension = getsizeof([x * 10 for x in range(1000)])

set_comprehension = getsizeof({x * 10 for x in range(1000)})

dict_comprehension = getsizeof({x: x * 10 for x in range(1000)})

generator = getsizeof(x * 10 for x in range(1000))

print('\nPara fazer a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comprehension} bytes')
print(f'Set Comprehension: {set_comprehension} bytes')
print(f'Dict Comprehension: {dict_comprehension} bytes')
print(f'Generator Expression: {generator} bytes')

"""
Veja que a diferença é gritante.
Essa função é interessante para conseguir mais performace porque essa é uma informação que é usada e logo se apaga, 
agora list, dict e set são dados que persistem até o final do programa.
"""

print('Iterando no generator expression ---------------------------------------------------(x * 10 for x in range(10))')

generator2 = (x * 10 for x in range(10))
print(type(generator2))

for num in generator2:
    print(num)

print('Exercício 1 ------------------------------------------------------------------for numero in generator_quadrado:')

"""
Considere a lista de números abaixo:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crie um generator expression que gere uma nova lista contendo o quadrado dos números pares dessa lista. Em seguida, 
itere sobre o generator e imprima cada elemento gerado.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

generator_quadrado = (x ** 2 for x in numeros if x % 2 == 0)

for numero in generator_quadrado:
    print(numero)

print('Exercício 2 ------------------(palavra for palavra in palavras if palavra[0] == "j") / print(list(generator_j))')

"""
Dada a lista de palavras abaixo:

palavras = ['python', 'java', 'csharp', 'javascript', 'typescript']
Utilize um generator expression para criar uma nova lista que contenha apenas as palavras que começam com a letra 'j'. 
Em seguida, imprima a lista gerada.
"""

palavras = ['python', 'java', 'csharp', 'javascript', 'typescript']

generator_j = (palavra for palavra in palavras if palavra[0] == 'j')

print(list(generator_j))

"""
Eu tinha usado um loop e um .append() para montar essa lista, mas utilizando a função list() acaba ficando mais fácil.
"""

print('Exercício 3 -----------------------------------------------------------------------(n * i for i in range(1, 6))')

"""
Crie uma função chamada multiplicacao_infinita que receba um número como parâmetro e retorne um generator expression 
que gere uma sequência infinita de múltiplos desse número. Em seguida, utilize um loop para imprimir os primeiros 5 
elementos gerados por essa expressão.

def multiplicacao_infinita(numero):
    # Seu código aqui
"""


def multiplicacao_infinita(n):
    return (n * i for i in range(1, 6))


resultado_generator = multiplicacao_infinita(3)

for resultado in resultado_generator:
    print(resultado)
<<<<<<< HEAD
 
=======
>>>>>>> 8db86c2 (Venv)
