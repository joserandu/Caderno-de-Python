"""
SORTED

Não confunda com a função sort() que já estudamos em listas. O sort() só funciona em listas. Já o sorted() podemos
utilizar com qualquer iteravel.

Como o próprio nome já diz, sorted() serve para ordenar.
"""

print('Relembrando sort() --------------------------------------------------------------------------------lista.sort()')

lista = [3, 4, 2, 9, 39]
lista.sort()
print(lista)

print('Usando sorted() --------------------------------------------------------------------------------sorted(numeros)')

numeros = [3, 1, 4, 2, 6, 3, 3]
print(sorted(numeros))
print(numeros)

"""
A função sorted não altera a ordenação original da lista, já o método .sort() altera a ordem original da lista.
O sorted() SEMPRE retorna uma LISTA.
"""

print('Inverter a ordem da lista --------------------------------------------------------sorted(numeros, reverse=True)')

print(sorted(numeros, reverse=True))

print('Convertendo a lista para outros tipos de coleções --------------------set(sorted(numeros) tuple(sorted(numeros)')

print(set(sorted(numeros, reverse=True)))
print(tuple(sorted(numeros, reverse=True)))

print('A chave key= em sorted ---------------------------------------------------------------sorted(usuarios, key=len)')

"""
Podemos utilizar o sorted() para ações mais complexas.
"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro Bolos", "Eu adoro Pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Ordenando por número de tweets
print(sorted(usuarios, key=len))

"""
A chave (key=) é o que organiza a lista que será impressa, nesse caso, o len indica que o que ordenará a lista será o 
maior número.
A lista continua a mesma, porque todos tem dois.
"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro Bolos", "Eu adoro Pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},  # adicionei aqui
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Ordenando por nome de usuário.
print(sorted(usuarios, key=lambda usuario: usuario['username']))

"""
Passamos primeiro a lista de usuários para depois a função, que vem acompanhada da chave.
"""

# Ordenando pelo tweet em ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario['tweets']))

"""
Os vazios vem primeiro, para depois a ordem alfabética.
"""

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

print('O reverse na função sorted() ---------------------------------------------------------------------,reverse=True')

# Para inverter a ordem
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

print('Ordenando pelos valores de um dicionário --------------------sorted(musicas, key=lambda musica: musica["repr"])')

musicas = [
    {"título": "Vida Loka", "reproduções": 1234710},
    {"título": "Vida Loka pt.2", "reproduções": 23098457043},
    {"título": "Fórmula mágica da paz", "reproduções": 1093285643},
    {"título": "Diário de um detento", "reproduções": 1948243},
]

# Da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['reproduções']))

# Da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['reproduções'], reverse=True))

print('Exercício 1 ----------------------------------------------sorted(estoque, key=lambda produto: produto["preco"])')

"""
Exercício 1:

1 - Explique a diferença entre as funções sort() e sorted() em Python. Dê exemplos para ilustrar cada caso.
    R: O método sort() funciona somente com listas e altera a ordem original da lista. Já a função sorted() não 
    altera a ordem original da lista consegue lidar com qualquer iterável.
2- Crie uma lista de strings desordenada e ordene-a utilizando tanto o método sort() quanto a função sorted(). 
Compare os resultados e explique por que são diferentes.
3 - Escreva uma função que receba uma lista de dicionários, onde cada dicionário contém informações sobre um produto 
(nome, preço, quantidade em estoque). Ordene essa lista de dicionários pelo preço dos produtos em ordem crescente 
utilizando a função sorted().
"""

# Item 2
alunos = ['Ana', 'Clarisse', 'Bernardo', 'Renato', 'Lucas', 'Matheus']

# Utilizando sorted
lista_chamada = sorted(alunos)
print(lista_chamada)

# Utilizando sort
alunos.sort()
print(alunos)

"""
A diferença entre os métodos se mostra ao passo que sort altera a ordem original da lista, enquanto sorted() funciona 
como função propriamente dita, não alterando o iterável original.
"""

# Item 3
estoque = [
    {'produto': "Feijão", 'preco': 6.50, 'quantidade': 150},
    {'produto': "Arroz", 'preco': 22.50, 'quantidade': 80},
    {'produto': "Molho de tomate", 'preco': 1.25, 'quantidade': 500},
    {'produto': "Vinagre", 'preco': 3.20, 'quantidade': 200}
]

precos = sorted(estoque, key=lambda produto: produto['preco'])
print(precos)

print('Exercício 2 -----------------------sorted(usuarios, key=lambda usuario: len(usuario["username"]), reverse=True)')

"""
1 - Dada a lista de usuários fornecida no código, ordene-a de duas maneiras diferentes: primeiro, pelo número de 
tweets em ordem crescente e, em seguida, pelo número de tweets em ordem decrescente.
2 - Modifique a lista musicas fornecida para incluir uma nova música com um número alto de reproduções. Em seguida, 
ordene a lista de músicas de acordo com o número de reproduções em ordem decrescente.
3 - Utilizando a lista usuarios, ordene-a pelo comprimento do nome de usuário em ordem crescente e, em seguida, 
ordene-a pelo comprimento do nome de usuário em ordem decrescente.
"""

# Item 1
# Do menor para o maior
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Do maior para o menor
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))

# Item 2
nova_musica = {'título': 'Da ponte pra cá', 'reproduções': 61435461}
musicas.append(nova_musica)

mais_reproduzidas = sorted(musicas, key=lambda musica: musica['reproduções'], reverse=True)
print(mais_reproduzidas)

# Item 3
menores_nomes = sorted(usuarios, key=lambda usuario: len(usuario['username']))
print(menores_nomes)

maiores_nomes = sorted(usuarios, key=lambda usuario: len(usuario["username"]), reverse=True)
print(menores_nomes)

print('Exercício 3 ------------------------------------------sorted(musicas, key=lambda musica: musica["reproduções"])')

"""
1 - Dada a lista de usuários fornecida no código, crie uma função que ordene os usuários primeiro por sua presença em 
redes sociais (se possuem tweets ou não), e em seguida, em ordem alfabética pelo nome de usuário.
2 - Utilizando a lista usuarios, ordene-a pelos tweets de cada usuário em ordem alfabética.
3 - Modifique a lista musicas fornecida para incluir uma nova música com um número baixo de reproduções. Em seguida, 
ordene a lista de músicas de acordo com o número de reproduções em ordem crescente.
"""

# Item 1
presenca_usuarios = sorted(usuarios, key=lambda usuario: len(usuario['tweets']))
print(presenca_usuarios)

ordem_alfabetica_username = sorted(usuarios, key=lambda usuario: usuario['username'])
print(ordem_alfabetica_username)

# Item 2
ordem_alfabetica_tweets = sorted(usuarios, key=lambda usuario: usuario['tweets'])
print(ordem_alfabetica_tweets)

# Item 3
musicas.append({'título': 'Guina', 'reproduções': 16515})
menos_reproduzidas = sorted(musicas, key=lambda musica: musica['reproduções'])
print(menos_reproduzidas)
