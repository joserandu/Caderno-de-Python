"""
REDUCE

OBS: A partir do python versão 3+ a função reduce não é mais uma função integrada (built-in). Ou seja, agora temos
que importar e utilizar essa função a partir do módulo 'functools'.

Guido Van Rossum (criador do Python): "Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes, um loop for é mais legível."

Para entender o reduce:
- Imagine que você tem uma coleção de dados:
dados = [a1, a2, ... an]

e você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map() e filter() a função reduce() recebe dois parâmtros: a função e o iterável:

reduce(funcao, iterável)

A função reduce funciona da seguinte forma:
    Passo 1: resultado1 = f(a1, a2) -> aplica a função nos dois primeiros elementos da função e guarda o resultado.
    Passo 2: resultado2 = f(resultado1, a3) -> aplica a função passando o resultado do passo1 mais o terceiro
    elemento e guarda o resultado.

    Isso é repetido até o final.

    Passo 3: resultado3 = f(resultado2, a4)
    .
    .
    .
    Passo n: resultadoN = f(resultado(n - 1), a)

    Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No
    final, reduce() irá retornar o resultado final.

Alternativamente poderiamos ver a função reduce como:

função(função(função(a1, a2), a3), a4), ...), an)
"""
from functools import reduce

print('Multiplicando todos os números de uma lista ----------------------------------reduce(lambda x, y: x * y, dados)')

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para usar o reduce precisamos de uma função que recebe dois parâmetros:

result = reduce(lambda x, y: x * y, dados)
print(result)

print('Utilizando um loop normal -------------------------------------------for n in dados / resultado = resultado * n')

resultado = 1
for n in dados:
    resultado = resultado * n

print(resultado)
