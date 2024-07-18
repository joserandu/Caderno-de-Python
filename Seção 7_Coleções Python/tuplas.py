"""
TUPLAS (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

    1 - As tuplas são representadas por () ao invés de []

    2 - As tuplas são IMUTÁVEIS: Toda alteração em uma tupla gera uma nova tupla.
"""

print('Caracterização visual de uma tupla --------------------------------------------------------(1, 2, 3) ou 1, 2, 3')
# CUIDADO1 - As tuplas são representadas por parêntesis, mas sem parêntesis TAMBÉM É UMA TUPLA:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

print('Tuplas com apenas um elemento -------------------------------------------------------------------------------4,')

tupla3 = 4
print(tupla3)
print(type(tupla3))

"""
Essa variável é do tipo int, e se colocar parêntesis infringe a PEP8.
"""

tupla3 = 4,
print(tupla3)
print(type(tupla3))

"""
Nesse exemplo temos uma tupla.
CONCLUSÃO: Tuplas são definidas pelas VÍRGULAS, não pelos parentesis. 4 não é tupla. 4, é tupla
"""

print('Gerando tuplas dinamicamente com o range ------------------------------------------------tuple(range(1, 11, 5))')

tupla4 = tuple(range(11))
print(tupla4)
print(type(tupla4))

"""
Lembre-se: range(<inicio>,<fim>,<passa>)
"""

print('Desempacotamento de tupla -------------------------------------------------------------nome, sobrenome = tupla5')

tupla5 = ['Randú', 'José Costa']

nome, sobrenome = tupla5
print(nome)
print(sobrenome)

"""
Se colocar mais de uma variável, acaba dando errado.

IMPORTANTE:
Métodos de adição e remoção nas tuplas NÃO EXISTEM.
Mas podemos somar, valor mínimo, máximo e a quantidade de elementos.
"""

print('Operações para dados sobre uma tupla ---------------------------------------------------sum() max() min() len()')

tupla6 = 2, 3, 4, 5, 6, 7, 8

print(sum(tupla6))  # soma
print(max(tupla6))  # máximo
print(min(tupla6))  # mínimo
print(len(tupla6))  # número de elementos

print('Concatenação de tuplas -------------------------------------------------------------------------tupla1 + tupla2')

tupla7 = 1, 8, 15
tupla8 = 4, 6, 8

print(tupla7 + tupla8)

"""
Nenhuma das duas muda, pois são tuplas, mas se juntam.
"""

# Igualando a uma variável:
tupla7 = tupla7 + tupla8
print(tupla7)

print('Verificando se um elemento está contido na tupla ---------------------------------------------------3 in tupla1')

tupla9 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(3 in tupla9)
print(11 in tupla9)

"""
Não se esqueça do in. O retorno desse fácil método de pesquisa é booleano.
"""

print('Iterando sobre uma tupla ---------------------------------------------------------------------for n in tupla10:')

tupla10 = 1, 2, 3, 4, 5

# Imprimindo os valores da tupla
for n in tupla10:
    print(n)

for indice, valor in enumerate(tupla10):
    print(indice, valor)

"""
enumerate() é uma função que vai enumerar os elementos de uma lista, de uma tupla ou até de uma string. Muito útil 
para varios códigos.
"""

print('Contando elementos dentro de uma tupla ----------------------------------------------------------------.count()')

tupla11 = 'a', 'b', 'c', 'd', 'a', 'b'
print(tupla11.count('a'))

print('Transformando string em uma tupla -----------------------------------------------------tuple("Geek University")')

escola = tuple('Geek University')
print(escola)
# Contando quantas vezes 'e' aparece
print(escola.count('e'))

print('Dicas na utilização das tuplas ---------------------------------------')

"""
Usamos tuplas sempre que não precisamos mudar os dados contidos em uma coleção.
"""

meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', \
        'Novembro', 'Dezembro'

"""
Nesse caso, não faz sentido você retirar ou adicionar mais ou menos meses do ano, claro que dependendo do contexto.
"""

print('Acesso a elementos de uma tupla -----------------------------------------------------------------------meses[5]')

print(meses[5])  # # Bem semelhante às listas

print('Iterar com While -------------------------------------------------------------------------while i < len(meses):')

i = 0

# Imprimindo todos os meses
while i < len(meses):
    print(meses[i])
    i = i + 1

print('Verificando qual é o índice de um elemento em uma tupla -----------------------------------meses.index("Julho")')

print(meses.index('Julho') + 1)

"""
Eu somei 1 só para o retorno ficar como mês 7.
Se houver dois índices iguais, retornará a ocorrência do primeiro índice.
"""

print('Slicing ------------------------------------------------------------------------tuple[<inicio>: <fim>: <passo>]')

mes = 3

print(meses[mes - 1:8])

"""
Coloquei o " - 1" porque eu quiz que começasse pelo mês 5, pois estava começando por junho.
"""

print('Shallow Copy uma tupla --------------------------------------------------------------------nova_tupla = tupla11')

tupla12 = 10, 20, 30
novaTupla = tupla12
print(novaTupla)

# Concatenando
outra = novaTupla + tupla12

print(outra)

"""
Não é possível utilizar Deep copy em tuplas
"""

"""
POR QUE UTILIZAR TUPLAS:

1 - Tuplas são mais rápidas do que listas
    Isso gera maior performace nos seus dados.
    Podem ter vários tipos de dados misturados, só não são dinâmicas.

2 - Trás mais segurança ao seu código.
    Isso por conta da imutabilidade do código.

Se colocar o dir de uma tupla no console, você verá que só tem dois métodos: index e count, o resto são funções.
"""

print('Exercício 1 ---------------------------------------------------------------nome, idade, cidade = dados_pessoais')

"""
Criação e Desempacotamento:

Crie uma tupla chamada dados_pessoais com informações pessoais, como nome, idade e cidade.
Utilize o desempacotamento para atribuir cada elemento a variáveis individuais (por exemplo, nome, idade, cidade).
Imprima as variáveis individualmente.
"""

dados_pessoais = 'Randú', 23, 'Guarulhos'

nome, idade, cidade = dados_pessoais

print(nome)
print(idade)
print(cidade)

print('Exercício 2 ---------------------------------------------------------------------------print(tupla_a + tupla_b)')

"""
Operações e Concatenação:

Crie duas tuplas, tupla_a e tupla_b, com números de sua escolha.
Realize a soma dos elementos de ambas as tuplas e imprima o resultado.
Concatene as duas tuplas e imprima a tupla resultante.
"""

tupla_a = 2, 4, 6, 8, 10
tupla_b = 1, 3, 5, 7, 9

print(sum(tupla_a))
print(sum(tupla_b))

print(tupla_a + tupla_b)

print('Exercício 3 -----------------------------------------')

"""
Pesquisa e Contagem:

Crie uma tupla chamada frutas com nomes de diferentes frutas.
Utilize o método count para contar quantas vezes a fruta "Maçã" aparece na tupla.
Utilize o método index para encontrar o índice da fruta "Pera" e imprima o resultado.
"""

frutas = 'Maçã', 'Laranja', 'Melancia', 'Banana', 'Goiaba'

frutas.count('Maçã')
print(frutas.count('Pera'))
