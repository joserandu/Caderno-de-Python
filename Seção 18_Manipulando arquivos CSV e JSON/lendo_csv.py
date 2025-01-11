"""
Lendo arquivos csv

"""

from csv import reader, DictReader

print("Reader --------------------------------------------------------------------------------------------------------")

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)  # Devolve uma lista para a gente
    next(leitor_csv)  # Isso daqui serve para pular a primeira linha do iterator (cabeçalho)
    for linha in leitor_csv:
        print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros")


"""
A linguagem python possui duas formas diferentes para ler dados em arquivos CSV
    - Reader: Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader: Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts.
"""

print("DictReader ----------------------------------------------------------------------------------------------------")

# DictReader

with open('Lutadores.csv', encoding='utf-8') as arquivo2:
    leitor_csv2 = DictReader(arquivo2, delimiter=",")  # Serve para especificar caso não seja uma virgula separando
    # os arquivos.
    for linha in leitor_csv2:
        print(f"{linha['NOME']} nasceu no(a)(s) {linha['PAÍS']} e mede {linha['ALTURA (EM CM)']}")

# Arquivos CSV de ceps do Brasil
with open('ceps.csv', encoding='utf-8') as arquivo3:
    leitor_csv3 = DictReader(arquivo3, delimiter=",")
    for linha in leitor_csv3:
        if linha['CIDADE'] == "Guarulhos":
            print(f"Menor CEP: {linha['CEP DE']}\nMaior CEP: {linha['CEP ATÉ']}")
