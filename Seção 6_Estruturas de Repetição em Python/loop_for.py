"""
LOOP FOR

LOOP: É uma estrutura de repetição
FOR: Uma dessas estruturas de repetição

Em Java:
for(int i = 9; i < 10; i++) {
    // execução do loop
}

Utilizamos loops para valores interáveis.
- String:
    nome = 'Geek University'
- Lista:
    lista = [1, 2, 3, 4]
- Range:
    numeros = range(1, 10)
    ele trás todos os números do intervalo menos o último.
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

print('For com String ------------------------------------------------------------------------------for letra in nome:')

for letra in nome:
    print(letra)

print('For em lista ------------------------------------------------------------------------------for numero in lista:')

for numero in lista:
    print(numero)

print('Iterando sobre um range -------------------------------------------------------------for numero in range(1, 10)')

numero: 2
for numero in range(1, 10):
    print(numero)

"""
Pode-se declarar variáveis do tipo int e do tipo float com :.
"""

print('Para saber a posição de um valor ----------------------------for indice, letra in enumerate(nome): nome[indice]')

nome = 'Geek University'

for indice, letra in enumerate(nome):
    print(nome[indice])

print(tuple(enumerate(nome)))

"""
O enumerate pega cada letra e cria uma tupla de tuplas: (0, 'G'), (1, 'e') ...
"""

print('Perguntando ao usuário quantas vezes o loop deve repetir ----------------------------for n in range(1, qtde+1):')

qtde = int(input('Quantas vezes esse loop deve rodar: '))

for n in range(1, qtde+1):
    print(f'Imprimindo {n} vez(es)')

"""
Colocamos o +1 para o número não ficar menor.
"""

print('Exemplo esquisito -----------------------------------------------------------num int(input()) soma = soma + num')

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('Imprimindo sem passar para a próxima linha -----------------------------------------------------------, end='' ')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

print('Multiplicando uma string -------------------------------------------------------------------------"string" * 30')

"""
Tabela de emolgis unicodes: https://apps.timwhitlock.info/emoji/tables/unicode
"""

for num in range(1, 5):
    print('\U0001F496' * num)

print('Exercício 1 --------------------------------------------')

"""
Crie um programa em Python que utilize um loop FOR para imprimir uma contagem regressiva a partir de um número fornecido
pelo usuário até 1. O programa deve pedir ao usuário que insira um número inteiro positivo e, em seguida, imprimir a 
contagem regressiva, finalizando com "Fogo!".
"""

primeiro_numero = int(input('Digite um número para que possa ser feito a contagem regressiva: '))

for numero in range(primeiro_numero, 0, -1):
    print(numero)

print('Fogo!')

print('Exercício 2 --------------------------------------')

"""
Utilizando o conceito de loop FOR e a função enumerate, crie um programa que percorra a lista fornecida abaixo e imprima 
cada elemento juntamente com sua posição no formato "Posição: Elemento". A lista é a seguinte: ['Maçã', 'Banana', 
'Morango', 'Abacaxi', 'Uva'].

Dica: Utilize a função enumerate para obter tanto o índice quanto o valor durante a iteração.
"""

lista_fruta = ['Maça', 'Banana', 'Morango', 'Abacaxi', 'Uva']

for indice, fruta in enumerate(lista_fruta):
    print(f'{indice + 1}: {fruta}')
