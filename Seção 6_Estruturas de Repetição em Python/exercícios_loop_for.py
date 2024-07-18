"""
EXERCÍCIOS COM LOOP FOR

Devido a dificuldade que venho tendo para desenvolver essa matéria, resovi que preciso praticar mais e para tanto fiz
essa lista de exercícios para praticar.
"""

# from functools import reduce
# import operator

print('Exercício 1 --------------------------------------')

"""
Contagem Simples:

Escreva um programa que utilize um loop FOR para imprimir os números de 1 a 5.
"""

for numero in range(1, 6):
    print(numero)

print('Exercício 2 ---------------')

"""
Tabuada:

Crie um programa que peça ao usuário para inserir um número e, em seguida, use um loop FOR para imprimir a tabuada desse 
número, indo de 1 a 10.
"""

numero_escolhido = int(input('Insira um número para ver a sua tabuada: '))

tabuada = range(1, 11)

for numero in tabuada:
    print(f'{numero_escolhido} x {numero} = {numero_escolhido * numero}')

print('Exercício 3 -----------------------------------')

"""
Soma dos Pares:
Elabore um programa que calcule e imprima a soma dos números pares de 1 a 10 utilizando um loop FOR.
"""

numeros = list(range(1, 11))

numeros_pares = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f'A soma dos números pares de {numeros[0]} até {numeros[-1]} é {sum(numeros_pares)}')

print('Exercício 4 ----------------------------------')

"""
Caracteres Separados:
Dada a string "PYTHON", crie um programa que utilize um loop FOR para imprimir cada caractere em uma linha separada.
"""

python = list('PYTHON')

for letra in python:
    print(letra)

print('Exercício 5 --------------------------------------')

"""
Multiplos de 3:
Desenvolva um programa que utilize um loop FOR para imprimir os múltiplos de 3 no intervalo de 1 a 20.
"""

numeros = list(range(1, 20))

multiplos_3 = []

for numero in numeros:
    if numero % 3 == 0:
        multiplos_3.append(numero)

print(f'Os multiplos de 3 são: {tuple(multiplos_3)}')

print('Exercício 6 ----------------------')

"""
Calculadora de Média:
Solicite ao usuário que insira 5 notas. Utilizando um loop FOR, calcule e imprima a média dessas notas.
"""

notas = []

nota_aluno = int(input('Insira a nota de um aluno: '))
notas.append(nota_aluno)

for nota_aluno in notas:
    if len(notas) < 5:
        nota_aluno = int(input('Insira outra nota: '))
        notas.append(nota_aluno)

print(f'A média da sala é: {sum(notas) / len(notas)}')

print('Exercício 7 ----------------------------')

"""
Reverso:
Peça ao usuário para digitar uma palavra e, em seguida, utilize um loop FOR para imprimir a palavra de trás para frente.
"""

"""
palavra = list(input('Digite uma palavra para vê-la ao contrário: '))

for letra in palavra:
    print(letra[letra])
    letra -= 1

# print(palavra[::-1])
"""

print('Exercício 8 ------------------------------')

"""
Conversor de Temperatura:
Crie um programa que converta e imprima a temperatura de graus Celsius para Fahrenheit. O programa deve iterar de 
0 a 100 graus Celsius em intervalos de 10.
"""

temperaturas = list(range(0, 101))

for temperatura in temperaturas:
    if temperatura % 10 == 0:
        print(f'{temperatura}° C equivale a {temperatura * 1.8 + 32} °F')

print("Exercício 9 ------------------------------------------")

"""
Fatorial:
Implemente um programa que solicite ao usuário para inserir um número inteiro e, em seguida, utilize um loop FOR para 
calcular e imprimir o fatorial desse número.
"""

numero_escolhido = int(input('Escreva um numero inteiro para ver o seu valor fatorial: '))

fatorial = list(range(numero_escolhido, 1, -1))

fatorando = []

# fatorando.append(numero_escolhido)

for numero in range(numero_escolhido, 1, -1):
    fatorando.append(numero * numero - 1)

print(fatorando)
# print(f'O fatorial de {numero_escolhido} é {reduce(operator.mul, fatorando)}')
