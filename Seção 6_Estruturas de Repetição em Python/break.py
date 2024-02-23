"""
SAINDO DO LOOP COM BREAKS

Funciona da mesma forma que na linguagem C ou em Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

import random

print('Utilizando o break -----------------------------------------------------------------------if numero == 6: break')

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

print('Saiu do loop')

"""
Nesse loop o que está sendo passado é de que quando o loop chegar ao 6 ele acaba.
"""

print('Break no loop while-----------------------------------------------------------------if comando == "sair": break')

while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break

print('Exercício 1 ------------------------')

"""
Crie um programa que solicite ao usuário que digite números inteiros positivos. Utilize um loop para ler esses números 
até que o usuário digite um número negativo. Quando o número negativo for digitado, o programa deve imprimir a soma de 
todos os números positivos digitados antes do número negativo.
"""

numeros = []
numero = int(input('Digite um numero positivo para soma ou um negativo para sair: '))

while numero >= 0:
    numeros.append(numero)
    numero = int(input('Digite um numero positivo para soma ou um negativo para sair: '))

if numeros:
    print('Soma dos números positivos:', sum(numeros))
else:
    print('Nenhum número positivo foi digitado.')

print('Exercício 2 ----------------------------------')

"""
Desenvolva um jogo simples em que o computador gera um número aleatório entre 1 e 100, e o jogador tem que adivinhar 
qual é o número. Utilize um loop while para permitir que o jogador faça várias tentativas. O jogo deve fornecer dicas 
como "Muito alto" ou "Muito baixo" após cada tentativa. O loop deve ser interrompido quando o jogador acertar o número.
"""

numero_aleatorio = int(random.randint(1, 100))
print(numero_aleatorio)

numero_escolhido = int(input('Escolha um número: '))

while numero_aleatorio != numero_escolhido:
    if numero_escolhido > numero_aleatorio:
        print('Menos')
        numero_escolhido = int(input('Escolha outro número: '))
    elif numero_escolhido < numero_aleatorio:
        print('Mais')
        numero_escolhido = int(input('Escolha outro número: '))

print('Parabéns, Você acertou!')

print('Exercício 3 ---------------------------------')

"""
Crie um programa que simule um caixa eletrônico. O usuário deve fornecer o valor que deseja sacar. O caixa eletrônico 
possui notas de 100, 50, 20, 10, 5 e 2 reais. O programa deve calcular a quantidade mínima de notas necessárias para 
fornecer o valor solicitado, levando em consideração a disponibilidade de notas no caixa eletrônico. Utilize um loop 
para verificar se é possível fornecer o valor solicitado com as notas disponíveis. Se não for possível, o programa deve 
informar ao usuário.
"""

valor_saque = int(input("Digite o valor que deseja sacar: "))

notas_disponiveis = {100: 10, 50: 10, 20: 10, 10: 10, 5: 10, 2: 10}

notas_entregues = {}

for nota in sorted(notas_disponiveis.keys(), reverse=True):
    quantidade_notas = valor_saque // nota
    if quantidade_notas > 0 and quantidade_notas <= notas_disponiveis[nota]:
        notas_entregues[nota] = quantidade_notas
        valor_saque -= quantidade_notas * nota
        notas_disponiveis[nota] -= quantidade_notas

if valor_saque == 0:
    print("Notas entregues:")
    for nota, quantidade in notas_entregues.items():
        print(f"{quantidade} nota(s) de {nota} reais")
else:
    print("Não é possível fornecer o valor solicitado com as notas disponíveis.")

"""
Esse último exercício contém elementos que eu ainda não estudei, mas vou deixar esse exercício aqui para estuda-lo 
mais adiante.
"""
