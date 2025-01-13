"""
LEITURA DE ARQUIVOS

Para ler o conteúdo de um arquivo utilizamos a função integrada open(), que literalmente significa abrir.

open(): A forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho
para o arquivo a ser lido. Essa função retorna um _oi.TextIOWrapper e é com ele que trabalhamos então.

Para ver a documentação do open
https//:docs.python.org/3/library/functions.html#open

Por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro:
NotFileFoundError

"""

arquivo = open("texto.txt", 'r', encoding="utf-8")

"""
Pode ser necessário colocar o enconding para a impressão não ficar sem os caracteres de acentuação, pois as vezes a 
IDE não identifica, como aconteceu agora. (file -> file properties -> encoding file -> UTF-8).
"""

print(arquivo)
# mode="r" -> modo=leitura(read)

print(type(arquivo))

"""
Para ler o conteúdo de um arquivo após a sua abertura (open()) devemos utilizar a função read().
"""

# Para ler o arquivo
print(arquivo.read())

print(arquivo.read())  # Não imprime nada, pois o cursor já está no final.

"""
O Python utiliza um recurso para trabalhar com arquivos chamada cursor. Esse cursor funciona como o cursor quando 
estamos escrevendo. 

A função read lê todo o conteúdo do arquivo.
"""

retorno = arquivo.read()

print(retorno)
print(type(retorno))

"""
Vai virar string.
"""

ret = open("texto.txt")
print(ret.read().split(" "))
