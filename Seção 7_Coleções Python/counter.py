"""
MÓDULO COLLECTIONS - COUNTER

Collections -> High-performance Container Datatypes  (tipo de dados de conteiner de alta performace).

Counter significa contador em tradução literal.

Counter recebe um iterável como parâmetro e cria um objeto do tipo Collection Counter que é parecido com um
dicionário, contendo como chave o elemento da lista como parâmetro e como valor a quantidade de ocorrências desse
elemento.
"""

from collections import Counter

"""
Primeiramente, devemos importar a biblioteca Counter para realizar as operações.
"""

print('Utilizando o counter ------------------------------------------------from collections import Counter, Counter()')

lista = [1, 2, 1, 2, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 9]

res = Counter(lista)
print(type(res))
print(res)

"""
O método Counter() transforma os elementos de uma lista em chaves de um dicionário, e os valores são seus respectivos 
números de ocorrências.
A lista NÃO pode ser um conjunto, mas pode ser lista e tupla.
"""

print('Utilizando Counter em string -------------------------------------------------------------------------Counter()')

print(Counter('Geek University'))

"""
Nesse caso, o Counter irá mostrar o número de cada ocorrência das letras das strings, transformando as letras em 
chaves e o número de ocorrências em valores.
"""

print('Aplicando Counter em textos ---------------------------------------------------------------------------.split()')

texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to 
make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem 
Ipsum.Why do wuit? It is a long established fact that a reader will be distracted by the readable content of a page 
when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of 
letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop 
publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem 
ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes 
by accident, sometimes on purpose (injected humour and the like). Where does it come from? Contrary to popular belief, 
Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it
over 2000 years old. Richard McClintock,"""

# Criando a lista de palavras
palavras = texto.split()
print(palavras)

conte = Counter(palavras)
print(conte)

"""
Nessa caso o que fizemos primeiramente foi separar as palavras para em seguida sabermos o número de ocorrência de 
cada uma delas.

Curiosidade:
Existe um ramo da inteligencia artificial que se chama linguagem natural, que é as máquinas estudando como a gente
fala.
"""

print('Encontrar as palavras com mais ocorrências no texto --------------------------------------------.most_common(X)')

print(conte.most_common(5))

"""
Estamos pesquisando as 5 palavras com maior ocorrência.
"""

print('Exercício 1 ---------------------------------------')

"""
Considere a seguinte lista de frutas:

frutas = ['maçã', 'banana', 'maçã', 'morango', 'uva', 'abacaxi', 'uva', 'uva', 'morango', 'banana']

a) Utilize o Counter para criar um objeto que conte a quantidade de cada fruta na lista.

b) Determine qual é a fruta mais comum na lista.

c) Crie uma lista de tuplas, onde cada tupla contenha o nome da fruta e sua quantidade de ocorrências na lista.
"""

frutas = ['maçã', 'banana', 'maçã', 'morango', 'uva', 'abacaxi', 'uva', 'uva', 'morango', 'banana']

# a
quantidade = Counter(frutas)
print(quantidade)

# b
print(quantidade.most_common(1))

"""
Lembre-se:
O método most_common() não se referencia à lista (frutas), mas a variável que já possui o método Counter.
"""

# c
print(quantidade.most_common(5))

print('Exercício 2 ---------------------------')

"""
Considere a seguinte frase:

frase = "Python é uma linguagem de programação poderosa e fácil de aprender. Python é amplamente utilizado em diversas 
áreas."

a) Utilize o Counter para criar um objeto que conte a quantidade de cada palavra na frase.

b) Determine as três palavras mais frequentes na frase.

c) Crie uma lista de tuplas, onde cada tupla contenha a palavra e sua quantidade de ocorrências na frase.
"""

frase = "Python é uma linguagem de programação poderosa e fácil de aprender. Python é amplamente utilizado em " \
        "diversas áreas."

# a - Contando a ocorrência das palavras
listando_palavras = frase.split()
contando = Counter(listando_palavras)
print(contando)

# b - As três mais frequentes
print(f'As três palavras mais usadas na frase são: {contando.most_common(3)}')

# c - Criando as tuplas
print(contando.most_common(15))

print('Exercício 3 -------------------------------')

"""
Considere a seguinte lista de números:

numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

a) Utilize o Counter para criar um objeto que conte a quantidade de cada número na lista.

b) Determine qual é o número mais comum na lista.

c) Crie uma lista de tuplas, onde cada tupla contenha o número e sua quantidade de ocorrências na lista.
"""

numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

contando = Counter(numeros)
print(contando)

print(f'O número mais comum da lista de números é o número {contando.most_common(1)[0][0]}')

print(contando.most_common(5))
