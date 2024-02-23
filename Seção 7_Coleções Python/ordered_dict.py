"""
MÓDULO COLLECTIONS: ORDERED DICT

Em um dicionário, a ordem de inserção dos elementos não é garantida para chave e valor.

OrderedDict é um dicionário que nos garante a ordem de inserção dos elementos.
"""
# Importando a biblioteca OrderedDict
from collections import OrderedDict

print('Relembrando Dicionários -------------------------------------------------------------------------------.items()')

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor};')

"""
- Não necessáriamente o valor será impresso na ordem de entrada, para isso, usamos o OrderedDict.
- Lembre-se de colocar o método .items(), para dividir os valores dentro do dicionário.
"""

print('Utilizando Ordered Dict --------------------------------------------------------------------------OrderedDict()')

dicionario2 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario2.items():
    print(f'chave={chave}: valor={valor};')

"""
É simples, é so colocar o OrderedDict() que a ordem de entrada dos elementos será garantida.
"""

print('Entendendo a diferença entre dict e OrderedDict --------------------------------------------------OrderedDict()')

# Sem OrderedDict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True

# Com OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # False

"""
Para o OrderedDict(), a ordem dos elementos importa.
"""

print('Exercício 1 ---------------------------------------------------------------for nome, contato in agenda.items():')

"""
Ordenação com OrderedDict

Crie um OrderedDict chamado agenda para armazenar informações de contatos. Adicione alguns contatos à agenda (chave 
sendo o nome do contato e valor sendo o número de telefone). Em seguida, itere sobre a agenda e imprima os contatos na 
ordem em que foram adicionados.
"""

agenda = OrderedDict({'Amanda': 11932453494, 'Carol': 119349549139, 'Leticia': 11932944839})

for nome, contato in agenda.items():
    print(f'Contato: {nome} | Número: {contato}')

print('Exercício 2 -----------------------------------------------------------dicionario_combinado.update(dicionario1)')

"""
Combinação de dicionários

Crie dois dicionários, dicionario1 e dicionario2, ambos contendo informações sobre produtos (por exemplo, nome do 
produto, preço, quantidade). Utilize um OrderedDict para cada dicionário. Combine esses dois dicionários em um terceiro 
OrderedDict chamado dicionario_combinado mantendo a ordem de inserção dos elementos de ambos.
"""

dicionario1 = OrderedDict({'Produto1': 10.99, 'Produto2': 20.99, 'Produto3': 30.99})
dicionario2 = OrderedDict({'Produto4': 40.99, 'Produto5': 50.99, 'Produto6': 60.99})

dicionario_combinado = OrderedDict()
dicionario_combinado.update(dicionario1)
dicionario_combinado.update(dicionario2)

for produto, preco in dicionario_combinado.items():
    print(f'{produto}: R${preco:.2f}')

"""
O .2f serve para formatar que deve ter duas casas decimais.
"""

print('Exercício 3 -----------------------------------------------------------------cat_produtos[produto] = novo_preco')

"""
Atualização de preços

Suponha que você esteja gerenciando um catálogo de produtos em uma loja online. Crie um OrderedDict chamado 
catalogo_produtos com alguns produtos e seus preços. Em seguida, crie uma função chamada atualizar_preco que aceita o 
nome do produto e um novo preço como argumentos e atualiza o preço correspondente no OrderedDict. Teste a função 
atualizando o preço de pelo menos um produto e imprima o catálogo atualizado.
"""

catalogo_produtos = OrderedDict({
    'Xre 300': 35000.00,
    'CB 1000': 55000.00,
    'Fazer 250': 25000.00
})


def atualizar_preco(cat_produtos, nome_produto, novo_preco):
    if nome_produto in cat_produtos:
        cat_produtos[nome_produto] = novo_preco
        print(f'A motocicleta {nome_produto} teve o seu valor alterado para {novo_preco}')
    else:
        print(f'A motocicleta {nome_produto} não consta em nosso sistema.')


# Catalogo antes da atualização:
print(f'Catálogo antes da atualização: ')
for produto, valor in catalogo_produtos.items():
    print(f'{produto}: {valor}')

# Atualização
atualizar_preco(catalogo_produtos, 'Xre 300', 38000.00)

# Depois da atualização
print('Novo catálogo:')
for produto, valor in catalogo_produtos.items():
    print(f'{produto}: {valor}')
