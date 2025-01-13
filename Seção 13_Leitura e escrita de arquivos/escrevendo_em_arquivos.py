"""
ESCREVENDO EM ARQUIVOS

Para ler ou escrever em um arquivo, primeiro a gente deve abrir o arquivo, mas tem algumas mudanças para abrir esse
arquivo para escrita.

Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler. Da mesma forma, se abrimos um
arquivo para escrita, não podemos lê-lo, apenas escrever nele.

Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.
"""

print("Exemplo de escrita (modo 'w') ---------------------------------------")

with open("texto.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Escrever dados em arquivo é muito fácil. \n")
    arquivo.write("Podemos colocar quantas linhas quisermos.\n")
    arquivo.write("Essa é a última linha.\n")

"""
O open tem como padrão o modo de leitura, não precisando especificar. (modo 'r')
"""

print("Criando um novo arquivo com o open() -----------------------------------------------------open('novo.txt', 'w')")

with open("novo.txt", 'w', encoding="utf-8") as novo_arquivo:  # O novo.txt está diferente por conta do exemplo abaixo.
    novo_arquivo.write("Escrever dados em arquivo é muito fácil. \n")
    novo_arquivo.write("Podemos colocar quantas linhas quisermos.\n")
    novo_arquivo.write("Essa é a última linha.\n")

"""
Para escrever dados em um arquivos, apos abrir o arquivo utilizamos a função write(), essa função recebe uma string 
como parâmetro, caso contrário, teremos um TypeError.
"""

with open("novo.txt", 'w', encoding="utf-8") as novo_arquivo:
    novo_arquivo.write("Novos dados. \n")
    novo_arquivo.write("Outros dados.\n")
    novo_arquivo.write("Essa é a última.")

"""
Atenção: Quando abrimos um arquivo para a escrita com o modo 'w', se o arquivo não existir será criado, caso ele já 
exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é perdido.
Por isso, os dados do exemplo anterior foram apagados. Mas tem outros modos de aberturas de arquivos.
"""

print("Fazendo uma operação com o write -------------------------------------------")

with open('geek.txt', 'w', encoding="utf-8") as arquivo:
    arquivo.write('geek.\n' * 20)

print("Fazendo um loop para escrever um arquivo ------------------------while True: arquivo.write(fruta)")

with open('frutas.txt', 'w', encoding="utf-8") as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != 'sair':
            arquivo.write(f"{fruta} \n")
        else:
            break
