"""
LIST COMPREHENSION (PT.2)

Nós podemos adicionar estruturas condicionais lógicas às nossas list comprehensions.
"""

print('Utilizando if-----------------------------------------pares = [numero for numero in numeros if numero % 2 == 0]')

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]

impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

print('Refatorando -------------------------------------------pares = [numero for numero in numeros if not numero % 2]')

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

"""
Qualquer número par (% 2 == 0) e 0 em Python é False, mas not False é True.
Qualquer número ímpar (% 2 == 1) é True, pois o um é True
"""

print(pares)
print(impares)

print('Utilizando if else ------------------------------')

resultado = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(resultado)

"""
Para usar o else, é necessario colocar a expressão no início, antes do loop for.
"""

print('Exercício 1 ---------------------numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1))]')

"""
Filtragem de Números Primos

Considere a lista numeros fornecida no exemplo. Crie uma list comprehension para gerar uma nova lista contendo apenas 
os números primos dessa lista. Lembre-se de que um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
"""

numeros_primos = [numero for numero in numeros if numero > 1 and all(numero % i != 0 for i in range(2, int(numero **
                                                                                                           0.5) + 1))]
print(numeros_primos)

"""
Explicação: 
Neste exercício, utilizei a função all para verificar se o número é primo, percorrendo todos os valores de i de 2 até a 
raiz quadrada do número mais 1. Se o número for maior que 1 e não for divisível por nenhum desses valores, é considerado
primo e incluído na nova lista. O resultado é impresso para verificar se a list comprehension está filtrando 
corretamente os números primos da lista original
"""

print('Exercício 2 -------------------------------------------------------[numero for numero in numeros if numero > 0]')

"""
Números Negativos e Positivos

Utilizando a lista numeros novamente, crie duas list comprehensions separadas. A primeira lista deve conter apenas os 
números positivos e a segunda apenas os números negativos da lista original.
"""

numeros_positivos = [numero for numero in numeros if numero > 0]
numeros_negativos = [numero for numero in numeros if numero < 0]

print(numeros_positivos)
print(numeros_negativos)

print('Exercício 3 --------------------------[palavra.title() if len(numero) < 5 else palavra for palavra in palavras]')

"""
Transformação de Palavras

Dada a lista de palavras palavras = ['python', 'list', 'comprehension', 'if', 'else'], crie uma list comprehension para 
gerar uma nova lista onde cada palavra tenha o primeiro caractere em maiúsculo se a palavra tiver mais de 5 caracteres, 
caso contrário, mantenha a palavra em minúsculo. Lembre-se de imprimir os resultados para verificar se as list 
comprehensions foram criadas corretamente.
"""

palavras = ['python', 'list', 'comprehension', 'if', 'else']

palavras_titulo = [palavra.title() if len(palavra) < 5 else palavra for palavra in palavras]
print(palavras_titulo)
