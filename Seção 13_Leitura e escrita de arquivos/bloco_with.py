"""
O BLOCO WITH

Passos para trabalhar com arquivos:
1 - Abrimos o arquivo
2 - Manipulamos o arquivo
3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados após o bloco with.
    - With significa "com".
    - É a forma pythonica de trabalhar com arquivos.

Basicamente o with vai abrir e fechar os arquivos automaticamente.
"""

print("O Bloco With ------------------------------")

with open("texto.txt") as arquivo:
    print(arquivo.readlines())

print("Testando o with -------------------")

with open("texto.txt") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # False

print(arquivo.closed)  # True

"""
Dessa maneira, fica evidente que o bloco do with fechou o arquivo.
"""
