"""
TRABALHANDO COM MÓDULOS BUILT-IN

São módulos integrados, ou seja, que já vem instalado no Python. Mas precisamos fazer o import, assim como o random.
Utilizando alias (apelidos) para módulos/funções.
"""

# alias

import random as rdm

print(rdm.random())

"""
Podemos importar todas as funções de um módulo utilizando um *.
"""

from random import *

print(random())

"""
Dessa maneira não precisa colocar o "random."
"""

print('Apelidos para funções --------------')

from random import randint as rdi

print(rdi(5, 10))

from random import randint as rdi, random as rdm

print(rdi(5, 10))
print(rdm())

"""

"""

# Costumamos usar tuple para colocar multiplos imports de um mesmo módulo. Para ficar mais organizada que um monte de
# vírgula.

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(1, 10))
lista = [range(1, 20)]
shuffle(lista)
print(choice('Geek'))

# Chapei e fiz isso daqui:
fator = int(input('Digite um número para ver o seu fatorial: '))
resultado = 1


def verificar_valor_inteiro(entrada):
    try:
        return int(entrada)
    except ValueError:
        return f'"{entrada}" não é um valor possível de fazer o seu fatorial.'


valor_verificado = verificar_valor_inteiro(fator)

for valor in range(1, fator + 1):
    resultado = resultado * valor

print(f'{fator}! é igual a {resultado}, pois vamos multiplicar: ')

for n in tuple(reversed(range(2, fator + 1))):
    print(n, end=' * ')
print(1)
