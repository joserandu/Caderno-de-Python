"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays em outras linguagens), com a diferença de serem DINAMICOS e
podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo;
    Simplesmente cria a lista e vai adicionando elementos.
    Não quer dizer que a lista é infinita, ela acaba até onde tiver memória.
        Depende do tipo de computador/tablet/celular que está rodando.
- Qualquer tipo de dado: As listas não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em python são representados por [];
"""

print('Type list ---------------------------------------------------------------------------------------------type([])')

type([])

print('Listas para os exemplos da aula ----------------------------------------------------------------list(range(11))')

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print('Checando se um valor está contido na lista ---------------------------------------------------if num in lista4:')

num = 7
if num in lista4:
    print(f'O número {num} consta em nosso sistema')
else:
    print(f'O número {num} consta em nosso sistema')

print('Ordenando uma lista ------------------------------------------------------------------------------lista1.sort()')

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

"""
No caso de listas de strings, viram primeiro os espaços, depois os números e depois as letras em ordem alfabética.
"""

print('Contando o número de ocorrência dos valores --------------------------------------------------lista1.count("e")')

print(lista1.count(1))
print(lista5.count('e'))

print('Adicionando elementos em uma lista -----------------------------------------------------------lista1.append(18)')

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

print('Procurando uma lista dentro de outra lista ---------------------------------------------if [1, 2, 3] in lista1:')

if [8, 3, 1] in lista1:
    print('Esses dados estão disponíveis.')
else:
    print('Não encontrei a lista.')

print('Adicionando elementos como parte da lista ------------------------------------------lista1.extend([13, 14, 15])')

lista1.extend([164, 5, 195])
print(lista1)

"""
Dessa forma, não será adicionado uma lista assim como com o método append(), será adicionado os três elementos de 
forma a participarem individualmente da lista principal. Esse método é bem importante.

O código dessa aula continua, só vou trocar para esse não ficar muito poluído.
"""

print('Exercício 1 ---------------------------------------------------------------------------sort() remove() extend()')

"""
Considere a lista abaixo:

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

1.1. Ordene a lista em ordem crescente e imprima o resultado.

1.2. Remova o número 2 da lista e imprima o resultado.

1.3. Adicione os números 7 e 8 ao final da lista e imprima a lista atualizada.

1.4. Conte quantas vezes o número 5 aparece na lista e imprima o resultado.
"""

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

numeros.sort()
numeros.remove(2)
print(numeros)

numeros.extend([7, 8])
print(numeros)

print(f'O numeros de ocorrências do número 5 são {numeros.count(5)} vezes')

print('Exercício 2 ---------------------------------------')

"""
Considere as seguintes listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

2.1. Concatene as duas listas em uma única lista chamada lista_concatenada e imprima o resultado.

2.2. Verifique se o número 3 está presente na lista_concatenada e imprima se está ou não.

2.3. Crie uma nova lista chamada sublista que contenha os elementos da lista_concatenada do índice 2 até o índice 5 
(inclusive). Imprima sublista.

2.4. Inverta a ordem dos elementos na sublista e imprima o resultado.
"""

# 1
lista_um = [1, 2, 3, 4, 5]
lista_dois = [6, 7, 8, 9, 10]

lista_um.extend(lista_dois)
print(lista_um)

"""
Se você fazer lista_concatenada = lista1.extend(lista2), assim como eu estava tentando, o retorno será none, 
pois o valor que você quer é justamente o valor da lista1.
"""

lista_concatenada = lista_um

"""
Ao invés de fazer esse bololo todo eu poderia fazer simplesmente lista_concatenada = lista_um + lista_dois.
Essa última linha deixou o código bem anti-profissional.
"""

# 2
if 3 in lista_concatenada:
    print(f'O valor 3 está contido na lista')
else:
    print(f'O valor 3 não está contido na lista')

# 3
sublista = lista_concatenada[2: 6]
print(sublista)

# 4
sublista_invertida = sublista[::-1]
print(sublista_invertida)

"""
To me achando. O chatGPT falou para usar o reverse() e deu errado, mas eu tinha usado o [::-1] e deu certo. Isso 
acontece pelo mesmo motivo do extends a pouco, não se pode igualar esse método à uma variável. Faça dessa forma:

sublista.reverse()
print(sublista)
"""
