"""
Ranges

- Precisamos conhecer o loop for para conhecer os ranges.
- Precisamos conhecer range para trabalhar melhor com o loop for.

Ranges são utilizados para gerar sequencias numéricas não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

# 1
range(valor_de_parada)

obs: valor_de_parada não inclusive início padrão 0 e passo de 1 em 1.
O retorno é uma sequência de números de 0 à num - 1.
Ou seja é uma função de incremento.

# 2
range(valor_de_inicio, valor_de_parada).

obs: Do primeiro e vai encrementado até o valor de parada menos 1.

# 3
range(valor_de_inicio, valor_de_parada, passo)

obs: Passo específicado pelo programador.

# 4
range(valor_de_inicio, valor_de_parada, -passo)

obs: igual a forma 3, mas o inverso.

Colocando range no console não aparece a lista, apenas a instrução. Para ver é assim:
# >>> lista = list(range(10))
# >>> lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

print('range() com critério de parada -----------------------------------------------------------------------range(11)')

for num in range(11):
    print(num)

print('range() com critério de início e fim---------------------------------------------------------------range(1, 11)')

for num in range(1, 11):
    print(num)

print('range() com razão -----------------------------------------------------------------------------range(1, 11, 10)')

for num in range(5, 50, 10):
    print(num)

"""
Será feita uma p.a de 5 a 50 com razão 10.
"""

print('range() decrescente----------------------------------------------------------------------------range(10, 0, -2)')

for num in range(10, 0, -2):
    print(num)

print('Exercício 1 ---------------------------------------')

"""
Crie um programa que utilize a função range() para imprimir os números pares de 0 a 20. Certifique-se de incluir 
comentários explicativos no código.
"""

print(tuple(range(0, 21)))

print('Exercício 2 ------------------------------------')

"""
Desenvolva um programa que solicite ao usuário um número e, em seguida, utilize a função range() para imprimir os 
primeiros N termos da sequência de Fibonacci. A sequência de Fibonacci é aquela em que cada termo é a soma dos dois 
anteriores, começando com 0 e 1.
"""
'''
n = int(input('Coloque quantos números da sequencia de Fibonacci você deseja imprimir: '))

for an <= n:
'''
"""
a3 = a2 + a1 
"""

# Exercício 2 - Desafiador
# Imprimir os primeiros N termos da sequência de Fibonacci usando range()

# Solicitando ao usuário o número de termos desejados
n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja imprimir: "))

# Inicializando os primeiros dois termos da sequência de Fibonacci
a, b = 0, 1

# Imprimindo os primeiros N termos usando a função range()
for _ in range(n):
    print(a, end=" ")

    # Calculando os próximos termos da sequência
    a, b = b, a + b

"""
No Python, o uso do sublinhado _ como uma variável temporária em um loop é uma convenção para indicar que a variável não 
é usada dentro do loop e que seu valor não é relevante. Ele é muitas vezes utilizado quando o loop é iterado um número 
fixo de vezes, e a variável de iteração em si não é utilizada no bloco do loop.

No Exercício 2 - Desafiador, a variável _ é usada como uma convenção para indicar que não estamos utilizando o valor 
da ]variável de iteração do loop (_ pode ser qualquer nome de variável válido em Python). Nesse contexto, o valor de a 
(que representa os termos da sequência de Fibonacci) é o que importa, e a variável _ é apenas uma forma de indicar que 
não estamos fazendo uso dela.

Poderiamos ter declarado essa variável normalmente, chamando de i por exemplo, Entretanto, ao usar _, deixamos claro 
para outros programadores que a variável de iteração i não é relevante para o bloco do loop, e isso é especialmente útil 
quando não precisamos do valor da variável de iteração. Isso melhora a legibilidade do código.
"""
