"""
DICIONÁRIOS

OBS. Em algumas linguagens de programação os dicionários em Python são conhecidos por mapas.
Dicionários são coleções de chave/valor. (ou índice/valor, o que você preferir).
Ao contrário das listas e das tuplas, nas quais os ídices ficam implícitos, os índices ficam EXPLICITOS.
São representados por chaves: {}
"""

print('Representação visual ----------------------------------------------------{"chave": "valor", "chave2": "valor2"}')

print(type({}))  # type 'dict'

"""
- A chave e valor são separados por dois pontos 'chave: valor';
- tando chave quando valor podem ser de qualquer tipo de dado;
- Podemos misturar o tipo de dados;
"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

print('Outra Representação --------------------------------------------------------------------------dict(br="Brasil")')

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')  # Forma feia, usa a outra que é melhor
print(paises)
print(type(paises))

print('Acessando elementos ---------------------------------------------------------------------------dicionario["py"]')

print(paises['br'])
print(paises['py'])

"""
Isso é importantíssimo e você fará muito isso: pesquisar dados dentro de um dicionário.
Simplesmente você vai colocar o nome do dicionário e a chave do valor no qual você deseja acessar.
O acesso é feito da mesma forma que com as listas e tuplas, com a diferença que ao invés de procurarmos diretamente o 
índice, procuramos a chave primeiro.
Se tentarmos fazer o acesso com um índice que não existe, teremos um erro do tipo KeyError. Ex: print(paises['ru'])
"""

print('Forma recomendada ---------------------------------------------------------------------------------------.get()')

print(paises.get('br'))
print(paises.get('ru'))

"""
Usar o get() é recomendado por não retornar um KeyError caso o índice não seja achado. Apenas retorna um None, 
e dessa maneira você consegue trabalhar com a lógica do None.
"""

print('O dado do tipo NONE ---------------------------------------------------------------------------------------None')

"""
O DADO DO TIPO NONE em python representa o tipo sem tipo, ou pode ser chamado também de tipo vazio, porém, falar que é 
um tipo sem tipo é mais apropriado.
Lembre-se que em None A PRIMEIRA LETRA é MAIÚSCULA.
"""

numeros = None
print(numeros)
print(type(numeros))

"""
Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de recebermos um 
valor final. 
"""

# Ex:
numeros = 1.34, 1.44, 5.78
print(numeros)
print(type(numeros))

print('O tipo None sempre retorna falso --------------------------------------------------------------------None=False')

pais = paises.get('ru')  # None.

if pais:
    print('encontrei o país')
else:
    print('não encontrei o país')

"""
Perceba que a estrutura completa para esse comando seria if pais is True: , mas não é necessário.
É possível fazer isso sem usar o if/else, mas o exemplo que o professor deu foi tão merda e deu tão errado que não deu
nem vontade de escrever. O if/else resolve o seu problema.
"""

print('Verificação se uma chave existe -----------------------------------------------------------------"br" in paises')

print('br' in paises)  # True
print('ru' in paises)  # False
print('Estados Unidos' in paises)  # False, pois isso não é uma chave, é um valor.

print('Utilizando outros tipos de dados -------------------------------------------------------------{(-45, -60): "SP"')

"""
Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive lista, tupla, dicionário, como chaves 
de dicionários.
"""

localidades = {
    (35.8953, 58.8472): 'Escritório em Tókio',
    (40.8953, 60.8472): 'Escritório em Nova York',
    (65.8953, -12.8472): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

print('Adicionar elementos em um dicionário -----------------------------------------------.update({<chave>: <valor>})')

receita = {'jan': 1000, 'fev': 1200, 'mar': 3000, 'abr': 3500}

receita.update({'mai': 5000})
print(receita)

"""
O append() não funciona com dicionários, para adicionar elementos é com o .update({}) e colocando chave e valor.
"""

print('Atualizando dados ------------------------------------------------------------------receita[mai] = <novo valor>')

receita['mai'] = 5500
print(receita)

"""
Em dicionários NÃO podemos ter chaves repetidas. Só pode existir UMA chave para cada valor.
"""

print('Remover dados de um dicionário ---------------------------------------------------pop("<chave a ser retirada>")')

# Forma 1:
receita.pop('mai')
print(receita)

"""
Isso vai retirar a chave e o valor. Precisamos obrigatóriamente informar a chave, e caso não encontre, é retornado um 
KeyError.
"""

print('Retornando o valor retirado ------------------------------------------------------retirado = receita.pop("abr")')

retirado = receita.pop('abr')
print(retirado)
print(receita)

"""
Essa forma é bem útil e importante, atenção nela.
"""

print('Forma mais convencional de remover dados de um dicionário -----------------------------------del receita["mar"]')

# Forma 2:
del receita['mar']
print(receita)

"""
Se não ouver a chave, dessa vez não dá KeyError. se acostume a usar o del.
"""

print('Exemplo prático com listas -----------------------------------------------------------------------carrinho = []')

'''
Imagine que você tem um comércio eletrônico ende temos um carrinho de compras na qual adicionamos produtos
Carrinho de compras
    Produto 1:
        - nome:
        - quantidade:
        - preço:
    Produto 2:
        - nome:
        - quantidade:
        - preço:
'''

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

print('Exemplo prático com Tupla -------------------------------------------------------carrinho = (produto1, produto2')

produto1 = ('Plastation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

print('Exemplo prático com dicionário ------------------------------------------------------produto1 = {"nome": valor}')

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God Of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

"""
IMPORTANTE:
Perceba que É POSSÍVEL USAR APPEND() para adicionar DICIONÁRIOS EM UMA LISTA, não para adicionar elementos EM um 
DICIONÁRIO. Neste caso é usado o UPDATE.

- De cara, essa trás informações mais detalhadas e a vizualização é mais facil.
- perceba que esses tipos de coleções se completam: A lista pode ser uma lista de dicionários.
"""

print('Métodos para dicionários --------------------------------------------------------------------------------------')
print('Limpando totalmente o dicionário ----------------------------------------------------------------------.clear()')

dicionario = dict(a=1, b=2, c=3)
dicionario.clear()
print(dicionario)

print('Copiando um dicionário para outro (Deep Copy)------------------------------------------------------------copy()')

dicionario = {'a': 1, 'b': 2, 'c': 3}
novoDicionario = dicionario.copy()
novoDicionario['d'] = 4

print(dicionario)
print(novoDicionario)

"""
É uma forma melhor do que a próxima (Shallow Copy), pois permite mexer individualmente em um dicionário sem alterar o 
original.
"""

print('Copiando um dicionário para outro (Shallow Copy) ---------------------------------dicionario2 = novo_dicionario')

dicionario2 = novoDicionario
dicionario2['e'] = 5

print(dicionario2)
print(novoDicionario)

"""
Dessa forma altera ambos os dicionários.
"""

print('Forma não usual de criação de dicionários ------------------------------------------------{}.fromkeys("a", "b")')

# Forma simples:
outro = {}.fromkeys('a', 'b')  # cria um dicionario com aquela chave 'a' e este valor 'b'.
print(outro)
print(type(outro))

"""
'a' vira chave e 'b' vira o valor.
"""

# Com a chave sendo uma lista
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

"""
Perceba que nesse caso 'desconhecido' virou valor para todas as chaves contidas nas listas.
"""

# Dividindo uma string
veja = {}.fromkeys('teste', 'valor')
print(veja)

"""
Aqui ele dividiu a palavra teste e fez 3 chaves com as letras t, e, s.
Perceba isso no fromkeys, ele divide a string.
"""

# Utilizando range()
vejaDeNovo = {}.fromkeys(range(1, 11), 'valor')
print(vejaDeNovo)

print('Exercício 1 -----------------------------------------------------------------------------------------aluno = {}')

"""
Crie um dicionário chamado aluno que represente as informações de um estudante. O dicionário deve conter as seguintes 
chaves:

'nome': com o nome do aluno.
'idade': com a idade do aluno.
'curso': com o curso que o aluno está cursando.

Em seguida, imprima as informações do aluno utilizando as chaves do dicionário.
"""

aluno = {'nome': 'Carolina', 'idade': 27, 'curso': 'psicologia'}
print(f'Nome: {aluno["nome"]} \n Idade: {aluno["idade"]}, \n Curso: {aluno["curso"]}')

print('Exercício 2 --------------------------------------------------------------for produto, info in estoque.items():')

"""
Crie um dicionário chamado estoque que represente o estoque de uma loja. O dicionário deve conter informações sobre três 
produtos diferentes, utilizando os nomes dos produtos como chaves e, para cada produto, um dicionário com as seguintes 
chaves:

'quantidade': com a quantidade em estoque.
'preco': com o preço do produto.

Em seguida, imprima as informações de todos os produtos do estoque.
"""

estoque = {
    'Air Max': {'quantidade': 15, 'preço': 750.00},
    'Springblade': {'quantidade': 2, 'preço': 600.00},
    'Mizuno de Mil': {'quantidade': 25, 'preço': 1200.00}
}

print(estoque)

for produto, info in estoque.items():
    print(f'Produto: {produto}; Quantidade: {info["quantidade"]}; Preço: {info["preço"]}')

"""
LEMBRE-SE:
O método items é essencial para a vizualisação de um dicionário. E que para vizualizar é preciso o chave e valor que 
nesse caso foi o produto, info.
Veja outro exemplo:

O método items() em dicionários em Python retorna uma visualização de todos os itens (pares chave-valor) presentes no 
dicionário. A função desse método é fornecer acesso fácil tanto às chaves quanto aos valores do dicionário, permitindo 
iterações eficientes sobre seus elementos.

O método items() retorna um objeto de visualização (view object) que exibe uma lista de tuplas, onde cada tupla contém 
um par chave-valor do dicionário. Essa visualização é dinâmica, o que significa que reflete quaisquer alterações feitas 
no dicionário original.

Exemplo de uso do método items():

meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

# Obtendo a visualização de itens
itens = meu_dicionario.items()

# Iterando sobre os itens
for chave, valor in itens:
    print(f'Chave: {chave}, Valor: {valor}')
O resultado seria:

Chave: a, Valor: 1
Chave: b, Valor: 2
Chave: c, Valor: 3
O uso de items() é comum quando você precisa percorrer simultaneamente as chaves e os valores de um dicionário em um 
loop, facilitando o acesso a ambos.
"""

print('Exercício 3 --------------------------------------------------------------------if produto in estoque1.items():')

"""
Crie uma função chamada processar_vendas que recebe como parâmetros o dicionário de estoque, o nome do produto e a 
quantidade vendida. A função deve verificar se o produto está no estoque e, se estiver, atualizar a quantidade em 
estoque subtraindo a quantidade vendida. Além disso, a função deve calcular o valor total da venda 
(quantidade vendida * preço do produto) e imprimir uma mensagem informando o sucesso da venda.

Em seguida, faça chamadas à função processar_vendas para simular vendas de diferentes produtos e quantidades, 
atualizando o estoque e mostrando o resultado.
"""

estoque = {
    'Air Max': {'quantidade': 15, 'preço': 750.00},
    'Springblade': {'quantidade': 2, 'preço': 600.00},
    'Mizuno de Mil': {'quantidade': 25, 'preço': 1200.00}
}


def processar_vendas(estoque1, produto_recebido, quantidade):
    if produto_recebido in estoque1.items():
        print(f'O produto está no estoque e tem {quantidade} unidades')
    print('O produto não está no estoque')


processar_vendas(estoque, 'Air Max', 5)
