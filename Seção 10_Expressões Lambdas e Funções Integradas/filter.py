"""
FILTER

filter() serve para filtrar dados de uma determinada coleção.
"""

import statistics  # Biblioteca para trabalhar com dados estatísticos.

print('Tirando a média da maneira convencional --------------------------------------------sum(valores) / len(valores)')

valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)

print(media)

print('Filtrando valores acima da média --------------------------------------------filter(lambda x: x > media, dados)')

# Dados coletados
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Média dos dados com a função mean()
media2 = statistics.mean(dados)
print(f'Media: {media2}')

res = filter(lambda x: x > media2, dados)

print(f'Os valores acima da média são: {list(res)}')

"""
Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.
A função lambda na l26 é uma função anônima padrão com retorno.

Usar a biblioteca statistics é bom ao passo que é uma biblioteca pequena e não atrapalha na velocidade de reprodução 
do código. Pode usar para coisas simples.
"""

print('Após o primeiro uso os valores somem ----------------------------------------------------list(res) <> list(res)')

"""
Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória.
"""

print(f'Os valores acima da média são: {list(res)}')

"""
Isso é uma estratégia para não ocupar tanto a memória.
"""

print('O type filter -----------------------------------------------------------------------------------<class filter>')

print(type(res))

"""
filter object não é um conjunto, mas você pode convertê-lo.
"""

print('Dados faltantes ---------------------------------------------------------------------------filter(None, paises)')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador']
print(paises)

"""
Não é interessante nas nossas aplicações dados vazios como nesta lista. Então podemos utilizar filter() para 
removê-los.
"""

# Forma 1
res = filter(None, paises)  # Só
print(list(res))

"""
Função e iterável, é a mesma coisa, é como se fosse uma função de retorno que tivesse como retorno None. A diferença 
é que já colocamos o resultado direto nesse caso.
"""

# Forma 2
res2 = filter(lambda pais: len(pais) > 0, paises)
print(list(res2))

"""
Mesma coisa nesse exemplo, é uma função anônima que tem um resultado que será filtrado do iterável, ou seja, 
será selecionado na lista. O filter é como o filtro de café, que retém aquilo que não interessa para a gente e deixa 
passar o que nos convem.
Nesse exemplo, se um elemento da lista tem o número de letras maior que 0, ele é retornado.
"""

# Forma 3
res3 = filter(lambda pais: pais != '', paises)
print(list(res3))

"""
Aqui, se for diferente de '', retorna.
"""

"""
A diferênça entre map() e filter() é:

Em bom português, o filter() filtra valores desejados, e o map() retorna todos os valores. Agora vamos as definições 
literais:

map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeado a função para cada elemento
do iterável.

filter() -> Recebe dois parâmetros, uma função e um iterável, e retorna um objeto filtrando apenas os elementos de
acordo com a função.

A função filter() sempre retorna True ou False, que será o definidor de se um dado deve ou não ser selecionada. Já
o map retorna todos os valores.
"""

print('Exemplo mais complexo --------------------------------------lambda usuario: len(usuario[tweets]) == 0, usuarios')

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro Bolos", "Eu adoro Pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

"""
Vamos filtrar os usuários que estão inativos no twitter, ou seja, que nunca publicaram nenhum tweet.
"""

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

"""
Aqui a lógica foi a seguinte: len(usuario['tweets']) vai contar quantas ocorrências de valores há no valor da lista 
usuários, e se for igual a 0, o nome da pessoa será retornado.
"""

# Forma 2
inativos2 = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos2)

"""
Se o valor da chave for vazio, e eu negar, retorna True, por que o vazio é falso, e negando o falso, fica verdadeiro. 
Espero ter ajudado.

Filter com lambda é um diferencial, ao passo que são duas ferramentas muito úteis e que te destacam no mercado de 
trabalho.
"""

print('Combinando filter() e map() -----------------------------------map(lambda <função>, filter(<função>, <iterável>')

"""
Devemos criar uma lista contendo 'Sua instrutora é' + nome_da_instrutora, desde que cada nome tenha menos de 5 
caracteres. Ou seja, só a Ana, nesse caso a seguir:
"""

nomes = ['Vanessa', 'Ana', 'Maria']

lista1 = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista1)

"""
Pois bem, essa micelanha que contém duas virgulas funciona porque o filter() nesse caso virou o iterável. Dividindo:
FUNÇÃO: lambda nome: f'Sua instrutora é {nome}',
ITERÁVEL: filter(lambda nome: len(nome) < 5, nomes)
"""

print('Exercício 1 --------------------------------------------------------------filter(lambda n: n % 2 == 0, numeros)')

"""
Suponha que você tem uma lista de números inteiros e deseja criar uma nova lista que contenha apenas os números pares 
elevados ao quadrado. Utilize as funções filter() e map() para realizar essa tarefa.

1. Crie uma lista de números inteiros, por exemplo: numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
2. Utilize a função filter() para filtrar apenas os números pares da lista.
3. Utilize a função map() para elevar ao quadrado cada número par obtido no passo anterior.
4. Imprima a lista resultante contendo os quadrados dos números pares.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = filter(lambda n: n % 2 != 1, numeros)

print(list(map(lambda x: x ** 2, numeros_pares)))

print('Exercício 2 -------------filter(lambda quadrado_da_idade: quadrado_da_idade[`idade`] ** 2, quadrado_das_idades)')

"""
Vamos supor que você tem uma lista de dicionários representando pessoas e suas idades, e você quer criar uma nova lista 
que contenha o nome das pessoas que são maiores de idade (idade maior ou igual a 18) e, para essas pessoas, você quer 
calcular o quadrado da idade.

1.
pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bob", "idade": 17},
    {"nome": "Charlie", "idade": 30},
    {"nome": "David", "idade": 16},
    {"nome": "Eva", "idade": 22}
]

2. Use filter() para filtrar apenas as pessoas maiores de idade (idade maior ou igual a 18).
3. Use map() para criar uma nova lista contendo o nome das pessoas filtradas no passo 2 e o quadrado da idade delas.
4. Imprima a lista resultante.
"""

pessoas = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bob", "idade": 17},
    {"nome": "Charlie", "idade": 30},
    {"nome": "David", "idade": 16},
    {"nome": "Eva", "idade": 22}
]

maiores_de_idade = list(filter(lambda pessoa: pessoa['idade'] > 18, pessoas))

quadrado_das_idades = list(map(lambda quadrado_da_idade: quadrado_da_idade['idade'] ** 2, maiores_de_idade))

print(maiores_de_idade)
print(quadrado_das_idades)
