"""
LISTAS - 3ª PARTE
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print('Podemos colocar qualquer tipo de elemento em uma lista -----------------------[1, 2.3, "Python", True, [45, 23]')

lista6 = [1, 2, 34, True, [51, 1009]]

print('Iterando sobre uma lista ----------------------------------------------------------------for elemento in lista:')

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

"""
Isso fará o python imprimir cada elemento da lista.
Além disso, o soma = soma + elemento retornará a soma de todos os elementos, ao passo que ele será iterado e 
atualizado a cada repetição.
"""

print('Utilizando While ----------------------------------------------------------------------while produto != "sair":')

carrinho = []
produto = ''

while produto != 'sair':
    produto = input('adicione um produto na lista ou digite "sair" para sair: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print('Utilizando variáveis em listas -------------------------------------------------------resultados = [x, y, z, w]')

num1 = 1
num2 = 2
num3 = 3

numeros = [num1, num2, num3]
print(numeros)

print('Indexando uma lista ---------------------------------------------------------------cores = ["verde", "amarelo"]')

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[2])

"""
Nesse caso será impresso o azul, que é o indice [2]. 
- Lembre-se que nesse caso se usa [] ao invés de () para indicar o índice.
- Se colocar números negativos ele vai contar de trás pra frente, como se a lista fosse circular, mas não da mais de uma
volta.
"""

print('Imprimindo a lista com for -------------------------------------------------------------------for cor in cores:')

for cor in cores:
    print(cor)

print('Utilizando while erroneamente para imprimir a lista indexada ----------------------- while indice < len(cores):')

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

"""
O resultado é o mesmo, não será impresso o indice junto da cor porque no formato valor[indice] o resultado é o 
próprio valor.
"""

print('Gerando indice valor de uma lista corretamente usando for ---------------for indice, valor in enumerate(cores):')

for toma, cor in enumerate(cores):
    print(toma, cor)

"""
O enumerate é um método que serve para enumerar os elementos de uma lista.
- Lembre-se que independe do nome dos parametros passados para o for, o que importa é a posição que eles ocupam.
"""

print('Encontrando indices de elementos em uma lista -------------------------------------------------numeros.index(6)')

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(6))

"""
Será retornado o valor um. Se o valor não for encontrado, gera erro na execução.
"""

print('Fazendo uma busca focada na lista ----------------------------------------------------------numeros.index(5, 1)')

print(numeros.index(5, 1))

"""
O segundo número serve para colocar um ponto de início dentro da listas para as buscas, o retorno é 3 porque tem um 5 no
indice 3 da lista.
"""

print(numeros.index(5, 2))

# Busca dentro de um intervalo
print(numeros.index(5, 1, 4))

"""
Esse terceiro número irá dizer até qual índice podemos procurar.
"""

print('Técnica de slicing com parâmetro "inicio"-------------------------------------------------------------lista[1:]')

"""
lista[inicio:fim:passo]
"""

lista7 = [5, 6, 7, 8]

print(lista7[1:])

"""
Se lista[1] retorna o primeiro elemento, lista[1:], pela lógica, imprime a lista a partir do índice [1].
"""

print(lista7[2:])

print('Slicing com parâmetro "fim" --------------------------------------------------------------------------lista[:3]')

print(lista7[:3])

print('Slicing com parâmetros "inicio" e "fim" -------------------------------------------------------------lista[1:3]')

print(lista7[1:4])

print('Slicing com parâmetro "passo" ---------------------------------------------------------------------lista[1:3:4]')

print(lista7[1:2:4])

print('Colocando uma razão entre os índices ---------------------------------------------------------------lista[1::2]')

print(lista7[1::2])

"""
Nesse caso, será impresso os valores da lista um sim, um não.
- Pode usar números negativos.
"""

print('Invertendo valores de uma lista -------------------------------------------------------------nomes[1], nomes[0]')

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
print(nomes[0], nomes[1])

"""
Usar o método reverse pode ser melhor.
Nesse caso eu tive que colocar na ordem de novo para imprimir invertido, pois está invertido a partir do modo usado 
em aula.
No método da 162, é impresso em formato de lista.
"""

print('Métodos algebricos básicos -------------------------------------------------------------sum() min() max() len()')

lista8 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(lista8))  # soma
print(min(lista8))  # mínimo
print(max(lista8))  # máximo
print(len(lista8))  # tamanho da lista

print('Transformando uma lista em tupla ------------------------------------------------------------------tuple(lista)')

"""
Não estudamos ainda, mas uma tupla, visualmente, ao invés de ser fechada com colchetes, é fechada com parêntesis.
"""

lista9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista9)
print(type(lista9))

tupla = tuple(lista9)
print(tupla)
print(type(tupla))

print('Desempacotamento de listas -------------------------------------------------numero1, numero2, numero3 = lista10')

lista10 = [3, 4, 5]

numero1, numero2, numero3 = lista10

print(numero1)
print(numero2)
print(numero3)

"""
Se tivermos mais elementos para desempacotar do que argumentos para receber, teremos uma ValueError.
"""

print('Shallow Copy e Deep Copy --------------------------------------------------------------------------------------')

print('Deep Copy --------------------------------------------------------------------------nova_lista = lista11.copy()')

lista11 = [1, 2, 3]
novaLista = lista11.copy()

novaLista.append(4)

print(lista11)
print(novaLista)

"""
Toda modificação que for feita na novaLista não influencia na lista11, sãu duas listas diferentes.
"""

print('Shallow Copy ------------------------------------------------------------------------------nova_lista = lista11')

lista11 = [1, 2, 3]
novaLista = lista11

novaLista.append(4)

print(lista11)
print(novaLista)

"""
Dessa maneira, a lista original será modificada ao passo que modificamos a cópia.
"""

print('Exercício 1 ---------------------------------------------------------------------------------soma = nota + soma')

"""
Soma e Impressão:

Crie uma lista chamada notas com valores numéricos que representam as notas de um aluno em diferentes disciplinas.
Utilizando um loop for, calcule a soma das notas e imprima o resultado.
"""

# Notas
notas = [7, 8, 9, 5, 10, 6, 7, 9]

# Primeiro valor da soma
soma = 0

# Calculo por iteração
for nota in notas:
    soma = nota + soma

# Impressão
print(soma)

print('Exercício 2 -----------------------------------------------------------------------------frutas.index("Banana")')

"""
Busca e Substituição:

Crie uma lista chamada frutas com nomes de frutas.
Utilize o método index para encontrar o índice da fruta "Banana" na lista.
Substitua a "Banana" por "Morango" e imprima a lista resultante.
"""

frutas = ['mexirica', 'maça', 'goiaba', 'laranja', 'abacaxi', 'Banana']

print(frutas.index('Banana'))

print('Exercício 3 --------------------------------------------------------paises[0], paises[1] = paises[1], paises[0]')

"""
Invertendo com Desempacotamento:

Crie uma lista chamada paises com nomes de diferentes países.
Utilize a técnica de desempacotamento para inverter a ordem dos dois primeiros países na lista.
Imprima a lista resultante.
"""

paises = ['Brasil', 'Bolivia', 'Argentina', 'Venezuela', 'Colombia']

paises[0], paises[1] = paises[1], paises[0]
print(paises)
