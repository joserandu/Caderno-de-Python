"""
MAPAS

Em Python conhecemos como dicionários, que são representados por {}.
"""
print('Iterando sobre dicionarios ---------------------------------------------------------------for chave in receita:')

receita = {'jan': 1000, 'fev': 2500, 'mar': 4000}

# Imprimindo a chave
for chave in receita:
    print(chave)

# Imprimindo o valor
for chave in receita:
    print(receita[chave])

"""
Preste bem atenção em como se retira o valor, pois você precisa obrigatóriamente da chave.
"""

print('Trazendo chave e valor -------------------------------------------------------------------for chave in receita:')

for chave in receita:
    print(f'{chave}: {receita[chave]}')

"""
REPARE: O dicionário/map é como uma tranca, na qual você precisa saber a chave para acessar.
"""

print('Para saber quais são as chaves -------------------------------------------------------------------------.keys()')

print(receita.keys())

"""
O método .keys() retorna as chaves do dicionário.
"""

for chave in receita.keys():
    print(receita[chave])

"""
Com isso você tem acesso aos valores também.
"""

print('Acessando os valores ---------------------------------------------------------------------------------.values()')

print(receita.values())

"""
Esse método vai retornar todos os valores do dicionário.
"""

for valor in receita.values():
    print(valor)

"""
Ao contrário do feito acima, com o for, será listado bonitinho, sem caracteres identificadores. É o método mais 
pythonico.
"""

print('Desempacotando ----------------------------------------------------------------------------------------.items()')

print(receita.items())

"""
Retorna as chaves e os valores dentro de uma lista que ficam organizados em tuplas.
"""

for chave, valor in receita.items():
    print(f'Chave={chave} e valor={valor}')

print('Soma, valor máximo, valor mínimo e tamanho ---------------------------------------------sum() max() min() len()')

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
print(len(receita))

"""
O len não necessita do método .values(), pois ele já tem como função contar os elementos dentro de values.
"""

print('Exercício 1 --------------------------------------------------------------for chave, valor in despesas.items():')

"""
Crie um novo dicionário chamado despesas com três meses ('jan', 'fev', 'mar') e seus respectivos valores. Utilize a 
estrutura de repetição for para iterar sobre as chaves e valores do dicionário despesas, imprimindo cada mês e seu 
valor.
"""

despesas = {'jan': 1500, 'fev': 1000, 'mar': 500}

for chave, valor in despesas.items():
    print(f'Mês: {chave} | Despesa: {valor}')

print('Exercício 2 -----------------------------------------------------{sum(dictionario.values()) / len(dicionairio)}')

"""
Dado o dicionário receita, crie uma função chamada calcular_media que recebe um dicionário como parâmetro e retorna a 
média dos valores contidos nele. Em seguida, chame essa função passando o dicionário receita como argumento e imprima 
o resultado.
"""


def calcular_media(dicionario):
    return f'A receita média foi de: {sum(dicionario.values()) / len(dicionario)}'


print(calcular_media(receita))

print('Exercício 3 --------------------------------------------------------------------------if mes in receita.keys():')

"""
Utilizando o dicionário receita, crie uma função chamada encontrar_mes que recebe um valor como parâmetro e retorna o 
mês correspondente a esse valor no dicionário. Se o valor não estiver presente no dicionário, a função deve retornar 
"Mês não encontrado". Em seguida, chame a função com um valor existente no dicionário e outro que não exista, e imprima
os resultados.
"""


def encontrar_mes(mes):
    if mes in receita.keys():
        print(f'O receita do mês de {mes} foi de {receita[mes]} reais.')
    else:
        print('Mês não encontrado')


encontrar_mes('jan')
