"""
PACOTES

Módulo -> apenas um arquivo python com diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;
    - O diretório no qual está contido esse arquivo por exermplo é um pacote.
    - Nas versões anteriores a 3 do python um pacote deveria conter dentro dele um arquivo chamado __init__.py,
    mas nas novas versões não é mais obrigatória a utlização desse arquivo, mas ainda é usado para manter a
    compatibilidade.

Fizemos um python package chamado geek, criamos dois arquivos e um subpacote com mais dois arquivos. e perceba que é
feito a adição de um __init__.py automaticamente.
"""

# Importando os pacotes

from geek import geek1, geek2
# Atenção aqui:
from geek.university import geek3, geek4


"""
Para importar uma função de um módulo dentro de um pacote: from geek.geek1 import funcao1
Subpacotes a gente importa dessa forma: geek.university
"""

print(geek1.pi)

print(geek1.funcao1(2, 3))

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

print(geek1.funcao1(2, 5))
