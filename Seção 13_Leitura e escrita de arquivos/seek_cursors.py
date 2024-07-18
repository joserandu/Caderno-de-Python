"""
SEEK E CURSORS

A função seek é utilizada para movimentar o cursor pelo arquivo.
    - Ela recebe um parâmetro que indica onde queremos colocar o cursor.
    - Seek significa procurar.
"""

print("Relembrando o open() ------------------------------------------------------------")

arquivo = open("texto.txt")
print(arquivo.read())

print("Movimentando o cursor pelo arquivo com a função seek() ------------------------------")

arquivo.seek(0)
print(arquivo.read(50))  # Para limitar a leitura em 50 caracteres

"""
Com isso conseguimos fazer o cursor voltar no início e conseguimos ler o arquivo novamente.
Com a função read conseguimos controlar o número de caracteres a serem lidos no arquivo.
"""

arquivo.seek(21)
print(arquivo.read())

print("Função readline() para ler linha a linha -----------------------------------------")

arquivo.seek(0)  # Voltando ao começo
print(arquivo.readline())  # O cursor para no final da linha.
print(arquivo.readline())  # Lê a próxima linha.

print(type(arquivo.readline()))  # str

"""
Por transformar em uma string, podemos fazer as funções naturais que fariamos com uma string, usando split(' '), 
len(), etc.

"""

print("Função redlines() para transformar o aquivo em uma lista de linhas ------------------------")

arquivo.seek(0)
print(arquivo.readlines())

# Contando a quantidade de linhas
arquivo.seek(0)
linhas = len(arquivo.readlines())
print(linhas)

"""
Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o nosso 
programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. 
Para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;
2 - Trabalhar o arquivo;
3 - Fechar o arquivo;
    - Esse processo é importante para evitar erros.
"""

# 1 - Abrir o arquivo
arquivo = open("texto.txt")

# 2 - Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado.

# 3 - Fechar o arquivo
arquivo.close()

print(arquivo.closed)

"""
Se tentarmos manipular o arquivo após o seu fechamento, teremos um ValueError.
"""
