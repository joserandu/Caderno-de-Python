"""
ANY E ALL

São funções integradas, diferente da reduce.

All: retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
"""

print('Funcionamento do all -------------------------------------------------------------------------all([1, 2, 3, 4])')

print(all([1, 2, 3, 4]))
print(all([0, 1, 2, 3, 4]))  # 0 = False
print(all([]))

"""
Poderia ser um set, string, qualquer iterável.
"""

print('Uso prático --------------------------------------------------------------all(nome[0] == "C" for nome in nomes)')

nomes = ['Carlos', 'Camila', 'Carla', 'Cristiana', 'Cristina']
nomes2 = ['Carlos', 'Camila', 'Carla', 'Cristiana', 'Cristina', 'Daniel']

print(all(nome[0] == 'C' for nome in nomes))
print(all(nome[0] == 'C' for nome in nomes2))

print('Utlizando if -----------------------------------------------all([letra for letra in "eio" if letra in "aeiou"])')

print(all([letra for letra in 'eio' if letra in 'aeiou']))
print(all([letra for letra in 'jklç' if letra in 'aeiou']))

"""
No segundo caso, a expressão gera uma lista vazia [] porque nenhuma letra em 'jklç' está presente em 'aeiou'. E como 
não há elementos na lista, all([]) retorna True, pois não há elementos para verificar e, portanto, a condição é 
verdadeira.
"""

print('Utilizando list comprehension ----------------------------------all([num for num in [2, 4, 7] if num % 2 == 0])')

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print('')

print('Any() =========================================================================================================')

print('')

print('funcionamento do any -------------------------------------------------------------------------any([0, 1, 2, 3])')

"""
Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))

"""
Vai retornar True porque do 1 em diante é verdadeiro.
"""

print(any([0, False, {}]))

print('Utilizando o loop for -----------------------------------any([num for num in [4, 2, 10, 6, 8] if num % 2 == 1])')

print(any(nome[0] == 'C' for nome in nomes))

print(any([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))

print('Exercício 1 ------------------------------------------------------------------------------------all([1, 2, ""])')

"""
Complete as seguintes afirmações com True ou False, considerando o funcionamento da função all:

a) all([3, 5, 0, 8]) retorna __False__.
b) all([True, True, True]) retorna __True__.
c) all([1, 2, ""]) retorna __False__.
"""

print('Exercício 2 ----------------------------------------------------any([nome for nome in nomes if nome[0] == "M"])')

"""
Dada a lista de nomes a seguir, crie uma expressão utilizando a função any para verificar se há algum nome que começa 
com a letra "M".

nomes = ['Maria', 'Pedro', 'Mariana', 'Lucas', 'Ana']
"""

nomes = ['Maria', 'Pedro', 'Mariana', 'Lucas', 'Ana']

print(any([nome for nome in nomes if nome[0] == 'M']))

"""
Poderia ser também:
any(nome.startswith('M') for nome in nomes)
"""

print('Exercício 3 ---------------------------------------------any([numero for numero in numeros if numero % 2 == 0])')

"""
Crie uma expressão utilizando a função all para verificar se todos os números em uma lista são pares.

numeros = [2, 4, 6, 8, 10]
"""

numeros = [2, 4, 6, 8, 10]

print(all([numero for numero in numeros if numero % 2 == 0]))

"""
Poderia ser também:
all(num % 2 == 0 for num in numeros)
"""
