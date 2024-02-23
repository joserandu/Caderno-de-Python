"""
LOOP WHILE

A forma geral:

while <expressão_booleana>:
    // execução do loop

O bloco do while será repetido enquando a expressão booleana for verdadeira.
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.
"""

import random

numero = 1

while numero < 10:
    print(numero)
    numero += 1

"""
Lembre-se que a impressão fica no meio da expressão e do critério de parada.
numero += 1 quer dizer que numero = numero + 1, igual no JavaScript. É um valor que com a repetição da lógica ele 
acaba se iterando enquanto a expressão booleana for verdadeira.
"""

print('Usando loop While com input -----------------------------------------------------------while resposta != "sim":')

"""
Obs: em um loop while, é importante que cuidemos do critério de parada. No caso aqui, o critério de parada é o while 
não ser mais verdadeiro.
IMPORTANTE: Se cair em um loop infinito sem querer, aperte em stop no lado do run (CTRL + F2).

Loops infinitos são importantes em jogos.
"""

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

"""
A lógica aqui é que enquanto não ser respondido sim no input, o loop continua. Isso pode ser muito utilizado na 
construção de jogos.
"""

print('Exercício 1 -----------------------')

"""
Elabore um programa utilizando um loop while que conte de 1 a 5 e exiba cada número durante a iteração. Ao final, 
imprima uma mensagem indicando que o loop foi concluído.
"""

numero = 1

while numero < 6:
    print(numero)
    numero += 1

print('O loop foi concluído.')

print('Exercício 2 ----------------------------------')

"""
Crie um programa que simule um jogo de adivinhação. O computador escolherá um número aleatório entre 1 e 100, e o 
jogador tentará adivinhar. Utilize um loop while para permitir que o jogador faça múltiplas tentativas. Forneça dicas ao
jogador sobre se o número é maior ou menor do que a tentativa atual. O jogo deve continuar até que o jogador adivinhe 
corretamente ou decida sair digitando 'sair'. Ao final, exiba o número de tentativas feitas pelo jogador e uma mensagem 
de parabenização se ele adivinhar corretamente.
"""

""""
print('Adivinhe qual é o número de um a cem! \n')

numero_aleatorio = int(random.randint(1, 100))

resposta = int(input('De zero a 100, qual é o número?'))

while resposta != numero_aleatorio:
    if resposta > numero_aleatorio:
        resposta = int(input('Menos, \n Qual é o número?:'))
    elif resposta < numero_aleatorio:
        resposta = int(input('Mais, \n Qual é o número?:'))

print('Acertou')
"""

# Resposta

numero_secreto = random.randint(1, 100)

tentativas = 0
adivinhou = False

print("Bem-vindo ao jogo de adivinhação!")

while not adivinhou:
    tentativa = int(input("Tente adivinhar o número (ou digite 'sair' para sair): "))

    if tentativa == numero_secreto:
        adivinhou = True
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")

    tentativas += 1

    if tentativa == 'sair':
        print(f"O número secreto era {numero_secreto}. Você desistiu após {tentativas} tentativas.")
        break

"""
Esse exemplo do mano GPT foi bem mais complexo do que eu imaginava para o momento, mas eu consegui absorver algumas 
coisas. Leia com atenção esse código. No meu código, que está comentado logo acima, eu consegui fazer a estrutura 
base do jogo, mas não consegui contar as tentativas por puro desconhecimento de uma estrutura complexa de um loop 
while, fica para uma próxima.
O que mais me incomodou foi que o código dá erro ao escrever sair, pois é uma string e não pode ser convertida para int.
Para resolver tal problema com muita classe pode ser usado os métodos de tratamento de erros, que ainda não aprendi, 
mas quando aprender eu volto com esse tipo de exercício. Mas fica muito bonito:

numero_secreto = random.randint(1, 100)
tentativas = 0
adivinhou = False

print("Bem-vindo ao jogo de adivinhação!")

while not adivinhou:
    tentativa = input("Tente adivinhar o número (ou digite 'sair' para sair): ")

    if tentativa.lower() == 'sair':
        print(f"Você desistiu após {tentativas} tentativas. O número secreto era {numero_secreto}.")
        break

    # Verifica se a entrada pode ser convertida para inteiro
    try:
        tentativa = int(tentativa)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if tentativa == numero_secreto:
        adivinhou = True
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    elif tentativa > numero_secreto:
        print("Tente um número menor.")

    tentativas += 1
"""
