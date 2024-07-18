"""
LISTAS ANINHADAS

Na matemática são chamadas de matrizes.

- Algumas linguagens de programação possúem uma estrutura de dados chamadas de arrays:
    - Unidimensionais: Arrays (propriamente ditos), vetores.
    - Multidimensionais: Matrizes.

Em Python não existe Arrays, existem listas.

exemplo = [1, '2', 3.789, 4, True]

Em outras linguagens, geralmente não podemos variar o tipo de dado, mas em Python pode.
"""

print('Matriz em Python -------------------------------------------------------------[[1, 2, 3], [4, 5, 6], [7, 8, 9]]')

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
print(type(listas))

"""
Continua sendo do tipo lista.
"""

print('Acessando elementos: linha x coluna ---------------------------------------------------------------listas[0][1]')

print(listas[0])  # voltará o primeiro elemento.
print(listas[0][1])  # perceba a linha e coluna.
print(listas[2][-2])  # Com numeros negativos também funciona.

"""
Lembre-se que a linha e coluna começam com o zero.
"""

print('Iterando com loop for em uma lista aninhada ---------------------------for lista in listas: / for num in lista:')

for lista in listas:
    print(lista)  # Retorna as listas dentro da lista.

for lista in listas:
    for num in lista:
        print(num)

"""
É um loop dentro de outro loop.
"""

print('Usando List Comprehension -------------------------[[valor for valor in lista]')

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""
Perceba que esse não é o jeito convencional que haviamos visto anteriormente, mas esse jeito se encaixa mais a 
situação posto que se for feito com um print posteriormente, como foi feito abaixo, a impressão fica em formato de 
lista. Lembre-se que ali é o lugar da função.
"""

valores = [[valor for valor in lista] for lista in listas]
print(valores)

print('Gerando um tabuleiro/matrix 3x3 -----------------[[numero for numero in range(1, 4)] for numero in range(1, 4)]')

tabuleiro = [[numero for numero in range(1, 4)] for numero in range(1, 4)]
print(tabuleiro)

print('Gerando jogadas para o jogo da velha ---------------["x" if numero % 2 == 0 else "0" for numero in range(1, 4)]')

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

"""
Colocar as chaves no lugar errado pode mudar tudo.
"""

print('Gerando valores iniciais -------------------------------------[["*" for i in range(1, 4)] for j in range(1, 4)]')

print([['*' for i in range(1, 4)] for j in range(1, 4)])

"""
Nesse exemplo a ideia era colocar os espaços vazios dentro da velha.
"""

print('Exercício 1 -----------------------------------')

"""
Crie uma lista aninhada chamada matriz_identidade que represente uma matriz identidade 3x3. Uma matriz identidade é uma 
matriz quadrada em que todos os elementos da diagonal principal são iguais a 1 e todos os outros elementos são iguais 
a 0. Imprima a matriz.
"""

matriz_identidade = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print('Exercício 2 ------------------------------')

"""
Dada a lista aninhada abaixo, representando as notas de alunos em diferentes disciplinas:

notas_alunos = [
    [8, 7, 9],
    [5, 6, 7],
    [10, 9, 8],
    [6, 7, 5]
]

Calcule a média de cada aluno e imprima o resultado. Em seguida, calcule a média de cada disciplina e imprima o 
resultado.
"""

notas_alunos = [
    [8, 7, 9],
    [5, 6, 7],
    [10, 9, 8],
    [6, 7, 5]
]

media_aluno = [sum(notas) / len(notas) for notas in notas_alunos]
print(f'A média de cada aluno foi: {media_aluno}')

"""
Deixei essa parte do código para imprimir com a finalidade de ficar mais claro o que está acontecendo.
"""

for i, media in enumerate(media_aluno):
    print(f'Aluno: {i + 1} | Média: {media:.2f}')

media_disciplina = [sum(notas) / len(notas) for notas in notas_alunos]

media_disciplinas = [sum(notas[i] for notas in notas_alunos) / len(notas_alunos) for i in range(len(notas_alunos[0]))]
print(media_disciplinas)

for i, media in enumerate(media_disciplinas):
    print(f'Matéria: {i + 1} | Média: {media}')

print('Exercício 3 ---------------------------')

"""
Crie uma lista aninhada chamada triangulo_pascal que represente as primeiras cinco linhas do Triângulo de Pascal. O 
Triângulo de Pascal é construído de forma que cada número é a soma dos dois números diretamente acima dele na linha 
anterior. Imprima a lista resultante.
"""

triangulo_pascal = [[1], [1, 1]]

for i in range(2, 5):
    linha_anterior = triangulo_pascal[-1]
    nova_linha = [1] + [linha_anterior[j - 1] + linha_anterior[j] for j in range(1, i)] + [1]
    triangulo_pascal.append(nova_linha)

print("Triângulo de Pascal:")
for linha in triangulo_pascal:
    print(linha)

"""
Belíssimo exercício.
"""
