"""
DEBUGANDO COM PDB

PDB -> Python Debugger

Bug significa inseto
    No inicio os computadores eram gigantes e um dia um desses computadores estava com problemas no processamento dos
    dados e quando descobriram era uma mariposa presa em alguns componentes. Dai então surgiu o nome "BUG".
    Eu olhei no translate e a tradução é erro, mas tudo bem.

Em muitos casos a gente usa a função print para descobrir onde está os erros.
"""

import pdb

print('Jeito não aconselhável de debugar erros ----------------------------------------------------print(f"{a} e {b}")')


def dividir(a, b):
    print(f'a={a}, b={b}')  
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    except ZeroDivisionError:
        return 'Não é possível fazer uma divisão por 0 (zero)'


print(dividir(4, 7))

"""
Essa é uma prática ruim para debugar, existem formas mais profissionais de se fazer esse debug, utilizando o debugger 
em Python. Podemos fazer isso em diferentes IDEs, como o Pycharm ou utilizando o PDB - Python Debugger.
"""

print('Exemplo com o Pycharm --------------------------------------------------------<marca linha e clica na mariposa>')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
    except ZeroDivisionError:
        return 'Não é possível fazer uma divisão por 0 (zero)'


print(dividir(4, 7))

"""
1° - Marque as DUAS linhas nas quais você quer debbugar com um ponto vermelho do lado. (inicio do debug ao final)
2° - Depois com o botão direito você clica em Debug.

Repare todos os materiais que o pycharm possibilita para a gente descobrir os erros, ele mostra os valores de cada 
variável.

WATCHES

Se voce selecionar: int(a) / int(b) -> BD -> Watches
    Isso vai mostrar o valor da divisão.

Podemos colocar mais pontos de parada
"""

print('Quando não estamos editando com o pycharm ----------------------------------------import pdb / pdb.set_trance()')

"""
No Pycharm é o mais indicado, mas, por vezes, não estamos usando o pycharm, para isso utilizamos o Python 
Debugger (PDB).

Para utilizarmos o Python Debugger precisamos importar a biblioteca pdb (como já fizemos no inicio) e então utilizar a 
função set_trace().
"""

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso de ' + curso
print(final)

"""
Mostrou a linha seguinte.

Comandos básicos do PDB:

l - listar onde estamos no código
n - próxima linha (next)
p - imprime variável
c - continua a execução/finaliza o debug

Depois de listar, se colocarmos o nome da variável, é retornado para nós o valor.
Se no nosso caso colocamos a variável nome completo, vai aparecer como não definido, pois colocamos a função antes de 
definir essa variável. Para isso, colocamos o comando n, que vai dar mais uma linha ao nosso intervalo. E colocando o C 
a gente encerra o debug.

Perceba que o PDB é bem manual, diferente do Pycharm.

Porque usar o ; :
O debug é utilizado durante o desenvolvimento, mas depois que achou o problema você não vai mais usar ele. Costumamos 
realizar todos os imports de bibliotecas no início do arquivo, mas esse import a gente não vai postar quando estiver 
pronto, é só usar para descobrir o erro e acabou, então é só passar para a próxima linha.
"""

nome = 'Angelina'
sobrenome = 'Jolie'
# import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso de ' + curso
print(final)

"""
No Python 3.7 não é mais necessário importar a biblioteca PDB, pois o comando de debug foi incorporado como função 
bilt-in, ou seja, integrada, chamada break point.
"""

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso de ' + curso
print(final)


"""
Cuidado com os conflitos entre nomes de variáveis e os comandos do PDB.
"""


def soma(l1, n, p, c):
    breakpoint()
    return l1 + n + p + c


print(soma(1, 3, 5, 7))

"""
Desse jeito não dá pra saber o valor de l, n, p, c pelo debugger, só se colocar o p na frente. Ai os comando ficam: p l, 
por exemplo.

Mas sempre use nomes significativos, para não dificultar a sua vida, como um num1, num2, etc.
"""
