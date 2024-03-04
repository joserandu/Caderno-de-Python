"""
LEN, ABS, SUM e ROUND

len() - retorna o número de items de um iterável.
abs() - retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real e positivo.
sum() - recebe como parâmetro um iterável podendo receber um valor inicial, e retorna a soma total dos elementos.
round() - retorna um número arredondado para n digitos de precisão após cada casa decimal. Se a precisão não for
informada, retorna o inteiro mais próximo da entrada.
"""

print('Revisando o len ------------------------------------------------------------------------------len(range(1, 10))')

print(len('Geek University'))
print(len(range(1, 11)))

"""
Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
"""

print('Geek University'.__len__())

"""
Toda função python que começa com __ se chama Dunder e o nome da função, nesse caso, Dunder len.
"""

print('a função abs()----------------------------------------------------------------------------------------abs(-3.4)')

print(abs(-5))
print(abs(5))
print(abs(-3.4))

"""
A função abs não funciona com string.
"""

print('A função sum ------------------------------------------------------------------------------sum([1, 2, 3, 4], 5)')

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 6))  # Vai somar o 6 também.

"""
Isso pode servir para calcular o valor total com o frete de uma lista de produtos.
E podemos usar com qualquer iterável.
"""

# Em um dicionário
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

print('Função round() --------------------------------------------------------------------------round(10.000000000051)')

print(round(10.2))
print(round(10.5))
print(round(10.5000000000000000000000000000001))
print(round(10.6))
print(round(10.21221212121212, 2))
print(round(1.2199999999999, 20))

print('Exercício 1 ------------------------------------------------------------------------------------print(abs(-10))')

"""
Exercício 1:

1 - Qual é o resultado da função len() quando aplicada à string 'Hello World'?
    R: 11
2 - Utilizando a função abs(), encontre o valor absoluto de -10.
3 - Escreva uma expressão usando a função sum() que calcule a soma dos números de 1 a 100.
"""

# Item 2
print(abs(-10))

# Item 3
print(sum(range(1, 101)))

print('Exercício 2 ---------------------------------------------------------------------------------------------------')

"""
Complete as seguintes afirmações:

1 - A função len() retorna o número de ___elementos___ de um iterável.
2 - A função round() retorna um número arredondado para _2_ dígitos de precisão após cada casa decimal.
3 - A função sum() recebe como parâmetro um iterável e retorna a ___soma___ total dos elementos.
"""

print('Exercício 3 --------------------------------------------------------round(horas_trabalhadas * taxa_por_hora, 2)')

"""
Escreva uma função em Python chamada calcular_pagamento que aceite dois parâmetros: horas_trabalhadas e taxa_por_hora. 
Esta função deve calcular o pagamento do trabalhador multiplicando o número de horas trabalhadas pela taxa por hora e 
retornar o resultado. Certifique-se de que o resultado retornado esteja arredondado para duas casas decimais.
"""


def calcular_pagamento(horas_trabalhadas, taxa_por_hora):
    return round(horas_trabalhadas * taxa_por_hora, 2)


total_de_horas = 5
taxa = 80.2588

print(f'O total a ser pago pelo serviço é de R${calcular_pagamento(total_de_horas, taxa)}')
