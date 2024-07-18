"""
DEFININDO FUNÇÕES

É um dos pilares da programação em geral.
- Funções são pequenas partes de código que realizam tarefas específicas.
- Pode ou não receber entrada de dados e retornar uma saída de dados.
- Sâo muito úteis para executar procedimentos similares repetidas vezes.

OBS: Se você escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada.

Já utilizamos várias funções desde que inciamos o curso: print(), len(), max(), min(), count(), entre outras.
"""

print('Funções que suportam qualquer tipo de dado -------------------------------[1, 1.4, True, None, False, "python"]')

cores = ['verde', 'amarelo', 'azul', 'branca']
print(cores)  # imprime uma lista

curso = 'Programação em Python: Essencial'
print(curso)  # imprime uma string

"""
Repare que a função print() não liga para qual é o tipo de dado que é enviado para ele, somente executa.
"""

print('Funções que não aceitam qualquer tipo de dado --------------------------------------------------------.append()')

cores.append('laranja')
print(cores)

print('Funções que não aceitam dados de entrada --------------------------------------------------------------.clear()')

cores.clear()
print(cores)

"""
Veja que após o chamado do método nas opções de atalho aparece clear(self).

ATENÇÃO:
Função é um bloco de código que realiza algumas tarefas, já o método é caracterizado por vir depois do .; ex: .append()
"""

print('Origem dos métodos do Python ----------------------------------------------------------------------------help()')

print(help(print))

"""
- Agora imagine se não houvesse esses métodos e a gente precisasse fazê-los do zero.
- Com essa função help(), a gente consegue entender mais ou menos como foi feito.
"""

print('Princípio do DRY: Don`t Repeat Yourself (Não repita você mesmo) --------------------------------------------DRY')

"""
Também pode ser chamado de não repita o seu código, a ideia é que você não precise ficar repetindo linhas de código.
"""

print('Definindo funções ------------------------------------------------------------------------------------------def')

"""
Forma geral:
def nome_da_funcao(parâmetros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> também chamado de corpo da função ou implementação, é onde o implementamento da função acontece. 
Neste bloco, pode ter ou não retorno da função;

OBS: Veja que para definir uma função usamos a palavra 'def' informando ao Python que estamos definindo uma função. 
Também abrimos o bloco de código com o já conhecido dois pontos ':'
"""

print('')
print('Definindo a primeira função -----------------------------------------------------------------------------------')

# Definição


def diz_oi():
    print('oi!')


"""
OBS: 
1 - Veja que dentro das nossas funções podemos utilizar outras funções.
2 - Perceba que a nossa função só executa uma tarefa, ou seja, imprime 'oi'.
3 - Veja que essa função não recebe nenhum parâmetro de entrada. (O parâmentro de entrada pode ser uma variável)
4 - Essa função não retorna nada, pois ela só foi criada, mas não foi chamada.
"""

# Chamada de execução
diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar parênteses à frente do nome da função para executá-la.
"""

print('Mais um exemplo -------------------------------------------------------------------------def cantar_parabens():')


def cantar_parabens():
    print('Parabéns pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


cantar_parabens()
cantar_parabens()

"""
Essa função será executada o tanto de vezes que a gente chamar.
"""

print('Usando for in para facilitar a nossa vida ---------------------------------for n in range(2): cantar_parabens()')

for n in range(2):
    cantar_parabens()

print('Igualando uma função à uma variável e chamando -----------------------------------------canta = cantar_parabens')

canta = cantar_parabens  # Sem parentesis
canta()  # Com parêntesis

"""
Nâo é muito comum usar essa forma, mas fique com mais esse ensinamento.
"""

print('Exercício 1 ----------------------')

"""
 Identificação de Conceitos

Responda às seguintes perguntas com base nas anotações de aula:

Qual a definição de função apresentada nas anotações?
    São blocos de código que tem por finalidade realizar operações lógicas e processoais dentro da lógica da aplicação.
Quais são as características principais das funções em Python?
    Visualmente, iniciam o seu bloco de código com def, o nome da função, contendo apenas letras minúsculas e 
    underline (SNACK CASE), os parâmetros e em seguida o bloco de código a ser executado sempre que a função for 
    chamada. As funções tem por caracteristicas fazerem desenvolvimentos lógicos de partes específicas do código, como 
    calculos, e processamento de dados.
Por que é recomendado não ter funções com várias tarefas diferentes?
    Porque deixar uma função com várias tarefas acaba deixando a lógica da função muito mais complexa, 
    o que dificulta o entendimento posterior do código.
Qual a função do método .append() em listas?
    O método append() tem por finalidade adicionar elementos ao final de uma lista.
O que o método .clear() faz em listas?
    O método .clear() tem por finalidade esvaziar a lista.
"""

print('Exercício 2 -----------------------------------------')

"""
Aplicação Prática

Crie uma função chamada saudacao que recebe o nome de uma pessoa como parâmetro e imprime uma mensagem de saudação 
personalizada, como "Olá, [nome]! Como você está?". Em seguida, chame essa função duas vezes, passando nomes diferentes 
como argumento.
"""


def saudacao(nome):
    print(f'Olá, {nome}! Como você está?')


saudacao('Ana')
saudacao('Scarlet')

print('Exercício 3 --------------------------')

"""
Análise de Código

Analise o seguinte trecho de código:

def soma(a, b):
    resultado = a + b
    return resultado

x = 5
y = 10
z = soma(x, y)
print(z)

1. Explique o que esse código faz.
    Esse código tem como função somar o número x com o y.
2. Modifique a função soma para aceitar um terceiro parâmetro opcional chamado c e somar esse terceiro valor à soma de 
a e b. Caso c não seja fornecido, a função deve realizar a soma apenas de a e b.
    
3. Chame a função soma com dois valores e imprima o resultado, em seguida, chame a função com três valores e imprima o 
novo resultado.
"""

# 2.


def soma(*args):
    resultado = sum(args)
    return resultado


print(soma(5, 10))
print(soma(5, 10, 7))

"""
Nesse caso poderia também ser usado o dado do tipo None:
def soma(a, b, c=None):
    if c is not None:
        resultado = a + b + c
    else:
        resultado = a + b
    return resultado
    
Claro que na prática você vai usar o *args, mas é interessante saber também.
"""
