"""
DICTIONARY COMPREHENSION

Pense o seguinte:

Se quisermos fazer uma lista fazemos: lista = [1, 2, 3, 4, 5]
Caso queiramos criar uma tupla: tupla = (1, 2, 3, 4, 5) ou 1, 2, 3, 4, 5
Para fazer um set (conjunto): {1, 2, 3, 4, 5}
E para criar um dicionário: dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Sintax:
List Comprehension:
[valor for valor in iteravel]

Dictionary Comprehension:
{chave: valor for valor in iterável}
"""

print('Utilizando dictionary comprehension --------------------{chave: valor ** 2 for chave, valor in numeros.items()}')

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

"""
A chave continua a mesma, somente o valor que acaba sendo iterado
"""

print('Gerando um dicionário a partir de uma lista --------------------------{valor: valor ** 2 for valor in numeros2}')

numeros2 = [1, 2, 3, 4, 5]
quadrado2 = {valor: valor ** 2 for valor in numeros2}
print(quadrado2)

print('Gerando um dicionário a partir de uma tupla --------------------------{valor: valor ** 2 for valor in numeros2}')

numeros3 = 1, 2, 3, 4, 5
quadrado3 = {valor: valor ** 3 for valor in numeros3}
print(quadrado3)

"""
Não muda nada na sintaxe.
"""

print('Gerando um dicionário a partir de um set -----------------------------{valor: valor ** 2 for valor in numeros2}')

numeros4 = {1, 2, 3, 4, 5}
quadrado4 = {valor: valor ** 4 for valor in numeros4}
print(quadrado4)

"""
Também não muda nada na sintaxe.
"""

# Lembre-se:
numeros2 = [1, 2, 3, 4, 5, 1, 2]
quadrado2 = {valor: valor ** 2 for valor in numeros2}
print(quadrado2)

"""
As chaves não podem ser repetidas. Os valores novos não são adicionados a partir de chaves não existentes.
"""

print('Juntando chaves e valores de listas diferentes ----------{chaves[i]: valores[i] for i in range(0, len(chaves))}')

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

print('Exemplo com lógica condicional (if/else) ---------{num: ("par" if num 2 % == 0 else "impar") for num in numbers')

numeros5 = [1, 2, 3, 4, 5]
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros5}
print(resultado)

print('Exercício 1 --------------------------------------------------{i + 1: letras[i] for i in range(0, len(letras))}')

"""
Crie um dicionário chamado letras_indices que mapeie cada letra do alfabeto (de 'a' a 'z') ao seu índice correspondente
no alfabeto. Imprima o dicionário resultante.
"""

letras = 'abcdefghijklmnopqrstuvwxyz'

letras_indices = {i + 1: letras[i] for i in range(0, len(letras))}
print(letras_indices)

print('Exercício 2 ------{chave: ("aprovado" if valor >= 6 else "reprovado") for chave, valor in alunos_notas.items()}')

"""
Dada a lista de alunos e suas respectivas notas abaixo, crie um dicionário chamado aprovados que mapeie o nome do aluno 
à sua situação na disciplina. Se a nota for maior ou igual a 6, a situação é 'aprovado', caso contrário, é 'reprovado'. 
Imprima o dicionário resultante.

alunos_notas = {'Alice': 7, 'Bob': 5, 'Charlie': 8, 'David': 4, 'Eva': 6}
"""

alunos_notas = {'Alice': 7, 'Bob': 5, 'Charlie': 8, 'David': 4, 'Eva': 6}

aprovados = {chave: ('aprovado' if valor >= 6 else 'reprovado') for chave, valor in alunos_notas.items()}
print(aprovados)

"""
Nunca se esqueça do .items(). Você vai acessar como um dicionário sem antes especificar?
"""

print('Exercício 3 --------------------------------{letra: frase.count(letra) for letra in set(frase) if letra != " "}')

"""
Crie um dicionário chamado contagem_letras que conta a frequência de cada letra na string abaixo. Não inclua espaços na 
contagem. Imprima o dicionário resultante.

frase = "python dictionary comprehension"
"""

frase = "python dictionary comprehension"

contagem_letras = {letra: frase.count(letra) for letra in set(frase) if letra != ' '}
print(contagem_letras)
