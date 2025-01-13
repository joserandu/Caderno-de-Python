"""
MODOS DE ABERTURA DE ARQUIVOS

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir.
    - Caso o arquivo exista, gera FileExistsError.
a -> (append) Abre para escrita, adicionando o conteúdo ao final do arquivo.
    - Abrindo o modo 'a'(append), se o arquivo não existir será criado. Caso exista, o novo conteúdo será adicionado
    ao final.
+ -> abre para o modo de atualização: Leitura e escrita.

Podemos ver mais modos em: https://docs.python.org/3/library/functions.html#open
"""

try:
    with open("geek.txt", 'w', encoding="utf-8") as arquivo:
        arquivo.write("geek.\n" * 20)
except FileExistsError:
    print("O arquivo já existe!")

print("Adicionando elementos no arquivo (modo 'a') ----------------------------------------------open('text.txt', 'a')")

with open("frutas.txt", 'a', encoding="utf-8") as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite sair: ")
        if fruta != 'sair':
            arquivo.write(f"{fruta} \n")
        else:
            break

"""
Não conseguimos controlar o cursor com o modo 'a'.
"""

print("Adicionando elementos no topo da lista ----------------------")

with open("novo.txt", "r+", encoding="utf-8") as arquivo:
    # Aqui está a mágica
    conteudo_existente = arquivo.read()
    arquivo.seek(0)

    arquivo.write(f"Escrita da aula de modos:\n")
    arquivo.write(f"Logo abaixo, a escrita da aula de escrevendo em arquivos:")
    arquivo.write("\n\n---------------------------------------------------------------\n")

    arquivo.write(conteudo_existente)

"""
Se usar o w, o arquivo será reescrito, portanto, use o 'r'.
"""
