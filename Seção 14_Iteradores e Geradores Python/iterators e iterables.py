"""
ENTENDENDO ITERATORS E ITERABLES (iterável)

ITERATOR -> é um objeto da programação que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

ITERABLE -> Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""

# Exemplos de iterable (Não são um iterator)
nome = "Geek"
numeros = [1, 2, 3, 4, 5, 6]
numeros2 = 1, 2, 3, 4, 5, 6

# Iterators
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

print("Utilizando loop ---------------------------------------------")

for letra in nome:
    print(f"{letra}")
