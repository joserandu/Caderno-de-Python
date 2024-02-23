"""
MAP

Com Map fazemos mapeamento de valores para função.
"""

import math

"""
Lembre-se de colocar a importação de uma biblioteca antes do resto da codificação para respeitar a PEP8.
"""

print('Nova biblioteca: math ------------------------------------------------------------------------------import math')

"""
Importamos essa biblioteca para trazer o valor de pi. Para não escrevermos ele diretamente na função, é só importar 
da biblioteca e escrever em seu lugar: math.pi.
"""

print('Área da cicunferência -----------------------------------------------------------------------math.pi * (r ** 2)')


def area(raio):
    return math.pi * (raio ** 2)


print(area(3))

"""
Antes de colocar como parametro da função 'raio', estava r, o que alertou que estava sendo infringindo a PEP8. 
Portanto, nunca deixe uma letra somente como parametro, por mais intuitiva que ela seja, como nesse caso.
"""

print('Calculando vários raios --------------------------------------------------for r in raios: areas.append(area(r))')

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

"""
PASSO A PASSO:
- Declaramos a lista de raios;
- Declaramos uma lista vazia;
- Declaramos o loop for/in para que sejam cauculadas todos os elementos;
- Trazemos para dentro do loop a lista areas acompanhada do método append() para que sejam adicionados valores à ela.
- Trazemos a função area com o argumento r para ser calculado dentro da função.
- Esse processo é repetido varias vezes até acabar os elementos da lista.
"""

print('Map -----------------------------------------------------------------------------------map(<funcao>, <iterável>')

areas1 = map(area, raios)
lista_areas1 = list(areas1)
print(lista_areas1)

"""
- Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. area é uma função,definida 
anteriormente, e o segundo é uma lista, nesse caso.
- O map vai pegar cada um dos dados do iterável e vai mandar para a função um por um.

A princípio não estava dando certo, mas atribuindo uma variável para transformar o map em uma lista fazendo uso 
também do método list(), ficou mais claro o código e interpretável.
"""

print('Verificando classe --------------------------------------------------------------------------------------type()')

print(type(areas1))  # map

print('Outra forma de utilizar o list() -----------------------------------------------------------------print(list())')

print(list(areas1))

"""
Você deve pedir para listar usando o método list(), mas a partir de quando você o usa, ao usar de novo ele retorna 
uma lista vazia.

OBS: após utilizar a função map() depois da primeira utilização do resultado ele zera.
Isso é bom para limpar a memória.
"""

print('Para fixar map ----------------------------------------')

"""
- Temos dados iteráveis:
- dados: a1, a2, ..., an
- Temos uma função:
- Função: f(x)
- Utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função.
- o Map Object: f(a1), f(a2), f(...), f(an).
"""

"""
No exemplo abaixo vamos listar algumas cidades e as suas respectivas temperaturas médias em uma lista formada por 
tuplas. Mas queremos passar todas as temperaturas para Farenheit. Para isso, podemos usar maps, pois temos uma função 
para ser aplicada em um iterável.
Fórmula: f = 9 / 5 * c + 32
"""

# Iterável
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26)]  # lista de tuplas
print(cidades)

# Map
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))  # Poderia ser uma tuple também.

"""
O professor mostrou assim: c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
Não faça isso. A ideia principal de uma função anônima é justamente não ter nome, por isso, fica contraditório a 
teoria, resultando em erro.
"""

print('Exercício 1 ---------------------------------------------------------------list(map(caucular_quadrado, numeros)')

"""
1. Crie uma lista de números, por exemplo: numeros = [1, 2, 3, 4, 5].
2. Defina uma função chamada calcular_quadrado que recebe um número como argumento e retorna o quadrado desse número.
3. Utilize a função map para aplicar a função calcular_quadrado a cada elemento da lista de números.
4. Imprima a lista resultante contendo os quadrados dos números.
5. Dica: Se necessário, converta o objeto map para uma lista para visualizar o resultado.
"""

numeros = [1, 2, 3, 4, 5]


def caucular_quadrado(numero):
    return numero ** 2


print(list(map(caucular_quadrado, numeros)))

print('Exercício 2 ------------------------------------------------------------------------------nome.replace(" ", "")')

"""
1. Vamos supor que temos uma lista de nomes e queremos criar usernames a partir desses nomes, removendo espaços e 
convertendo para letras minúsculas.
2.Crie uma lista de nomes, por exemplo: nomes = ["João Silva", "Maria Souza", "Carlos Oliveira", "Ana Pereira"].
3. Defina uma função chamada gerar_username que recebe um nome como argumento, remove espaços e converte para letras 
minúsculas, e retorna o resultado.
4. Utilize a função map para aplicar a função gerar_username a cada elemento da lista de nomes.
5. Imprima a lista resultante contendo os usernames.
6. Dica: Se necessário, converta o objeto map para uma lista para visualizar o resultado.
"""

nomes = ["João Silva", "Maria Souza", "Carlos Oliveira", "Ana Pereira"]


def gerar_username(nome):
    return nome.replace(" ", "").lower()


print(list(map(gerar_username, nomes)))

"""
CURIOSIDADE:

Para tirar os acentos de uma string, utilizamos a biblioteca 'unidecode', e para instalar usamos os comandos: pip 
install unidecode, e o nosso código fica assim:

from unidecode import unidecode  # importação depois da instalação

nomes = ["João Silva", "Maria Souza", "Carlos Oliveira", "Ana Pereira"]


def gerar_username(nome):
    return unidecode(nome.replace(" ", "").lower())  # unidecode()


"""
