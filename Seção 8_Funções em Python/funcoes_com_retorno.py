"""
FUNÇÕES COM RETORNO

A função deve ser isolada dentro do código com duas linhas de espaçamento em cima e em baixo.
"""

# Importando para a função jogar_moeda
from random import random

print('Relembrando ---------------------------------------------------------------------------------------------------')

numeros = [1, 2, 3]
ret = numeros.pop()
print(f'retorno de pop: {ret}')

ret_pr = numeros
print(f'Retorno de ret_pr: {ret_pr}')

"""
Repare que por conta de ret_pr não ser uma função de retorno, é impresso o valor None, pois não é dado nenhum valor 
resultante da função. A função não dá um retorno, ela dá uma impressão, entenda a diferênça.
"""

print('Exemplo de função -------------------------------------------------------------------------def quadrado_de_7():')

"""
ATENÇÃO: Agora que vamos estudar funções de retorno, necessita-se de uma mudança de vocabulário. O print não retorna 
valores, ele IMPRIME valores.
"""


def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()

print(f'Retorno: {quadrado_de_7()}')

"""
Como essa última função não é uma função de retorno, esperar um valor de retorno dela é errado, pois não existe um 
valor de retorno, existe um valor de impressão. Portanto, o retorno é None.
"""

print('Refatorando a função de cima ----------------------------------------------------------------------------return')

"""
Refatorar significa redefinir/reescrever uma função.
"""


def quadrado_de_6():
    return 6 * 6


retorno = quadrado_de_6()

print(f'Retorno: {quadrado_de_6()}')
print(f'Retorno: {retorno}')  # Tanto faz

"""
Criamos uma variável para receber o retorno da função e estamos imprimindo.
Repare que agora declaramos explicitamente que temos um valor/resultado para a função. 
Não precisamos necessáriamente para receber o retorno de uma função, podemos passar a execução da função para outras 
funções ou mesmo para outras funções.
"""

# Funções de retorno com contas
print(f'Retorno: {retorno + 1}')

print('Refatorando a função diz_oi ------------------------------------------------------------------------return "oi"')


def diz_eai():
    return 'eai'


print(diz_eai())
diz_eai()

"""
Dessa forma, ao invés de imprimir, a função RETORNA.
Se somente chamar a função, não será impresso nada, pois, no segundo caso não houve a instrução para impressão.
"""

print('Aplicação com junção de variáveis ------------------------------------------------print(diz_ola() + nome + "!")')


def diz_ola():
    return 'Olá, '


nome = 'Pedro'

print(diz_ola() + nome + '!')

"""
Se usassemos uma função sem retorno, na hora de concatenar a função com a(s) variável(is) e string(s) daria erro.

OBS: 
Sobre a palavra reservada RETURN

1 - Ela finaliza a função, ou seja, ela sai da execução da função.
2 - Podemos ter em uma função diferentes returns, mas ela só vai executar um.
3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores.
"""

print('Return como finalizador da função -----------------------------------------------------------------------------')


def say_my_name():
    print('Eu sou impresso')
    return 'Heiserberg'
    # print('Eu não sou impresso')


"""
Comentei a última linha para não deixar nenhum erro no código. Mas a ideia é essa: tudo que estiver no bloco da 
função após o return não é impresso.
"""

print(say_my_name())

print('Usando if/elif/else ----------------------------------------------------------------------if variavel: return 4')


def nova_funcao():
    variavel = False
    if variavel:  # is True
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())

"""
Eu poderia não ter escrito o else, mas eu ainda gosto dele e acho que ele deixa mais claro o código.
Tome cuidado com essas funções que as vezes por causa de besteira a gente acaba gastando muito tempo à toa.
Nessa função, está sendo passado um valor a variável e atribuindo a tomadas de decisões do if/else/elif.
"""

print('Utilizando uma Tupla na função de retorno -------------------------------------------------------return x, y, z')


def outra_funcao():
    return 2, 4, 6, 8


print(outra_funcao())
print(type(outra_funcao()))

print('Função para jogar uma moeda ----------------------------------------------from random import random // random()')


def joga_moeda():
    valor = random()  # Gera um valor pseudo-randômico
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(f'A face que saiu na moeda é {joga_moeda()}')

"""
Para utilizar uma função randômica, precisamos importar a bibioteca ramdom, como fizemos no início. Mais pra frente, 
trabalharemos mais profundamente sobre as bibliotecas.
"""

print('Refatorando o código ------------------------------------------------------------------------------------------')


def joga_moeda2():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(f'A face que saiu na moeda é {joga_moeda2()}')

"""
O random() é uma função, e não precisa ser igualada a uma variável. Economizamos uma linha de código.
Os valores de um random e outro dentro do código são independentes.
"""

print('Erros comuns na utilização do retorno -------------------------------------------')

"""
Não são erros própriamente ditos, mas sim, redundâncias o linhas que podem ser tiradas do código.
"""


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    #  else:
    return False


print(eh_impar())

"""
Na def acima, como já mostrado anteriormente, é recomendável não usar o else, pois não é necessário em funções de 
retorno.
"""

print('Exercício 1 ----------------------------------------------------------def calcula_area_triangulo(base, altura):')

"""
Crie uma função chamada calcula_area_retangulo que recebe dois parâmetros, base e altura, e retorna a área do retângulo. 
Utilize a declaração return para retornar o resultado.
"""


def calcula_area_triangulo(base, altura):
    return f'O triangulo com a base medindo {base}cm e altura medindo {altura}cm é {base * altura / 2}cm²'


print(calcula_area_triangulo(5, 10))

print('Exercício 2 -----------------------------------------------------------------------------if n % 2 == 1: (impar)')

"""
Elabore uma função chamada verifica_numero_par que recebe um número como parâmetro e retorna True se o número for par e 
False se for ímpar. Utilize uma estrutura condicional e a declaração return para retornar o resultado.
"""


def verifica_numero_par(n):
    if n % 2 == 1:
        return f'{n} é um número impar'
    return f'{n} é um número par'


print(verifica_numero_par(5))

print('Exercício 3 ----------------------------------------------------if num1 > num2: / if num1 > num3: / return num1')

"""
Crie uma função chamada maior_numero que recebe três parâmetros, num1, num2 e num3, e retorna o maior entre eles. 
Utilize estruturas condicionais e a declaração return para retornar o resultado.
"""


def maior_numero(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        return num3
    elif num2 > num1:
        if num2 > num3:
            return num2
        return num3


print(f'O maior número é o {maior_numero(19, 6, 23)}')
