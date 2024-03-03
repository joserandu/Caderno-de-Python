"""
O BLOCO TRY/EXCEPT

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o programa
pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é

try:
    //Execução problemática
except:
    //o que deve ser feito em caso de problema

OBS: Esse código ficou problemático propositalmente para que sejam mais bem exemplificados os tipos de erros.
"""

print('Tratando o erro genérico -------------------------------------------------------------------------------except:')

"""
try:
    geek()
except:
    print('Deu algum problema')
"""
"""
O programa passa a mensagem de erro, e segue o seu funcionamento.
Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre tratar de forma específica.
"""

print('Tratando um erro específico ------------------------------------------------------------------except NameError:')

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente.')

"""
Isso servirá para tratar o NameError, se quisesse tratar outro tipo, é só especificar.
"""

print('TypeError ----------------------------------------------------------------------------except TypeError as erro:')

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

"""
Essas mensagens de erro a gente costuma guardar no log da aplicação ou no banco de dados.
"""

print('NameError -----------------------------------------------------------------------------except NameError as err:')

try:
    print(f'Geek'[9])
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print(f'Deu um erro diferente')

print('try/except dentro de uma função ----------------------------------------------def soma(x, y): try: return x + y')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'Geek'}

print(pega_valor(7, 'game'))

"""
O KeyError e o TypeError foram tratados.
"""

print('Exercício 1 --------------------------------------------------------------------------except ZeroDivisionError:')

"""
Escreva uma função chamada divide que recebe dois números como entrada e retorna o resultado da divisão do primeiro 
número pelo segundo. Utilize um bloco try para lidar com a possibilidade de divisão por zero. Se ocorrer uma divisão 
por zero, exiba uma mensagem ao usuário informando que a divisão por zero não é permitida.
"""


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return f'impossível, pois nenhum número é divisível por zero'


num1 = 5
num2 = 0

print(f'O resultado da divisão entre {num1} e {num2} é {divide(num1, num2)}.')

print('Exercício 2 ---------------------------------------------------------------------------------except IndexError:')

"""
Crie uma função chamada lista_elemento que recebe uma lista e um índice como entrada e retorna o elemento da lista no 
índice especificado. No entanto, utilize um bloco try para lidar com índices que estejam fora do intervalo válido para 
a lista. Se um índice inválido for fornecido, a função deve retornar None.
"""

lista = [11, 22, 33, 44, 55, 66, 77]


def lista_elemento(i):
    try:
        return f'é o {lista[i]}'
    except IndexError:
        return f'não existe na lista'


busca = 8
print(f'O elemento que você procura {lista_elemento(busca - 1)}')

print('Exercício 3 -------------------------------------------')

"""
Escreva uma função chamada converte_para_inteiro que recebe uma string como entrada e tenta convertê-la para um número 
inteiro. Utilize um bloco try para lidar com casos em que a string fornecida não seja um número inteiro válido. Se a 
conversão não for possível, a função deve retornar None.
"""


def converte_para_inteiro(string):
    try:
        return int(string)
    except ValueError:
        return f'Não foi possível converter "{string}" para um número inteiro.'


dado_recebido = 'r'
print(converte_para_inteiro(dado_recebido))
