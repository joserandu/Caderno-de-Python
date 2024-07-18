"""
FUNÇÕES COM PARÂMETROS (DE ENTRADA)
    *A redundância é para deixar bem claro isso:

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
"""

print('Função estática -----------------------------------------------------------------------------------return 7 * 7')


def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())
print(quadrado_de_7())

"""
Essa função está estática e independentemente de quantas vezes imprimirmos ela o resultado sempre será o mesmo.
"""

print('Refatorando para deixar dinâmico -------------------------------------------------def funcao(indicar_parâmetro)')


def quadrado(numero):
    return numero * numero


print(quadrado(9))
print(quadrado(14))

"""
Precisa indicar que a função recebe algum argumento.
É no print() que colocamos o parâmetro da função.
"""

print('Usando operadores matemáticos -------------------------------------------------------------------------------**')


def quadrado2(numero):
    return numero ** 2


print(quadrado2(20))
print(quadrado2(18))

"""
Se não colocar um parâmetro quando indicamos que a função recebe parâmetros, o código acaba gerando erro.
"""

print('Refatorando a função cantar_parabens() --------------------------------------------------------(aniversariante)')


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Ra tim bum {aniversariante}, {aniversariante}, {aniversariante}')


cantar_parabens('Patrícia')

print('Funções com mais de um parâmetro ----------------------------------------------------------def funcao(x, y, z):')

"""
Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros forem 
nessessários, sendo eles separados por vírgula (,).
"""


def soma(x, y):  # Parâmetros.
    return x + y


def multiplica(z, w):
    return z * w


def outra(a, b, c):
    return (a + b) * c


print(soma(25, 30))  # Argumentos.
print(multiplica(7, 9))
print(outra(21, 2, 2))
print(outra(2, 3, 'Python '))

"""
PARÂMETROS: São os espaços que abrimos na função para recebimento dos argumentos.
ARGUMENTOS: Dados enviados para a função.
Essa é a minha clara definição para quando eu ler eu entender, mas a definição mais formal é:

PARÂMETROS: Variáveis declaradas na definição de uma função;
ARGUMENTOS: Dados passados durante a execução de uma função;

Na ultima impressão a string será repetida o número devido de vezes segundo os parâmetros.

Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError, seja com mais ou menos argumentos.
"""

print('Nomeando parâmentos --------------------------------------------------------def nome_completo(nome, sobrenome):')

"""
Em programação, sempre é importante que tudo faça sentido, para isso, precisamos saber nomear os parâmetros.
"""


def nome_completo(nome1, sobrenome1):
    return f'Seu nome completo é {nome1} {sobrenome1}'


print(nome_completo('Angelina', 'Jolie'))

"""
Lembre-se que a ordem dos argumentos importa.
Não faço ideia porque o PEP8 estava reclamando dos parametros se chamarem nome e sobrenome, mas eu coloquei o um na 
frente e o erro saiu.
"""

print('Argumentos nomeados --------------------------------------------------------------------------Keyword Arguments')

"""
Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
"""

print(nome_completo(sobrenome1='José', nome1='Randú'))

# OU
nome = 'Antonieta'
sobrenome = 'Maria'

print(nome_completo(sobrenome1=nome, nome1=sobrenome))

print('Erro comum na utilização de return ----------------------------------------------------------------------    --')


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

# Repare na diferênça entre os dois resultados:


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

"""
A diferênça na impressão dessas duas funções, que aparentemente são idênticas consistem na POSIÇÃO DO RETURN.
No segundo caso, pelo return estar na mesma casa que a estrutura do if, o código do if acaba acontecendo uma única vez, 
resultando em um único resultado (1). Já com o return mais recuado, como no primeiro caso, o loop será feito 
completamente para depois a finalização.

A função recebe qualquer tipo de parâmetro, pode ser tupla, lista, conteiner, string, dict, etc.
"""

print('Exercício 1 ----------------------------------------------------------------------------caucular_media(x, y, z)')

"""
Considere a seguinte função:

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
    
A função calcular_media recebe três parâmetros que representam as notas de um aluno e retorna a média dessas notas. 
Utilizando essa função, calcule e imprima a média das seguintes notas: 8.5, 9.2 e 7.8.
"""


def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


print(f'A média das notas dos alunos é: {calcular_media(8.5, 9.2, 7.8)}')

print('Exercício 2 -----------------------------')

"""
Crie uma função chamada verificar_maioridade que recebe como parâmetro a idade de uma pessoa e retorna uma mensagem 
indicando se ela é maior de idade ou não. Considere a maioridade a partir dos 18 anos. Em seguida, utilize essa função 
para verificar se uma pessoa de 22 anos é maior de idade.
"""


def verificar_maioridade(idade):
    if idade < 18:
        return 'Essa pessoa informada é menor de idade'
    return 'A pessoa informada é maior de idade'


print(verificar_maioridade(22))

print('Exercício 3 --------------------')

"""
Considere a seguinte situação:

Você está desenvolvendo um sistema de controle de estoque para uma loja. Crie um programa que utilize funções para 
realizar as seguintes operações:

1. Cadastro de Produto:

- Crie uma função chamada cadastrar_produto que recebe como parâmetros o nome do produto, o preço e a quantidade em 
estoque. A função deve armazenar essas informações em um dicionário representando o produto e adicioná-lo a uma lista 
de produtos.
- A lista de produtos deve ser uma variável global para que possa ser acessada e modificada por outras funções.

2. Listagem de Produtos:

- Crie uma função chamada listar_produtos que percorre a lista de produtos e imprime as informações de cada produto (
nome, preço e quantidade em estoque).

3. Atualização de Estoque:

- Crie uma função chamada atualizar_estoque que recebe como parâmetros o nome do produto e a quantidade a ser 
adicionada ao estoque. A função deve buscar o produto na lista, atualizar a quantidade em estoque e imprimir uma 
mensagem informando sobre a atualização.

4. Consulta de Produto:

- Crie uma função chamada consultar_produto que recebe o nome do produto como parâmetro e busca na lista de produtos. 
A função deve imprimir as informações do produto se ele existir, ou uma mensagem indicando que o produto não foi 
encontrado.

Utilize essas funções para realizar as seguintes operações:

- Cadastrar três produtos diferentes.
- Listar os produtos cadastrados.
- Atualizar o estoque de um dos produtos.
- Consultar as informações de um produto que foi cadastrado.
- Listar novamente os produtos para verificar as atualizações no estoque.

Observação: Considere que a lista de produtos e as funções devem ser definidas no escopo global do programa.
"""

"""
lista_de_produtos = []


def cadastrar_produto(produto, preco, quantidade):
    return lista_de_produtos.append({'nome': produto, 'preço': preco, 'quantidade': quantidade})


cadastrar_produto('Cenoura', 2.99, 50)
cadastrar_produto('Feijão', 6.99, 1000)


def listar_produtos():
    print(lista_de_produtos)


def atualizar_estoque(produto, quantidade):
    return lista_de_produtos


def consultar_produto(produto):
    if lista_de_produtos.index(nome=produto)= None:
        return f'{produto} existe em nosso estoque'
    return f'{produto} não existe em nosso estoque'


listar_produtos()
# print(consultar_produto('Cenoura'))
"""

# Variável global para armazenar a lista de produtos
lista_produtos = []


# Função para cadastrar um produto
def cadastrar_produto(nome_produto, preco, quantidade):
    produto = {'nome': nome_produto, 'preco': preco, 'quantidade': quantidade}
    lista_produtos.append(produto)
    print(f'Produto {nome} cadastrado com sucesso.')


# Função para listar os produtos
def listar_produtos():
    print('\nLista de Produtos:')
    for produto in lista_produtos:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")


# Função para atualizar o estoque
def atualizar_estoque(nome_produto, quantidade):
    for produto in lista_produtos:
        if produto['nome'] == nome_produto:
            produto['quantidade'] += quantidade
            print(f'Estoque do produto {nome_produto} atualizado. Nova quantidade: {produto["quantidade"]}')
        return print(f'Produto {nome_produto} não encontrado.')


# Função para consultar um produto
def consultar_produto(nome_produto):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            print(f"Informações do produto {nome_produto}:")
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            return
    print(f'Produto {nome} não encontrado.')


# Cadastro de produtos
cadastrar_produto('Camiseta', 29.99, 50)
cadastrar_produto('Tênis', 99.99, 30)
cadastrar_produto('Mochila', 49.99, 20)

# Listagem inicial de produtos
listar_produtos()

# Atualização de estoque
atualizar_estoque('Camiseta', 10)

# Consulta de produto
consultar_produto('Tênis')

# Listagem após as operações
listar_produtos()

"""
O \n serve para mostrar o título na impressão.
"""
