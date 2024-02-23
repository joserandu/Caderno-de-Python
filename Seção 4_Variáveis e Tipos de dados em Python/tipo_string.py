"""
Já vimos que em Python um dado é considerado do tipo string sempre que está entre aspas simples.

Ex: 'Exemplo', 'True', '123', 'True' -> não são outros tipos de dados, são strings pela mesma lógica.
Sempre que estiver entre aspas duplas também: "Exemplo".
Aspas simples triplas também: '''123'''
"""

nome = """Geek 'University'"""
print(nome)
print(type(nome))  # class 'str

"""
A primeira vista isso parece ser o própiro terror da PEP8. Essas anotações entre aspas são consideradas strings, mas 
somente se estiver na frente da variável.
Esse modo de escrever strings podem ser uteis em casos nos quais a temos strings com aspas no meio delas.
Como no caso do print aqui em baixo:
"""

print("A mesma coisa para as outras aspas ---------------------------------------------------------------'Ginas's Bar'")

nome = "Gina's Bar"
print(nome)

"""
Aqui é necessário colocar a string em aspas duplas para não dar problema.
"""

print('Quebra de linha no meio da string ---------------------------------------------------------------------------\n')

# Forma 1
nome = 'Angelina \n Jolie'
print(nome)
print(type(nome))

"""
O \n serve para indicar uma quebra de linha. Atenção que não é a barra de data.
Repare como houve uma quebra de linha na impressão do título
"""

# Forma 2
nome = """Angelina 
Jolie"""
print(nome)
print(type(nome))

"""
Da um resultado semelhante, com a diferença que não fica um espaço antes do Jolie. Mas para fazer isso é necessário 
usar aspas triplas.
"""

print('Método para formatação das strings ------------------------------------------upper() lower() split() nome [0:4]')

nome = 'Geek University'
print(nome.upper())  # CAIXA ALTA
print(nome.lower())  # caixa baixa
print(nome.split())  # Forma uma lista.
print(nome[0:7])  # Determina a posição a ser retornada.

"""
No método split, se houver uma string com mais de uma palavra, será retornado uma lista com duas palavras.
No método das chaves a lógica é a seguinte: O primeiro valor serve para determinar a partir de qual posição a string 
será retornada, e o segundo valor serve para postular QUANTO da string será impresso a partir da posição colocada no 
primeiro valor.
"""

print('Trabalhando mais com os métodos de listagem e busca ---------------------------------nome[2: 5] nome.split()[1]')

print(nome[5:1755])

"""
Pode colocar qualquer número que a string não vai se repetir, ela vai terminar no sua última letra.
"""

print(nome.split()[1])

"""
Será impresso o segundo nome da lista de strings, porque o primeiro é o 0.
"""

print('Buscando mais de uma string ------------------------------------------------------------print(nome[3], nome[6])')

print(nome[14], nome[5])

"""
Vai retornar cada posição de uma string.
"""

print('Intertendo a ordem dos valores de uma string --------------------------------------------------------nome[::-1]')

print(nome[::-1])
print(nome[:4:-1])

"""
É como se a gente estivesse dizendo 'vá até o último valor e inverta'.
"""

print("Substituindo valores dentro de uma string -----------------------------------------------nome.replace('G', 'P')")

print(nome.replace('G', 'P'))

"""
Não esqueça dos detalhes que esse método pede e que ele é muito importante.
"""

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

"""
Engraçadão.
"""

print('Exercício 1 --------------------------------------------------------------------------nome_completo.split()[-1]')

"""
Crie um programa em Python que recebe o nome completo do usuário e exibe apenas o primeiro e o último nome.

Dica:

- Utilize a função input para receber o nome completo.
- Utilize a função split para separar as palavras do nome.
- Exiba o primeiro e o último nome na tela.
"""

nome_completo = input('Digite o seu nome completo:')

print(f'Seja Bem Vindo, {nome_completo.split()[0]} {nome_completo.split()[-1]}')

print('Exercício 2 --------------------------------------------------------------------------------frase.split()[::-1]')

"""
Escreva um programa que solicita ao usuário que digite uma frase. Em seguida, o programa deve imprimir a frase 
invertida, considerando cada palavra individualmente.

Dica:

- Utilize a função input para receber a frase.
- Utilize a técnica de indexação reversa para inverter a ordem das palavras.
- Exiba a frase invertida na tela.
"""

frase = input('Escreva uma frase para eu inverter:')

print(f'Invertendo a frase fica: {frase.split()[::-1]}')
