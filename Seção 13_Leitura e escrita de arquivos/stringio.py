"""
StringIO

Para ler ou escrever dados em arquivos do SO o software precisa ter permissão:
    - Permissão de Read -> Para ler o arquivo
    - Permissão de Write -> Para ecrever o arquivo

StringIO -> Utilizado para ler e criar arquivos em memória
    - Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois.
"""
# Atenção a estrita do import:
from io import StringIO

mensagem = 'Mensagem normal'

arquivo = StringIO(mensagem)

"""Agora tendo o arquivo podemos utilizar tudo o que já sabemos, pois equivale ao arquivo = open('text.txt', 'w'"""

print(arquivo.read())

# Escrevendo outros textos
arquivo.write(" Outro texto")

"""
Podemos também movimentar o cursor e fazer a leitura novamente.
"""

arquivo.seek(0)

print(arquivo.read())
