"""
RECEBENDO DADOS DO USUÁRIO
"""

# Entrada de dados
print('Qual seu nome?')
nome = input()

# Processamento

# saída de dados

print(f'Seja bem-vindo(a) {nome}')
print('Qual sua idade?')
idade = input()
print(f'O(a) {nome} tem {idade} anos de idade')

print('Exercício 1 ---------------------------------------------------------------------------------------int(input())')

"""
Escreva um programa em Python que solicite ao usuário que digite dois números inteiros e, em seguida, exiba a soma 
desses dois números.

Dica:

- Utilize a função input para receber os números do usuário.
- Converta os valores de entrada para inteiros usando int().
- Realize a soma dos dois números.
- Exiba o resultado.
"""

print('Digite um número:')
numero1 = int(input())

print('Digite outro número:')
numero2 = int(input())

print(f'A soma entre {numero1} e {numero2} é {numero1 + numero2}')

print('Exercício 2 -------------------------')

print('Deseja fazer uma operação adicional? (responda "sim" ou "não")')
resposta2 = input()

resposta = numero1 + numero2

if resposta2.lower() != 'sim':
    print('Programa encerrado. \nAté um outro dia.')
else:
    print('Escolha outro número:')
    outro_numero = int(input())
    print('Escolha uma operação: +, -, *, /.')
    operacao = input()
    if operacao == '+':
        resultado = resposta + outro_numero
        print(f'O resultado dessa operação é {resultado}')
    elif operacao == '-':
        resultado = resposta - outro_numero
        print(f'O resultado dessa operação é {resultado}')
    elif operacao == '*':
        resultado = resposta * outro_numero
        print(f'O resultado dessa operação é {resultado}')
    elif operacao == '/':
        resultado = resposta / outro_numero
        print(f'O resultado dessa operação é {resultado}')
