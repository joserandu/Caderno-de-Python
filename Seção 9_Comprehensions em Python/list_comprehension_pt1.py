"""
LIST COMPREHENSION

Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

Sintaxe da list comprehension:
[ função for dado in iterável ]  # Para cada dado nessa coleção de dados, será gerada uma nova lista.
"""

print('Exemplo 1 ---------------------------------------------------------------------[<função> for <dado> in <lista>]')

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
Comando: Multiplique 10 PARA cada número EM numeros.
- Repare que não precisa declarar o que é numero.

Para entender melhor o que está acontecendo precisamos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros.
- A segunda parte: numero * 10.
"""

print('Utilizando list comprehension com divisão ----------------------------------------------[numero / x for x in A]')

res2 = [numero / 2 for numero in numeros]
print(res2)

print('List comprehension com função -------------------------------------------[funcao(numero) for numero in numeros]')


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]

print(res3)

"""
- O que foi criado aqui foi uma função que eleva todos os elementos de numeros ao quadrado.
- O comando é que para a função será passado cada um dos elementos da lista numeros.
- EXECUTE a funcao() PARA cada numero EM numeros.
"""

print('List comprehension vs loop ------------------------------------------------------------------------------------')

print('Loop for ---------------------------------------------------------------numeros_dobrados.append(numero_dobrado)')

# Loop
numeros2 = [1, 2, 3, 4, 5]

numeros_dobrados = []

for num in numeros2:
    numero_dobrado = num * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

"""
PASSO A PASSO:
- Declaração da lista;
- Declaração da segunda lista na qual será armazenado os resultados;
- Declaração do for/in chamando a primeira lista;
- Chamado da segunda lista e declaração da lógica da função;
- Uso da função append() para adicionar os valores já modificados;
"""

print('List comprehension ----------------------------------------------------------------[num * 2 for num in numeros]')

print([num * 2 for num in numeros2])  # Só.

print('Usando apenas uma linha ------------------------------------------------------[num * 2 for num in [x, y, z, w]]')

print([num * 2 for num in [1, 2, 3, 4, 5]])

"""
É um loop de somente uma linha. É muito simples. É interesantíssimo ter o domínio dessa ferramenta, pois pode fazer 
a aplicação ganhar mais desempenho e diminuir o tempo de códificação.
Isso é python AVANÇADO.
"""

print('List Comprehension nas Strings -----------------------------------------------[letra.upper() for letra in nome]')

nome = 'Geek University'

print([letra.upper() for letra in nome])

"""
Separa as letras e as deixa maiúsculas.
"""

print('Passando mais de uma string para a list comprehension ------------------------[letra.upper() for letra in nome]')

nome = 'Geek University', 'usp'

print([letra.upper() for letra in nome])

"""
- Não se esqueça das chaves [].
- O Python aqui foi mais inteligente que o professor imaginou nessa. Quando passamos uma string, será retornada uma 
lista de letras, mas se houver mais de uma string, será devolvida uma lista de strings.
"""

amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

print([amigo.upper() for amigo in amigos])

print('List conprehension com range() -----------------------------------------------[num * x for num in range(1, 10)]')

print([number * 3 for number in range(1, 10)])  # [1, 9]

print('Transformando elementos em boolean -----------------------------------------------------------------bool(valor)')

print([bool(valor) for valor in [0, [], '', 'd', ' ', True, 1, -2.89, 4]])

"""
- Valores True: True, numeros e strings (até com caracteres especiais);
- Valores False: 0, e vazios em geral. 
"""

print('Transformando numeros em strings -------------------------------------------------------------------str(numero)')

print([str(numero) for numero in [1, 2, 3, 5, 6]])

print('Exercício 1 ----------------------------------------[numero ** indice for indice, numero in enumerate(numeros)]')

"""
Multiplicação por Potências de 2

Considere a lista numeros fornecida no exemplo. Crie uma list comprehension para gerar uma nova lista onde cada número 
seja multiplicado pela potência de 2 correspondente ao índice na lista. Ou seja, o primeiro número será multiplicado por 
2 elevado à potência de 0, o segundo número por 2 elevado à potência de 1, e assim por diante.
"""

numeros = [1, 2, 3, 4, 5]

potencias = [numero * (2 ** indice) for indice, numero in enumerate(numeros)]
print(potencias)

"""
Lembre-se da função enumerate() quando for trabalhar com elementos da lista.
A chave vem antes do valor.
"""

print('Exercício 2 -------------------------------------------------[numero for numero in numeros2 if numero % 2 != 1]')

"""
Filtragem de Números Pares

Utilizando a lista numeros2 do exemplo que contém números de 1 a 5, crie uma list comprehension para gerar uma nova 
lista contendo apenas os números pares dessa lista.
"""

numeros2 = [1, 2, 3, 4, 5]  # Apagar depois

numeros_pares = [numero for numero in numeros2 if numero % 2 != 1]
print(numeros_pares)

"""
Vivendo e aprendendo. Pode colocar o if a frente do iterável.
"""

print('Exercício 3 ------------------------------------------[f"Amigo: {amigo}" for amigo in amigos if len(amigo) > 5]')

"""
Concatenação de Strings com Condição

Dada a lista de amigos fornecida (amigos), crie uma list comprehension para gerar uma nova lista onde cada amigo seja 
representado por uma string no formato "Amigo: <Nome do Amigo>". No entanto, inclua apenas os amigos cujo nome tenha 
mais de 5 caracteres.
"""

amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

os_de_verdade = [f'Amigo: {amigo}' for amigo in amigos if len(amigo) > 5]
print(os_de_verdade)
