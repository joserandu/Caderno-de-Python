"""
REVERSED

Não confunda com a função reverse() que estudamos na Seção de listas.
"""

print('Relembrando reverse() ---------------------------')

lista = [1, 2, 3, 4, 5]

lista.reverse()
print(lista)

"""
Repare que essa é uma função exclusiva para as listas, Já a reversed() funciona com qualquer iterável.
"""

print('O tipo de objeto -----------------------------------------')

res = reversed(lista)
print(res)

"""
A função reversed() retorna um iterável chamado List Reverse Iterator
"""

"""
Podemos converter o elemento retornado para uma lista, tupla ou conjunto.
"""

lista = [1, 2, 3, 4, 5]

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Set (sem ordem)
print(set(reversed(lista)))

# Iterando sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')

"""
O end= serve para indicar o que será colocado no espaçamento entre cada elemento da lista, sendo assim, como passamos 
uma string vazia, não haverá quebra de linha.
"""

# Podemos fazer o mesmo sem o uso do for

print('\b')
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso com o slicing de strings

print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(1, 11)):
    print(n)

# Apesar de que também já vimos como fazer isso utilizando o próprio range()
for n in range(10, -1, -1):
    print(n)
