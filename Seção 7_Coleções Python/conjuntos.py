"""
CONJUNTOS - SETS

- Conjuntos em qualquer linguagem de programação faz referência a teoria dos conjuntos da matemática.
- Aqui no Python os conjuntos são chamados de Sets
- Da mesma forma que na matemáticas, sets (conjuntos) não possuem valores:
    duplicados
    ordenados
    indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação
deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em python com {}.

Diferença entre Conjuntos (sets) e Mapas (dicionário) em Python:
    - Um dicionário tem chave e valor;
    - Um conjunto tem apenas valor;
"""

print('Definindo um conjunto --------------------------------------------------------------------------{x, y, z} set()')

# Forma feia
s = ({1, 2, 3, 4, 5, 6, 7, 2, 3})

print(s)
print(type(s))

"""
Lembre-se que os valores não são repetidos.
"""

# FORMA MAIS COMUM:
s1 = {1, 2, 3, 1, 2, 3}
print(s1)
print(type(s1))

print('Transformando uma string em conjunto -----------------------------------------------------------------set(nome)')

nome = 'Scarlet Johanson'
print(set(nome))

"""
As letras e o espaço viram elementos da lista e a ordem é aleatóriamente alterada.
"""

print('Trabalhando com if/else ------------------------------------------------------------------------if num in set1:')

num = 13

if num in s1:
    print(f'A lista possui o número {num}')
else:
    print(f'A lista não possui o número {num}')

"""
Importante lembrar que além de não termos valores duplicados não temos ordem.
"""

print('Comparando as coleções -------------------------------------Conjunto: {conjunto} com {len(conjunto)} elementos.')

dados = '99, 2, 34, 23, 12, 1, 23, 44, 5'

"""
Ele colocou essa variável nas demais para evitar a repetição, mas deu errado, porque adicionou a virgula na lista, 
usando os métodos tuple(), e set(). Desconsidere.
"""

lista = [99, 2, 34, 23, 12, 1, 44, 23, 5]
print(f'Lista {lista}, com {len(lista)} elementos.')

tupla = (99, 2, 34, 23, 12, 1, 44, 23, 5)
print(f'Tupla {tupla}, com {len(tupla)} elementos.')

dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 23, 5], 'dict')

"""
Lembre-se: Para declarar um dicionário, primeiramente coloque as chaves, depois o método .fromkeys() e dentro do
método você declara as chaves e o valor delas.
"""

print(f'Dicionário: {dicionario}, com {len(dicionario)} elementos.')

"""
Dicionários não aceitam chaves duplicadas, por isso, 8 elementos.
"""

conjunto = {99, 2, 34, 23, 12, 1, 23, 44, 5}
print(f'Conjunto {conjunto}, com {len(conjunto)} elementos.')

print('Conjuntos suportam qualquer tipo de valor -------------------------------------------------{3, True, 3.44, "f"}')

s2 = {3, True, 3.44, 'f'}
print(s2)
print(type(s2))

print('iterando valores do set -----------------------------------------------------------------------for valor in s2:')

for valor in s2:
    print(valor)

print('Usos interessantes com sets -----------------------------------------------------------------------------------')

"""
Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam 
manualmente a cidade de onde vieram. Nós adicionamos cada cidade em uma lista python já que em uma lista podemos
adicionar novos elementos e ter repetição.
"""

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

# Precisamos saber quantas cidades estão presentes. Podemos utilizar o set para isso:

print(len(set(cidades)))  # Fazendo isso, teremos o números de cidades que comparecemos.

print('Adicionando elementos em um conjunto --------------------------------------------------------------------.add()')

s3 = {1, 2, 3}
s3.add(4)
s3.add(4)  # Duplicidade não gera erro, apenas é ignorada.
print(s3)

print('Removendo elementos ----------------------------------------------------------------------------------.remove()')

s4 = {3, 6, 9}
s4.remove(6)  # A vida é simples.
print(s4)
s4.remove(3)  # Se tentar remover um valor que não exista, KeyError
s4.remove(9)
print(s4)  # Fiz um teste aqui pra ver como ficava.

print('Outro jeito de remover elementos --------------------------------------------------------------------.discard()')

s5 = {5, 10, 15}
s5.discard(10)
print(s5)
s5.discard(20)  # Com o método discard, se colocar um valor que não existe ele não dá erro.
print(s5)

print('Copiando um conjunto para outro --------------------------------------.copy() (Deep Copy), x = y (Shallow Copy)')

# Deep Copy
s6 = {12, 34, 56}
s7 = s6.copy()
s7.add(78)
print(s6)
print(s7)

# Shallow copy
s8 = {9, 8, 7, 6}
s9 = s8  # A igualdade vale da esquerda para direita e da direita para esquerda.
s9.add(5)
print(s8)
print(s9)

print('Podemos excluir todos os termos de um conjunto ----------------------------------------------------------.clear')

s10 = {1, 2, 3, 5, 8}
s10.clear()
print(s10)

print('Métodos matemáticos de conjuntos ------------------------------------------------------------------------------')
print('')
print('Métodos de união de conjuntos ---------------------------------------------------------------------.union() e |')

"""
Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um contendo estudantes do curso de Java e
precisamos gerar um conjunto com o nome dos estudantes sem repetição
"""

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando union()
uniao = estudantes_java.union(estudantes_python)
print(f' A união dos conjuntos é {uniao}')

"""
Essa forma é a mais recomendável, pois fica mais claro o código.
"""

# Forma 2 - Utilizando o caractere pipe '|'
uniao2 = estudantes_java | estudantes_python
print(f' A união dos conjuntos é {uniao2}')

print('Intersecção ------------------------------------------------------------------------------------.intersection()')

# Forma 1 - intersection
interseccao = estudantes_java.intersection(estudantes_python)
print(f'a intersecção dos conjuntos é {interseccao}')

# Forma 2 - &
interseccao2 = estudantes_java & estudantes_python
print(f'a intersecção dos conjuntos é {interseccao2}')

print('Subtração de conjuntos ---------------------------------------------------------------------------.difference()')

so_python = estudantes_python.difference(estudantes_java)
print(f'Fazem somente Python: {so_python}')

so_java = estudantes_java.difference(estudantes_python)
print(f'Fazem somente Java: {so_java}')

print('Soma, valor máximo, valor mínimo e tamanho --------------------------------------------------------------------')

s11 = {1, 2, 3, 4, 5}

print(sum(s11))
print(max(s11))
print(min(s11))
print(len(s11))

"""
Vimos nessa aula os mais importantes, mas temos outros também:

Todos os métodos possíveis: 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
'symmetric_difference_update', 'union', 'update'
"""

print('Exercício 1 ------------------------------')

"""
Considere dois conjuntos, conjunto_a e conjunto_b, representando estudantes de dois cursos diferentes. Crie esses 
conjuntos com alguns nomes de estudantes.

a) Utilizando o método de união (union ou |), crie um novo conjunto chamado todos_estudantes que contenha todos os 
estudantes sem repetição.

b) Utilizando o método de interseção (intersection ou &), crie um novo conjunto chamado estudantes_comuns que contenha 
os estudantes que estão presentes em ambos os cursos.

c) Utilizando o método de diferença (difference), crie dois conjuntos chamados estudantes_apenas_a e estudantes_apenas_b
que contenham os estudantes exclusivos de cada curso.
"""

conjunto_a = {'Erika', 'Elislaine', 'Jhonatas', 'Igor', 'Abel', 'Jorge'}
conjunto_b = {'Douglas', 'Estefany', 'Jorge', 'Elias', 'Elisa', 'Erika'}

# a
todos_os_estudantes = conjunto_a.union(conjunto_b)
print(todos_os_estudantes)

# b
estudantes_comuns = conjunto_a.intersection(conjunto_b)
print(estudantes_comuns)

# c
estudantes_apenas_a = conjunto_a.difference(conjunto_b)
estudantes_apenas_b = conjunto_b.difference(conjunto_a)
print(estudantes_apenas_a)
print(estudantes_apenas_b)

print('Exercício 2 -----------------------------------')

"""
Considere um conjunto de números inteiros numeros = {1, 2, 3, 4, 5}.

a) Calcule a soma de todos os números no conjunto.

b) Encontre o valor máximo e o valor mínimo no conjunto.

c) Determine o tamanho (número de elementos) do conjunto.
"""

numeros = {1, 2, 3, 4, 5}

# a
soma = sum(numeros)
print(soma)

# b
maximo = max(numeros)
minimo = min(numeros)
print(maximo)
print(minimo)

# c
tamanho = len(numeros)
print(tamanho)

print('Exercício 3 --------------------------------')

"""
Dado um conjunto de letras letras = {'a', 'b', 'c', 'd', 'e'}, realize as seguintes operações:

a) Adicione a letra 'f' ao conjunto.

b) Remova a letra 'c' do conjunto.

c) Verifique se a letra 'd' está presente no conjunto e imprima uma mensagem indicando o resultado.

d) Crie uma cópia do conjunto original chamada outras_letras utilizando o método de cópia.
"""

letras = {'a', 'b', 'c', 'd', 'e'}

# a
letras.update('f')
print(letras)

# b
letras.remove('c')
print(letras)

# c
if 'd' in letras:
    print('A letra "d" está presente na lista')
else:
    print('A letra "d" não está presente na lista')

# d
outras_letras = letras.copy()
print(outras_letras)
