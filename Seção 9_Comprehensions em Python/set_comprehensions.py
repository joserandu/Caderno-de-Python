"""
SET COMPREHENSION

Relembrando a sintax:
lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

A sintaxe do set comprehension é a mesma do list comprehension, com a única diferença de que o set utiliza {}.
A diferênça na parte lógica reside na não ordenação dos elementos e na impossibilidade de repeti-los.
"""

print('Set Comprehensions ---------------------------------------------------------------{num for num in range(1, 10)}')

numeros = {num for num in range(1, 7)}
print(numeros)

print('Utilizando range() -------------------------------------------------------------------{x ** 2 for x in range()}')

numeros2 = {x ** 2 for x in range(10)}
print(numeros2)

print('Para fazer um dicionário --------------------------------------------------------------{x: <set comprehension>}')

numeros3 = {x: x ** 2 for x in range(10)}
print(numeros3)

print('Mais sobre a teoria ----------------------------------------------------------------{letra for letra in string}')

letras = {letra for letra in 'Geek University'}
print(letras)

"""
Perceba que nenhum valor é repetido e a ordem das letras é alterada aleatóriamente.
"""

<<<<<<< HEAD
<<<<<<< HEAD
print('Exercício 1 -----------------')
=======
print('Exercício 1 --------------------------------------------------{num for num in range(1, 20 + 1) if num % 2 == 0}')
>>>>>>> 8db86c2 (Venv)
=======
print('Exercício 1 -----------------')
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61

"""
Compreensão de Conjuntos com Condições

Escreva uma set comprehension que crie um conjunto contendo apenas os números pares no intervalo de 1 a 20.
"""

conjunto1 = {num for num in range(1, 20 + 1) if num % 2 == 0}
print(conjunto1)

<<<<<<< HEAD
<<<<<<< HEAD
print('Exercício 2 --------------------')
=======
print('Exercício 2 -------------------------------------------------{num ** 2 for num in range(1, 16) if num % 2 != 0}')
>>>>>>> 8db86c2 (Venv)
=======
print('Exercício 2 --------------------')
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61

"""
Compreensão de Conjuntos com Transformação

Utilizando set comprehension, crie um conjunto que contenha o quadrado dos números ímpares no intervalo de 1 a 15.
"""

conjunto2 = {num ** 2 for num in range(1, 16) if num % 2 != 0}
print(conjunto2)

<<<<<<< HEAD
<<<<<<< HEAD
print('Exercício 3 ----------------------')
=======
print('Exercício 3 ---------------------------------------{letra for letra in set(string) if letra.lower() in "aeiou"}')
>>>>>>> 8db86c2 (Venv)
=======
print('Exercício 3 ----------------------')
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61

"""
Compreensão de Conjuntos com Strings

Dada a string "Python Programming", crie um conjunto contendo apenas as vogais presentes na string. Lembre-se de 
considerar tanto maiúsculas quanto minúsculas.
"""

string = 'Python Programming'

vogais = {letra for letra in set(string) if letra.lower() in 'aeiou'}
print(vogais)
