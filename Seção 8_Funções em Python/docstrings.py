"""
DOCUMENTANDO FUNÇÕES COM DOCSTRINGS

A partir do momento que escrevemos um código, precisamos fazer uma documentação, ou seja anotações para facilitar a
análise do código. É a famosa anotação reta e direta. Com certeza, não é como eu faço aqui, posto que eu estou
fazendo anotações de aprendizado, não de debug.
"""

print('Acessando as anotações de uma função ------------------------------------------------------------------.__doc__')


def diz_oi():
    """Repare nessa anotação sendo impressa"""
    return 'Oi '


print(diz_oi())
print(diz_oi.__doc__)  # sem parêntesis.

"""
Essa PROPRIEDADE __doc__ serve para ver as anotações DENTRO da função.
"""

print('Fazendo acesso a documentação utilizando a função help() -------------------------------def exp(b, p): """xx"""')


def exponencial(base, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a potência informada.
    :param base: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: retorna o exponencial de 'numero' por 'potência'.
    """
    return base ** potencia


print(exponencial(5))

"""
No momento em que se declara a função, abrindo aspas triplas e apertando enter já aparece os param (parâmetro) e o 
return, em formato de anotação.
"""

print('Exercício 1 --------------------------------')

"""
Crie uma função chamada calculo_media que recebe uma lista de números como parâmetro e retorna a média aritmética desses 
números. Documente a função utilizando docstrings para explicar o propósito da função, os parâmetros e o que ela 
retorna. Teste a função com uma lista de números.

# Exemplo de uso:
lista_numeros = [10, 15, 20, 25, 30]
resultado_media = calculo_media(lista_numeros)
print(resultado_media)  # Saída: 20.0
"""

lista_numeros = [10, 15, 20, 25, 30]


def calculo_media(lista):
    return sum(lista) / len(lista)


resultado_media = calculo_media(lista_numeros)
print(resultado_media)  # Saída: 20.0

print('Exercício 2 ---------------------------------')

"""
Crie uma função chamada verifica_par_impar que recebe um número como parâmetro e retorna uma string indicando se o 
número é par ou ímpar. Documente a função utilizando docstrings para explicar o propósito da função, o parâmetro e o que 
ela retorna. Teste a função com diferentes números.

# Exemplo de uso:
resultado1 = verifica_par_impar(7)
resultado2 = verifica_par_impar(14)
print(resultado1)  # Saída: 'Ímpar'
print(resultado2)  # Saída: 'Par'
"""


def verifica_par_impar(numero):
    if numero % 2 == 1:
        return f'{numero} é um número impar'
    return f'{numero} é um número par'


resultado1 = verifica_par_impar(7)
resultado2 = verifica_par_impar(14)
print(resultado1)  # Saída: 'Ímpar'
print(resultado2)  # Saída: 'Par'

print('Exercício 3 -----------------------------')

"""
Crie uma função chamada calcula_area_retangulo que recebe dois parâmetros, base e altura, e retorna a área de um 
retângulo. Documente a função utilizando docstrings para explicar o propósito da função, os parâmetros e o que ela 
retorna. Teste a função com diferentes valores para base e altura.

# Exemplo de uso:
area1 = calcula_area_retangulo(5, 10)
area2 = calcula_area_retangulo(8, 6)
print(area1)  # Saída: 50
print(area2)  # Saída: 48
"""


def calcula_area_retangulo(base, altura):
    """
    'base': medida de um dos lados de um retangulo
    'altura': medida de um lado adjacente ao da base
    'area': a area é dada pelo produto entre base e altura
    - Em python, a multiplicação é representada por '*'
    """
    return base * altura


area1 = calcula_area_retangulo(5, 10)
area2 = calcula_area_retangulo(8, 6)
print(area1)  # Saída: 50
print(area2)  # Saída: 48
print(calcula_area_retangulo.__doc__)
