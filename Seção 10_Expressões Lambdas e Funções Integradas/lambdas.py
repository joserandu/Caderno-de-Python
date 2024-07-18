"""
EXPRESSÕES LAMBDAS

Conhecidas como expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, FUNÇÃO ANÔNIMAS.
"""

print('Função normal ----------------------------------------------------------------------------------------------def')


def funcao(x):
    return 3 * x + 1


print(funcao(5))

print('A estrutura da Expressão Lambda ------------------------------------------------------------lambda x: 3 * x + 5')

"""
lambda x: 3 * x + 1. Esse não é o jeito de se organizar, pois até dá erro. O jeito mais certo é dentro de expressões 
ou de declarações como veremos mais adiante.
"""

print('Função lambda dentro de uma variável ---------------------------------------------cauculo = lambda x: 3 * x + 2')

"""
Eu comentei tudo que está a frente porque o jeito no qual foi utilizado os lambdas em aula é errôneo e é apenas 
<<<<<<< HEAD
<<<<<<< HEAD
aproveitavel dessa parte o aprendizado da sintaxe, por isso não exclui essa parte da aula.
=======
aproveitavel dessa parte o aprendizado da semantica, por isso não exclui essa parte da aula.
>>>>>>> 8db86c2 (Venv)
=======
aproveitavel dessa parte o aprendizado da sintaxe, por isso não exclui essa parte da aula.
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61
"""

"""
calculo = lambda x: 3 * x + 1

print(calculo(5))
print(calculo(25))


Perceba como o Lambda é essencialmente uma função anônima: Ao igualarmos o lambda à uma variável, 
<<<<<<< HEAD
<<<<<<< HEAD
estamos indiretamente dando nome à função, ou seja, você está inflinjindo a PEP8, mas o código roda nomalmente. 
=======
estamos indiretamente dando nome à função, ou seja, você está infrinjindo a PEP8, mas o código roda nomalmente. 
>>>>>>> 8db86c2 (Venv)
=======
estamos indiretamente dando nome à função, ou seja, você está inflinjindo a PEP8, mas o código roda nomalmente. 
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61


print('Expressões lambdas igualadas a variáveis com multiplas entradas --------------------------------lambda x, y, z:')

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina ', 'JOlie '))

amar = lambda: 'Como não amar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())  # Lembre-se dos (), é função.
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


- Para o azar da pureza desse código que eu sempre presei antes de subi-lo para o github, meu professor insistiu nesses 
exemplos nos quais ele iguala funções lambda à variáveis.
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61
- Lembre-se das primeiras aulas o .strip() serve para tirar os espaços. Lembra-se de striptease.
- .title() serve para deixar a primeira letra maiúscula.
- Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também. Mas se passarmos mais argumentos do 
que parametros teremos um TypeError.

<<<<<<< HEAD
=======
- Lembre-se das primeiras aulas o .strip() serve para tirar os espaços. Lembre-se de striptease.
- .title() serve para deixar a primeira letra maiúscula.
- Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também. Mas se passarmos mais argumentos do 
que parametros teremos um TypeError.
>>>>>>> 8db86c2 (Venv)
=======
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61
"""

print('Funções lambdas para trabalhar com nomes -----------------------.sort(key=lambda: sobrenome.split(" ").lower())')

autores = ['Pepetela', 'Pedro Bandeira', 'Jorge Amado', 'Clarisse Lispector', 'G. Rosa', 'Machado de Assis',
           'João Cabral de Melo']

print(autores)

# Ordenando pelo sobrenome:

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""
Vamos por partes:
.sort() - Esse método serve para ordenar os valores.
key= - Essa função serve para mostrar um retorno da função, é como uma função de retorno, a partir dele é mostrado o 
resultado da função.
.split() - serve para tirar alguma parte da string.
[-1] - serve para indicar qual é a parte da string será trabalhada (no caso, o último nome).
.lower() - deixar todas as letras minúsculas.

Juntando tudo: como autores é uma lista será passado cada um dos nomes para a função para que ela execute. Perceba 
que após o lambda não colocamos um valor de entrada (ex. lambda x: <função>), a função toda ocorre após os dois pontos.

Com isso, a lista é organizada a partir da ordem alfabetica dos últimos nomes.

ESSE É O FORMATO MAIS COMUM DE VER UMA EXPRESSÃO LAMBDA.
"""

print('Função do segundo grau ------------------------------------------------ return lambda x: a * x ** 2 + b * x + c')

# Definindo a função


def geradora_funcao_quadratrica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


print(geradora_funcao_quadratrica(3, 0, 1)(2))

"""
Esse 2 na frente já indica o valor de x, que era o valor faltante na expressão, não pode tirar ele, pois da erro no 
código.

Para essa função colocamos a função anonima dentro de uma função normal para que pudessemos descobrir o valor de x 
através do envio de a, b, c.
"""

print('Exercício 1 ---------------------------------------------------(lambda base, altura: 0.5 * base * altura)(5, 8)')

"""
Criando Expressões Lambda

Crie uma expressão lambda que calcule a área de um triângulo, dados a base e a altura. Utilize as variáveis base e 
altura como parâmetros.
"""

resultado = (lambda base, altura: 0.5 * base * altura)(5, 8)
print(resultado)

print('Exercício 2 --------------------------------------------------------list(filter(lambda x: x % 2 == 0, numeros))')

"""
Filtrando uma Lista com Expressões Lambda

Dada a lista de números [1, 4, 7, 10, 13, 16, 19], utilize uma expressão lambda para criar uma nova lista contendo 
apenas os números pares.
"""

numeros = [1, 4, 7, 10, 13, 16, 19]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)

"""
A função filter() é assunto da próxima aula.
"""

print('Exercício 3 ----------------------------------------sorted(nomes, key=lambda nome: nome.split(" ")[-1].lower())')

"""
Ordenação Personalizada com Expressões Lambda

Dada a lista de strings nomes = ['Alice Silva', 'Bob Souza', 'Carlos Lima', 'Daniel Rocha'], utilize uma expressão 
lambda com a função sorted para ordenar a lista pelo último nome em ordem alfabética.
"""

nomes = ['Alice Silva', 'Bob Souza', 'Carlos Lima', 'Daniel Rocha']

<<<<<<< HEAD
<<<<<<< HEAD
nomes_ordenados = sorted(nomes, key=lambda nome: nome.split(' ')[-1].lower())

print(nomes_ordenados)
=======
nomes.sort(key=lambda nome: nome.split(' ')[-1].lower())

print(nomes)

# Usando sorted()
nomes_ordenados = sorted(nomes, key=lambda nome: nome.split(' ')[-1].lower())

print(nomes_ordenados)

"""
A função sorted também será estudada mais adiante.
"""
>>>>>>> 8db86c2 (Venv)
=======
nomes_ordenados = sorted(nomes, key=lambda nome: nome.split(' ')[-1].lower())

print(nomes_ordenados)
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61
