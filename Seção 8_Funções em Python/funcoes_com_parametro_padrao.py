"""
FUNCOES COM PARAMETRO PADRÃO (DEFAULT PARAMTERS)

- Funções onde a passagem de parâmetro seja opcional;
"""

print('Parametro opcional -------------------------------------------------------------------------------------print()')

"""
A função print() é um exemplo claro disso.
"""

print('Geek University')
print()

print('Parâmetro obrigatório -----------------------------------------------------------------------------------------')


def quadrado(numero):
    return numero ** 2


print(quadrado(3))


def exponencial(numero, potencia):
    return numero ** potencia


print(exponencial(2, 3))

"""
Em ambos os casos os a passagem de argumentos à função é obrigatória ao chamá-la.
"""

print('Parâmetros padrão com valor default -----------------------------------------------------------------potencia=2')

"""
Agora imagine se o usuário coloque em uma função um número, ele seria elevado ao quadrado, mas se ele colocar dois 
números, o primeiro seria elevado pelo segundo.
"""


def exponencial(numero=4, potencia=2):  # A mágica está aqui.
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3))
print(exponencial())

"""
Com esse potencia=2 como parâmetro, o valor 2 fica como padrão se não for passado nenhum número como argumento.
O 4 também é padrão.
"""

print('A ordem dos parâmetros importa ------------------------------------------------------------------------(a, b=2)')


def teste(potencia, b=2):  # A ordem importa.
    return b ** potencia


print(teste(5, 3))

"""
O Valor default SEMPRE VEM DEPOIS porque se vier antes, acaba dando erro.
"""


def soma(x=1000, y=500):
    return x + y


print(soma(300, 750))
print(soma(599))
print(soma(400 + 1200))  # Primeira casa.

print('Exemplo com if/elif/else ------------------------------------def mostra_informacao(nome="Geek", instrutor=False')


def mostra_informacao(nome='Geek', instrutor1=False):
    if nome == 'Geek' and instrutor1:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Seja bem vindo {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor1=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

"""
Usamos parâmetros default por:

- Deixam a função mais fleixível.
- Evita erros com parâmetros incorretos.
- Nos permite trabalhar com exemplos mais legíveis de códigos.
"""

print('Tipos de dados que podemos utilizar como valores default para parâmetros -----------------------------quaisquer')

"""
Qualquer tipo de dado, até mesmo funções podem ser parâmetros.
"""


def diz_oi():
    return 'oi'


variavel = diz_oi()
print(variavel)

print('Usando funções como parâmetro -----------------------------------------------------------def mat(x, y, c=soma):')


def soma(x, y):
    return x + y


def mat(x, y, c=soma):
    return c(x, y)


def subtracao(x, y):
    return x - y


print(mat(2, 3))
print(mat(2, 3, subtracao))  # *Sem parêntesis.

"""
*A ausência de () em frente a função subtração nos argumentos se deve ao fato de que a função ser um argumento nesse 
caso, não sendo necessário indicar que é uma função, importa apenas o retorno dela.
"""

print('Escopo de variáveis globais e locais ------------------------------------------def diz_oi(): / instrutor = "py"')

instrutor = 'Geek'  # Escopo global


def diz_oi():
    instrutor2 = 'Python'  # Escopo local
    return f'Olá, {instrutor2}'


print(diz_oi())

"""
Eu coloquei nomes diferentes para as variaveis para respeitar a PEP8, mas o resultado é o mesmo.
O Python dá mais preferência para variáveis do escopo local do que do geral. Repare que o valor da variável do escopo 
global foi ignorada, e a que foi utilizada foi a do escopo local. A local tem preferência.
"""


def diz_ola():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_ola())

"""
Se for possível, EVITE variáveis globais.
"""

print('Trazendo variáveis do escopo global para o local --------------------------------------------------------global')

total = 0


def incrementa():
    global total  # É um aviso.
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

"""
O comando global é o que faz a mágica acontecer: ela avisa que estamos puxando de uma variável global. Mas novamente, 
EVITE construir códigos com variáveis no escopo global.
"""

print('Funções declaradas dentro de outras funções -----------------------------------------------------------nonlocal')

"""
Podemos ter funções que são declaradas dentro de funções e também tem uma forma especial de escopo de variável.
Não é comum ver isso, mas você pode tirar aprendizado.
"""


def fora():
    contador = 0
    def dentro():
        nonlocal contador  # variável não local
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

"""
nonlocal avisa que não é uma variável local, ela vem de um escopo acima.
Não é possível imprimir a função dentro(), pois ela não está declarada no escopo global, está no escopo da função.
"""

print('Exercício 1 -------------------------------')

"""
Crie uma função chamada calcula_potencia que aceita dois parâmetros: base e expoente. Essa função deve calcular e 
retornar a potência da base elevada ao expoente. Utilize valores padrão para base=2 e expoente=3. Teste a função 
chamando-a com diferentes conjuntos de argumentos.

# Exemplo de uso:
resultado1 = calcula_potencia(2, 3)
resultado2 = calcula_potencia(5)  # Usando valor padrão para expoente
resultado3 = calcula_potencia()   # Usando valores padrão para base e expoe
"""


def calcula_potencia(base=2, expoente=3):
    return base ** expoente


resultado1 = calcula_potencia(2, 3)
resultado2 = calcula_potencia(5)
resultado3 = calcula_potencia()

print(resultado1)
print(resultado2)
print(resultado3)

print('Exercício 2 -------------------------------------')

"""
Modifique a função mostra_informacao para aceitar um novo parâmetro chamado linguagem, que terá o valor padrão 'Python'.
A função deve retornar mensagens personalizadas com base na combinação de nome, instrutor1 e linguagem. Teste a função 
com diferentes argumentos.

# Exemplo de uso:
print(mostra_informacao())                               
print(mostra_informacao(instrutor1=True))                 
print(mostra_informacao('Ozzy', linguagem='JavaScript'))
"""


def mostra_informacao2(nome='Geek', instrutor1=False, linguagem='Python'):
    if nome == 'Geek' and instrutor1:
        return f'Bem-vindo instrutor Geek, nos seus dados consta que a sua linguagem de programação é {linguagem}'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Seja bem vindo {nome}, nos seus dados consta que a sua linguagem de programação é {linguagem}'


print(mostra_informacao2())
print(mostra_informacao2(instrutor1=True))
print(mostra_informacao2('Ozzy', linguagem='JavaScript'))

print('Exercício 3 -------------------------------')

"""
Crie uma função chamada contagem_global que incrementa uma variável global chamada contador a cada chamada. Utilize a 
declaração global dentro da função para acessar e modificar a variável global. Teste a função chamando-a várias vezes e 
exiba o valor do contador.

# Exemplo de uso:
print(contagem_global())  
print(contagem_global()) 
print(contagem_global())
"""

contador = 0


def contagem_global():
    global contador
    contador = contador + 1
    return contador


print(contagem_global())
print(contagem_global())
print(contagem_global())
