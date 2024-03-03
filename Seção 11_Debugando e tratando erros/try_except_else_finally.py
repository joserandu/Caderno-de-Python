"""
TRY, EXCEPT, ELSE, FINALLY

Dica de quando e onde tratar código:

TODA ENTRADA DE DADOS DEVE SER TRATADA!
O que o usuário quer, na sua mente de programador, é DESTRUIR o seu sistema.
"""

print('Sem tratar o erro -------------------------------------------------------------------num(int(input("Idade: ")))')

num = int(input(f'Informe um número: '))
print(f'Vocé digitou o {num}')

"""
Se digitar uma string que não pode ser transformada em um número, o usuário destruiu o seu sistema.
"""

print('Utilizando o tratamento de erros ---------------------------------------------------------try: saida = int(num)')

num = input('Informe um número: ')

try:
    saida = int(num)
    print(f'Você digitou o {saida}')
except ValueError:
    print('Valor incorreto')

print('Utilizando o else --------------------------------------------------try: / num = int(input("informe o número"))')

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

"""
Perceba que o Try sempre é executado.

ELSE
É executado somente se não acontecer o erro. Em outras palavras, só entrará no bloco do else se passar pelo bloco do 
except.
"""

print('Finally -------------------------------------------------------------------try: -> except: -> else: -> finally:')

"""
O mais sem graça.
"""

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você digitou um número inválido.')
else:
    print(f'Você digitou o número: {num}')
finally:
    print('executando o finally')

"""
O bloco finally é sempre executado, independente se houve exceção ou não.
O finally, geralmente, é utilizado para fechar ou desalocar recursos.
"""

print('Else em funções -------------------------------------------------------------else: / print(dividir(num1, num2))')


def dividir(a, b):
    return a / b


num1 = input('Informe o primeiro número: ')
num2 = input('informe o segundo número: ')

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print('Digite um número válido')
else:
    print(f'A divisão entre {num1} e {num2} é {dividir(num1, num2)}')

print('Tratando erros dentro da função --------------------------------------------------------def dividir(a, b): try:')

"""
É a melhor forma de tratar erros.
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível fazer uma divisão por 0 (zero)'


num_a = input('Informe o primeiro número: ')
num_b = input('Informe o segundo número: ')

print(dividir(num_a, num_b))

"""
Esse ZeroDivisionError é inpressindível em sistemas que realizam contas.
Se passasemos ao inves de números, tuplas ou listas, seria ValueError, e o sistema ainda funcionaria.
"""

"""
Você pode fazer genericamente colocando o 'except:' apenas, e qualquer tipo de erro será tratado, mas não é o ideal. 
Utilize o semigenérico
"""

print('Tratamento de erro semigenérico ----------------------------------------except (ValueError, ZeroDivisionError):')

"""
É a forma mais recomendada.
Deve-se passar uma tupla e ainda um apelido.
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    except ZeroDivisionError:
        return 'Não é possível fazer uma divisão por 0 (zero)'


num_a = input('Informe o primeiro número: ')
num_b = input('Informe o segundo número: ')

print(dividir(num_a, num_b))

print('Exercício 1 --------------------------------------------------------------------else: {2024 - ano_de_nacimento}')

"""
Escreva uma função chamada calcula_idade que recebe o ano de nascimento de uma pessoa como entrada e retorna sua idade. 
Utilize um bloco try/except para lidar com a possibilidade de o usuário fornecer um ano inválido (por exemplo, um ano 
que não seja um número). Se o ano fornecido for inválido, a função deve retornar uma mensagem de erro adequada.
"""


def calcula_idade(ano_nascimento):
    try:
        ano_nascimento = int(ano_nascimento)
    except ValueError:
        return f'{ano_nascimento} não é um ano válido.'
    else:
        return f'A idade dessa pessoa é {2024 - ano_nascimento}.'


print(calcula_idade(1978))

print('Exercício 2 ----------------------------------------------------------------if numero % 2 == 0 / return "É par"')

"""
Crie uma função chamada verifica_numero_par que recebe um número como entrada e verifica se ele é par ou não. Utilize 
um bloco try/except para lidar com a possibilidade de o usuário fornecer um valor que não seja numérico. Se o valor 
fornecido não for numérico, a função deve retornar uma mensagem de erro adequada.
"""


def verifica_numero_par(numero):
    try:
        numero = int(numero)
        if numero % 2 == 0:
            return f'O número {numero} é par.'
        return f'O número {numero} é impar.'
    except ValueError:
        return f'"{numero}" não é par nem impar.'


num3 = 'macetando'
print(verifica_numero_par(num3))

print('Exercício 3 --------------------------------------------------------------------except (ValueError, TypeError):')

"""
Escreva uma função chamada calcula_raiz_quadrada que recebe um número como entrada e calcula sua raiz quadrada. Utilize 
um bloco try/except para lidar com a possibilidade de o usuário fornecer um valor negativo, o que resultaria em um erro 
ao tentar calcular a raiz quadrada de um número negativo. Se um valor negativo for fornecido, a função deve retornar 
uma mensagem de erro adequada.
"""


def calcula_raiz_quadrada(numero):
    try:
        numero = int(numero)
        if numero >= 0:
            return numero ** 0.5
        else:
            return f'O número {numero} é menor que zero, logo, não possui raiz quadrada.'
    except (ValueError, TypeError):
        return 'Digite um número válido.'


print(calcula_raiz_quadrada(-25))
