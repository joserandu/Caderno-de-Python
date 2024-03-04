"""
MODULO RANDOM

- Os módulos nada mais são do que outros arquivos em Python.

O modulo random já é uma função integrada.

O modulo random possúi varias funções para a geração de números pseudoaleatórios.
    São gerados não tão aleatóriamente, pode haver repetições.

OBS: Existem duas formas de se utilizar um módulo ou função desse
"""

# Forma 1

# import random

"""
Ao realizar o import, importando todo o módulo. Ao realizar o import de todo o módulo, (ou seja só o , 
todas as funções, atributos, classes e propriedades que estiverem dentro do módulo ficaram disponíveis, 
em outras palavras, ficaram em memória. Então não é recomendado.
Caso você saiba quais funções você precisa utilizar desse módulo, então esta não seria a fórma ideal de utilização.
Se quiser saber quais são os módulos, no terminal escreva: dir(random), e para saber o que ele faz, utilize a função 
help().

Nós veremos uma forma melhor na forma 2.
"""

print('Forma mais aconselhável de importar a biblioteca -------------------------------------from random import random')

from random import random

"""
A função random() gera um número pseudoaleatório entre 0 e 1.
Veja que para utilizar a função random() no pacote random() nos colocamos o nome do pacote e o nome da função 
separados por ponto.
Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random é apenas uma função 
dentro do módulo random.
Para ver o código fonte do random = ctrl + clique no código fonte do random.
Se você fazer do primeiro jeito, você vai importar quase 800 linhas de código, deixando sua função mais lenta. Por 
isso, importe somente a função que você quer
"""

for i in range(0, 10):
    print(random())

"""
Repare que nessa forma recomendada não precisamos chamar novamente a coleção random().
Esse módulo é bastante usado em IA. Em redes neurais a gente usa bastante esse módulo random() para gerar pequenos 
valores.
"""

print('Função uniforme() --------------------------------------------------------------------------------uniform(3, 7)')

"""
Gerar um número real pseudoaleatório entre os valores estabelecidos.
"""

from random import uniform

for i in range(1, 7):
    print(uniform(3, 7))  # O número 7 não é incluido.


"""
Vai gerar numeros pseudo-aleatórios entre 3 e numeros menores que 7.
"""

print('Fazendo valores inteiros ------------------------------------------------------------------------randint(1, 61)')

from random import randint

for n in range(1, 6):
    print(randint(1, 61), end=', ')

print('\b')

"""
Infelizmente, acaba dando números repetidos.
"""

print('Choice() ---------------------------------------------------------------------------------------choice(jogadas)')

"""
O nome já diz tudo, é uma escolha.
Mostra um valor aleatório entre um iterável.
"""

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
print(choice('Geek University'))  # Imprime as letras.

print('Shuffle() --------------------------------------------------------------------------------------shuffle(cartas)')

from random import shuffle

"""
O nome também já é autoesplicativo.
Tem a função de embaralhar dados.
A semântica é diferente das funções normais, se colocar no print, da errado. Essa função altera a ordem inicial.
"""

cartas = ['K', 'Q', 'J', 'A', '1', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas)
# Para entregar a primeira:
print(cartas[0])

print('Exercício 1 ------------------------------------------randint(1, 6) for num in range(1, numero_de_jogadas + 1)]')

"""
1 - Escreva um programa que simule o lançamento de um dado de seis lados. Utilize a função randint para gerar o valor do 
dado e imprima o resultado.
2 - Modifique o programa para que o usuário possa especificar o número de lançamentos de dados que deseja realizar. 
Imprima os resultados de cada lançamento.
"""

# Item 1
print(f'O resultado do dado foi: {randint(1, 6)}')

# Item 2
numero_de_jogadas = 3
print(f'O resultado dos {numero_de_jogadas} lançamentos foram: '
      f'{[randint(1, 6) for num in range(1, numero_de_jogadas + 1)]}')

print('Exercício 2 -------------------------------------------------------------------------------choice("1234567890")')

"""
1 - Crie um programa que gere uma senha aleatória com 8 caracteres, composta de letras maiúsculas, letras minúsculas e 
dígitos numéricos. Utilize a função choice para selecionar aleatoriamente os caracteres de cada posição da senha.
2 - Peça ao usuário que especifique o comprimento desejado da senha e ajuste seu programa para gerar senhas com o 
comprimento fornecido.
"""

# Item 1
for n in range(0, 8):
    print(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678'), end='')

print('\b')

# Item 2
tamanho = 10

for n in range(0, tamanho):
    print(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678'), end='')

print('\b')

print('Exercício 3 -------------------------------------while numero_escolhido != numero_aleatorio and tentativas < 7:')

"""
1 - Desenvolva um jogo de adivinhação simples em que o computador escolhe um número aleatório entre 1 e 100, 
e o jogador tenta adivinhar qual é esse número. Forneça feedback ao jogador se o palpite for muito alto, muito baixo ou 
correto. Utilize a função randint para gerar o número aleatório.
2 - Aprimore o jogo permitindo que o jogador tenha um número limitado de tentativas para adivinhar o número. Se o 
jogador não acertar dentro desse número de tentativas, o jogo deve informar qual era o número secreto.
"""

numero_aleatorio = randint(1, 100)

numero_escolhido = int(input('Digite um número: '))

while numero_escolhido != numero_aleatorio:
    if numero_escolhido > numero_aleatorio:
        numero_escolhido = int(input('Menos: '))
    else:
        numero_escolhido = int(input('Mais: '))

print('Parabéns, você acertou!')

print('')

print('Agora vamos dificultar um pouco! \n Você deve acertar o número secreto em 7 tentativas!')

numero_aleatorio2 = randint(1, 100)

numero_escolhido2 = int(input('Digite um número de 1 a 100: '))

tentativas = 1

while numero_escolhido2 != numero_aleatorio2 and tentativas < 7:
    if numero_escolhido2 > numero_aleatorio2:
        numero_escolhido2 = int(input('Menos: '))
    else:
        numero_escolhido2 = int(input('Mais: '))
    tentativas = tentativas + 1

if numero_escolhido2 == numero_aleatorio2:
    print(f'Parabéns, você acertou em {tentativas} tentativas!')
else:
    print(f'Você não conseguiu :/ \b O número correto era: {numero_aleatorio2}')
