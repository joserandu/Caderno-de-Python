"""
CONTINUAÇÃO DE LISTAS:
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

print('Inserindo valores em uma lista ------------------------------------------------lista1.insert(<indice>, <valor>)')

lista1.insert(2, 'novo valor')
print(lista1)

"""
Adicionamos a string à terceira posição da lista.
"""

print('Usando range para criar uma lista ordenada -----------------------------------------------------list(range(11))')

lista2 = list(range(11))
print(lista2)

print('Juntando listas ------------------------------------------------------------lista_concatenada = lista1 + lista2')

lista3 = lista1 + lista2
print(lista3)

# Ou:
# lista1.extend(lista2)

print('Invertendo valores de uma string --------------------------------------------------------------------.reverse()')

lista4 = (list('Geek University'))
lista4.reverse()
print(lista4)

"""
A diferênça dessa técnica (in-place) para a slicing ([::-1]) é que com esta é possível igualar a uma variável, 
enquanto a reverse modifica a própria variável.
"""

print('Copiando uma lista -------------------------------------------------------------------------------lista1.copy()')

lista5 = lista1.copy()
print(lista5)

"""
Não se engane, o método copy() pode e DEVE ser igualado à uma variável para fazer sentido.
"""

print('Contando o número de elementos de uma lista --------------------------------------------------------len(lista2)')

print(len(lista2))

print('Removendo o último elemento de uma lista ----------------------------------------------------------lista4.pop()')

lista4.pop()
print(lista4)

"""
Como já se pode imaginar, se colocar um número nesse método, ele remove o elemento que você programar, mas será 
eliminada a posição, então se por exemplo você colocou 2, e depois, com outra função procurar essa posição,
você não achará.
"""

print('Retornando o valor excluido ---------------------------------------------------------------print(lista4.pop())')

print(lista4.pop())
print(lista4)

print('Removendo todos os elementos --------------------------------------------------------------------lista5.clear()')

lista5 = list('Randinho')
lista5.clear()
print(lista5)

print('Multiplicando uma string --------------------------------------------------------------------------"python" * 6')

lista6 = 'python ' * 3 * 2
print(lista6)

print('Tranformando uma frase em uma lista --------------------------------------------------------------curso.split()')

curso = 'Curso Python essencial'
curso = curso.split()
print(curso)

"""
- curso.split() não funciona, precisa igualar à uma variável pois você está mudando o tipo de dado.
- O que separa é o espaço entre as palavras e a vírgula.
"""

print('Juntando elementos de uma lista para gerar uma string --------------------------------lista7 = " ".join(lista7)')

lista7 = ['A', 'vida', 'não', 'é', 'problema,', 'é', 'batalha']
lista7 = ' '.join(lista7)
print(lista7)

"""
O " " serve para indicar qual caractere irá separar os elementos da lista.
"""

print('Exercício 1 -------------------------------------------------insert(<posição>, elemento) pop() reverse() copy()')

"""
Manipulação de Listas

Considere a lista abaixo:

numeros = [5, 10, 15, 20, 25]

1.1. Adicione o número 30 ao final da lista e imprima o resultado.

1.2. Insira o número 8 na posição de índice 2 da lista e imprima a lista atualizada.

1.3. Remova o número 15 da lista e imprima o resultado.

1.4. Crie uma nova lista chamada numeros_reverso que contenha os elementos de numeros em ordem inversa e imprima essa 
nova lista.
"""

numeros = [5, 10, 15, 20, 25]

# 1
numeros.insert(5, 30)
print(numeros)

# 2
numeros.insert(2, 8)
print(numeros)

# 3
numeros.pop(3)
print(numeros)

"""
O numero que deve ser colocado no método não é o número que você deseja retirar, mas sim, o seu ÍNDICE.
"""

# 4
numeros.reverse()
numeros_reverso = numeros.copy()
print(numeros_reverso)

# Adicional
numeros.reverse()
print(numeros)

"""
Coloquei o adicional só para lembrar que colocando o reverse() de novo a lista acaba voltando ao que era antes.
"""

print('Exercício 2 -------------------------------------------------------------------------" ".join(palavras) split()')

"""
Manipulação de Listas e Strings

Considere a seguinte lista de palavras:

palavras = ['Python', 'é', 'uma', 'linguagem', 'poderosa']

2.1. Junte as palavras da lista em uma única string, separando-as por um espaço em branco, e imprima o resultado.

2.2. Crie uma cópia da lista original e adicione a palavra 'elegante' ao final da cópia. Imprima ambas as listas para 
verificar que a original não foi modificada.

2.3. Transforme a string resultante da junção das palavras em uma lista, utilizando o espaço como separador. Imprima a 
nova lista.
"""

palavras = ['Python', 'é', 'uma', 'linguagem', 'poderosa']

# 1
palavras_str = ' '.join(palavras)
print(palavras_str)

# 2
palavras2 = palavras.copy()
palavras2.pop(4)
palavras2.insert(4, 'elegante')
print(palavras)
print(palavras2)

# 3
palavras_list = palavras_str.split()
print(palavras_list)

print('Exercício 3 --------------------------------------------------------------------resultados.extend([11, 12, 13])')

"""
OPERAÇÕES COM LISTAS E NÚMEROS

Considere a lista de números abaixo:

numeros = [2, 4, 6, 8, 10]

3.1. Multiplique todos os elementos da lista por 3 e imprima a lista resultante.

3.2. Calcule a soma de todos os elementos da lista e imprima o resultado.

3.3. Remova o primeiro elemento da lista e imprima a lista atualizada.

3.4. Adicione os números 12, 14 e 16 ao final da lista e imprima a lista atualizada.
"""

numeros = [2, 4, 6, 8, 10]

# 1
resultados = []

for numero in numeros:
    resultado = numero * 3
    resultados.append(resultado)

print(resultados)

# 2
print(sum(resultados))

# 3
resultados.pop(0)
print(resultados)

# 4
resultados.extend([12, 14, 16])
print(resultados)
