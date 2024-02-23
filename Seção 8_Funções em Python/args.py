"""
*ARGS

É um parâmetro especial de funções.
- É um parâmetro como outro qualquer. Isso significa que você poderá chama-lo de qualquer nomenclatura,
desde que começe com asterisco (*).

Ex: *xis
Mas por convenção, utilizamos *args para definí-lo.

O parâmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla. Entâo,
desde já, lembre-se que tuplas são imutáveis.
"""

print('Função simples ----------------------------------------------------------------def soma_todos_numeros(x, y, z):')


def soma_todos_numeros(x, y, z):
    return x + y + z


print(soma_todos_numeros(4, 7, 9))

"""
Nesse caso em que temos três argumentos e três parâmetros, funciona perfeitamente, mas se colocarmos mais ou menos 
argumentos, acaba dando TypeError. Mas se nós quisessemos adicionar n argumentos, precisariamos de métodos mais 
dinâmicos.
"""

print('Utilizando o *args -------------------------------------------------------------def soma_todos_numeros2(*args):')


def soma_todos_numeros2(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros2())
print(soma_todos_numeros2(1))
print(soma_todos_numeros2(2, 3, 4))
print(soma_todos_numeros2(5, 6, 7, 8, 600))

"""
O *args por si só, faz somente uma tupla, por isso precisamos usar o loop for para que fosse somado todos os 
argumentos contidos nele para realizar o calculo.
Mas podemos melhorar
"""

print('Utilizando o sum -------------------------------------------------------------------------------------sum(args)')


def soma_todos_os_numeros(*args):
    return sum(args)


print(soma_todos_numeros2(5, 6, 3, 23, 6, 43, 6, 2))

"""
Que função sagrada é o sum(), jamais esqueça dela.
"""

print('Podemos em uma mesma função ter valores obrigatórios e *args ---------------------def soma(nome, email, *args):')


def soma_todos_numeros3(nome, email, *args):
    return sum(args) / 2


print(soma_todos_numeros3('Randú', 'randujribeiro@gmail.com', 22, 6, 2000))

print('Exemplo de utilização do *args -----------------------------------if -condicão- in args and -condição2- in args')


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é...'


print(verifica_info())
print(verifica_info('Geek', 'University'))
print(verifica_info('Geek'))

print('Praticando ------------------------------------------------------------------------------if "12345678" in args:')


def verifica_senha(*args):
    if '12345678' in args:
        return 'Seja bem-vindo'
    elif '' in args:
        return 'Insira a sua senha'
    return 'Email ou senha incorretos, tente novamente'


print(verifica_senha(''))
print(verifica_senha('12345678'))
print(verifica_senha('87654321'))

print('Desempacotador do caminho das pedras -------------------------------------------------soma_tudo(1, 2, 3, 4 ...)')

"""
O args não consegue receber uma lista, somente consegue trabalhar com tuplas, porque a lista ele trata como um 
elemento só. É UMA lista. Mas temos como resolver isso.
"""


# Jeito que já sabemos:
def soma_tudo(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5]

a, b, c, d, e = numeros

print(soma_tudo(a, b, c, d, e))

print('Usando um desempacotador pythonico --------------------------------------------------------------------*numeros')


def soma_tudo2(*args):
    return sum(args)


numerais = [1, 1, 2, 3, 5, 8]

print(soma_tudo2(*numerais))

"""
O * serve para que informemos ao python que estamos passando como argumento uma coleção de dados. Desta forma ele 
saberá que ele precisará antes desempacotar esses dados.
Se ao invés de uma lista tivessemos uma tupla, daria o mesmo resultado. Já com dicionário não daria certo, 
mas vamos aprender a trabalhar com eles ainda.
"""

print('Exercício 1 -----------------')

"""
Crie uma função chamada calcula_media_args que aceita um número indefinido de argumentos e retorna a média aritmética 
desses números. Documente a função utilizando docstrings para explicar o propósito da função, os parâmetros (ou o uso 
do *args) e o que ela retorna. Teste a função com diferentes conjuntos de números.

# Exemplo de uso:
resultado1 = calcula_media_args(2, 4, 6)
resultado2 = calcula_media_args(10, 20, 30, 40, 50)
print(resultado1)  # Saída: 4.0
print(resultado2)  # Saída: 30.0
"""


def calcula_media_args(*args):
    return sum(args) / len(args)


resultado1 = calcula_media_args(2, 4, 6)
resultado2 = calcula_media_args(10, 20, 30, 40, 50)
print(resultado1)  # Saída: 4.0
print(resultado2)  # Saída: 30.0

print('Exercício 2 -----------------------------------------------------------------if all("Geek" in s for s in args):')

"""
Modifique a função verifica_info para aceitar um número indefinido de strings e retornar 'Bem-vindo Geek' apenas se 
todas as strings fornecidas contiverem a palavra 'Geek'. Caso contrário, retorne:
'Eu não tenho certeza de quem você é...'. 
Documente a função utilizando docstrings para explicar o propósito da função, o uso do *args e o que ela retorna. 
Teste a função com diferentes conjuntos de strings.

# Exemplo de uso:
resultado1 = verifica_info('Geek', 'University', 'Geeky')
resultado2 = verifica_info('Geek', 'Geeky', 'Geekster')
print(resultado1)  # Saída: 'Eu não tenho certeza de quem você é...'
print(resultado2)  # Saída: 'Eu não tenho certeza de quem você é...'
"""


def verifica_info(*args):
    if all('Geek' in s for s in args):
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é...'


# Exemplo de uso:
resultado1 = verifica_info('Geek', 'University', 'Geeky')
resultado2 = verifica_info('Geek', 'Geeky', 'Geekster')
print(resultado1)  # Saída: 'Eu não tenho certeza de quem você é...'
print(resultado2)  # Saída: 'Eu não tenho certeza de quem você é...'

print('Exercício 3 ----------------------------')

"""
Crie uma função chamada concatena_strings_args que aceita uma string inicial e um número indefinido de strings 
adicionais como argumentos. A função deve retornar a string resultante da concatenação de todas as strings. 
Documente a função utilizando docstrings para explicar o propósito da função, o uso do *args e o que ela retorna. 
Teste a função com diferentes conjuntos de strings.

# Exemplo de uso:
resultado1 = concatena_strings_args('Olá', ' ', 'mundo', '!')
resultado2 = concatena_strings_args('Python', ' é', ' uma', ' linguagem', ' incrível')
print(resultado1)  # Saída: 'Olá mundo!'
print(resultado2)  # Saída: 'Python é uma linguagem incrível'
"""


def concatena_strings_args(string, *args):
    return string + ''.join(args)


resultado1 = concatena_strings_args('Olá', ' ', 'mundo', '!')
resultado2 = concatena_strings_args('Python', ' é', ' uma', ' linguagem', ' incrível')
print(resultado1)  # Saída: 'Olá mundo!'
print(resultado2)  # Saída: 'Python é uma linguagem incrível'

"""
Nunca mais se esqueça do ''.join(lista) para juntar palavras de uma lista de palavras.
"""
