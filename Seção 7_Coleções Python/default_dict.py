"""
MÓDULO COLLECTIONS - DEFAULT DICT

Mais um container de alta performace.

Ao criar um dicionário utilizando o default dict nós informanmos um valor default, podendo utilizar um lambda para
isso. Esse valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não
existe, essa chave será criada e o valor default será atribuido.
"""

from collections import defaultdict

"""
Dessa vez, a coleção que vamos importar se chama defaultdict.
"""

print('Relembrando dicionários --------------------------------------------------------------------dicionario["curso"]')

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])

"""
Se colocar aqui uma chave que não existe, acontece um KeyError. Para evitar o KeyError, utilizamos o defaultdict.
"""

print('Utilizando o defaultdict -------------------------------------------------------------------------defaultdict()')

"""
OBS: lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores. Veremos com mais
detalhes mais para frente.
"""

dicionario2 = defaultdict(lambda: 'Valor não existente')
print(dicionario2)

"""
Criamos um dicionário sem valor nenhum.
Não se incomode com as marcações no inicio da impressão da linha por enquanto.
"""

dicionario2['curso'] = 'Programação em Python: Essencial'
print(dicionario2)

"""
Adicionamos a chave 'curso' e o valor 'Programação em Python: Essencial' no dicionário.
"""

print(dicionario2['outro'])
print(dicionario2)

"""
Usando uma chave que não existe na pesquisa, não será atribuido um KeyError, só será atribuido o valor declarado na 
função lambda à chave 'outro'.
"""

print('Exercício 1 -----------------------------------------')

"""
Criando um defaultdict com valores padrão diferentes

Crie um defaultdict chamado dicionario3 que utilize uma função lambda para atribuir o valor padrão "Chave não 
encontrada" para chaves ausentes. Adicione algumas chaves e valores a esse defaultdict e, em seguida, tente acessar uma 
chave que não foi previamente definida. Imprima o resultado.
"""

dicionario3 = defaultdict(lambda: 'Chave não encontrada')

dicionario3['1º'] = 'Andrey'
print(dicionario3)
dicionario3['2°'] = 'Bruno'
print(dicionario3)
dicionario3['3°'] = 'Carol'
print(dicionario3)

print(dicionario3['4°'])

print('Exercício 2 --------------------------------------------------')

"""
Modificando o valor padrão do defaultdict

Modifique o valor padrão do defaultdict dicionario2 para "Sem valor definido". Em seguida, adicione uma nova chave 
chamada 'linguagem' com o valor 'Python'. Tente acessar uma chave inexistente no defaultdict modificado e observe o 
resultado.
"""

dicionario2 = defaultdict(lambda: 'Sem valor definido')

dicionario2['linguagem'] = 'Python'

print(dicionario2['linguagem_preferida'])
print(dicionario2)

print('Exercício 3 -------------------------------------------')

"""
Utilizando um defaultdict com um contador

Crie um defaultdict chamado contador_palavras que utiliza uma função lambda para iniciar contagens de palavras com o 
valor padrão 0. Receba uma lista de palavras como entrada e use o defaultdict para contar a ocorrência de cada palavra. 
Imprima o resultado, exibindo cada palavra e sua contagem.
"""

# Função para contar as palavras


def contar_palavras(lista_palavras):
    contador_palavras = defaultdict(lambda: 0)

    # Contando as ocorrências de cada palavra
    for palavra in lista_palavras:
        contador_palavras[palavra] += 1

    # Imprimindo o resultado
    for palavra, contagem in contador_palavras.items():
        print(f'{palavra}: {contagem}')


# Lista de palavras de exemplo
palavras_exemplo = ['Python', 'é', 'uma', 'linguagem', 'poderosa', 'e', 'versátil', 'Python', 'é', 'amplamente',
                    'usado']

# Chamando a função com a lista de palavras
contar_palavras(palavras_exemplo)
