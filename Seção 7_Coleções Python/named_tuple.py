"""
MÓDULO COLLECTIONS - NAMED TUPLE

"tupla nomeada"
tupla = (num1=1, num2=2, num3=3)

São Tuplas diferenciadas, aonde especificamos um nome para a mesma e também, parâmetros.
"""

from collections import namedtuple  # com letra minuscula aqui

print('Relembrando tuplas -------------------------------------------------------------------------------------tuple()')

tupla = (1, 2, 3)
print(tupla)

print('Usando Named Tuple --------------------------------------------------------------------------------namedtuple()')

# Precisamos definir o nome e parâmetros.

# Forma 1
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2
cachorro2 = namedtuple('cachorro', 'idade, raça, nome')  # Prefiri essa.

# Forma 3
cachorro3 = namedtuple('cachorro', ['idade', 'raça', 'nome'])

nojento = cachorro2(idade=2, raça='Pitbull', nome='Nojento')
print(nojento)

print('Acessando dados ------------------------------------------------------------------------------------variavel[x]')

# Forma 1
print(nojento[0])  # Idade
print(nojento[1])  # raça
print(nojento[2])  # nome

# Forma 2
print(nojento.idade)  # Idade
print(nojento.raça)  # raça
print(nojento.nome)  # nome

"""
Essa daqui é mais interessante e intuitiva, melhora a performace e dá mais sentido em usar uma namedtuple() ao invés 
de uma lista.
"""

print('procurando o indice e contando as ocorrências -----------------------nojento.index("Pitbull") nojento.count(2))')

print(nojento.index('Pitbull'))
print(nojento.count(2))

"""
Se você tem domínio nessa seção de listas que chegou ao fim, você está muito a frente de muitos programadores python, 
atenção a documentação.
"""

print('Exercício 1 ----------------------------------------------------------namedtuple("Aluno", "idade, curso, nome")')

"""
Registro de Alunos com Named Tuple

Crie uma named tuple chamada Aluno para representar informações sobre estudantes, incluindo os campos nome, idade e 
curso. Em seguida, crie instâncias de alunos e imprima as informações de cada aluno.
"""

aluno = namedtuple('Aluno', 'idade, curso, nome')
belligham = aluno(idade=21, curso='História', nome='Belligham')
print(belligham)

print('Exercício 2 ------------------------------------------------produto(nome="Torxilax", preço=20, quantidade=6513)')

"""
Estoque de Produtos com Named Tuple

Crie uma named tuple chamada Produto para representar informações sobre produtos em um estoque, incluindo os campos 
nome, preco e quantidade. Em seguida, crie instâncias de produtos e imprima as informações de cada produto.
"""

produto = namedtuple('produto', 'nome, preço, quantidade')

produto1 = produto(nome='Torxilax', preço=20.00, quantidade=456)
produto2 = produto(nome='Dramin', preço=17.00, quantidade=7605)

print(produto1)
print(produto2)

print('Exercício 3 -------------------------------------------------------------------Latitude: {coordenada3.latitude}')

"""
Coordenadas Geográficas com Named Tuple

Crie uma named tuple chamada Coordenada para representar coordenadas geográficas, incluindo os campos latitude e 
longitude. Em seguida, crie instâncias de coordenadas para representar diferentes locais e imprima as informações de 
cada coordenada.
"""

coordenada = namedtuple('coordenada', 'latitude, longitude')

coordenada1 = coordenada(latitude=675, longitude=5)
coordenada2 = coordenada(latitude=6, longitude=546)
coordenada3 = coordenada(latitude=652, longitude=685)

print(f'Latitude: {coordenada1.latitude} | Longitude: {coordenada1.longitude}')
print(f'Latitude: {coordenada2.latitude} | Longitude: {coordenada2.longitude}')
print(f'Latitude: {coordenada3.latitude} | Longitude: {coordenada3.longitude}')
