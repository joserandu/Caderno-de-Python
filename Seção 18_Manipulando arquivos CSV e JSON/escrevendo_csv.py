"""
ESCREVENDO EM ARQUIVOS CSV

writer() -> cria um objeto para a gente escrever

writerow() -> Escreve uma linha.
"""

from csv import writer, DictWriter

with open('filmes.csv', 'a', encoding='utf-8', newline='') as arquivo:  # w escreve no arquivo, a escreve em cima do
    # arquivo gerando o arquivo CSV
    escritor_csv = writer(arquivo)
    filme = None
    # Fazendo o cabeçalho
    # escritor_csv.writerow(['TÍTULO', 'GÊNERO', 'DURAÇÃO'])  # Para não ficar apagando toda hora
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o gênero: ")
            duracao = input("Duração em minutos: ")
            escritor_csv.writerow([filme, genero, duracao])  # Escrevendo uma linha

print("DictWriter ----------------------------------------------------------------------------------------------------")

with open('filmes2.csv', 'a', encoding='utf8', newline='') as arquivo:  # newline pe para não ficar deixando linhas
    # em branco no windows
    cabecalho = ['TÍTULO', 'GÊNERO', 'DURAÇÃO']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'Sair':
        filme = input("Informe o nome do filme: ").strip().title()
        if filme != 'Sair':
            genero = input("Informe o gênero: ").strip().title()
            duracao = input("Informe a duração (em minutos): ").strip()
            escritor_csv.writerow({'TÍTULO': filme, 'GÊNERO': genero, 'DURAÇÃO': duracao})

"""
Observação: As chaves dos dicionários devem ser iguais as chaves do dicionario que criamos no cabeçalho.
Nesse segundo código de escrita de dados eu incrementei strip e title para haver uma padronização.
"""
