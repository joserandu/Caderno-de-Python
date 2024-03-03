"""
ERROS MAIS COMUNS EM PYTHON

- É importante a gente saber ler as saidas de erro.

NameError --------------------------------------------------------------------------------------------------------------

Quando a gente erra um comando aparece isso:

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 7, in <module>
    printf('Geek')
NameError: name 'printf' is not defined

Isso quer dizer que nesse arquivo, na linha 7, printf() esta escrito errado.
Se em algum repositório a gente abrir o terminal e digitar 'ls' a gente vai LiStar os arquivos da pasta.

SyntaxError ------------------------------------------------------------------------------------------------------------

Quando o python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não reconhece como parte da
linguagem.

def funcao:
    print('Geek University')

File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 37
    def funcao:
              ^
SyntaxError: invalid syntax

Sem os parêntesis

Exemplo 2:
None = 1

As variáveis não podem ter nomes de palavras especializadas.
Eu ia escrever um return fora de uma função, mas acabou travando o computador do professor e eu não quero travar o meu.

NameError --------------------------------------------------------------------------------------------------------------

Ocorre quando uma variável ou função não foi definida.

print(geek)

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 59, in <module>
    print(geek)
NameError: name 'geek' is not defined

O nome geek não existe como variável, ou seja, não foi definida.

Exemplo:
a = 18

if a < 10:
    msg = 'é maior que 10'

print(msg)

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 73, in <module>
    print(msg)
NameError: name 'msg' is not defined

a variável msg não existe fora do bloco do if.

TypeError --------------------------------------------------------------------------------------------------------------

Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplo 1:
print(len(5))

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 92, in <module>
    print(len(5))
TypeError: object of type 'int' has no len()

O len() não funciona com o tipo int.

Exemplo 2:
print('Geek' + [])

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 99, in <module>
    print('Geek' + [])
TypeError: can only concatenate str (not "list") to str

Só pode concatenar string (não lista) com string.

IndexError -------------------------------------------------------------------------------------------------------------

Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice invalido.

Exemplo:
lista = ['Geek']
print(lista[0][4]) Erro 1
print(lista[1]) Erro 2

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 116, in <module>
    print(lista[1])
IndexError: list index out of range

Só tem posição 0 na lista, só se tiver

ValueError -------------------------------------------------------------------------------------------------------------

Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.

Exemplo:
print(int('Geek'))

KeyError ---------------------------------------------------------------------------------------------------------------

Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplo:
dic = {}
print(dic['geek'])

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 140, in <module>
    print(dic['geek'])
KeyError: 'geek'

Preste atenção nas saidas de erro.

AttriobuteError --------------------------------------------------------------------------------------------------------

Ocorre quando uma variável não tem um atributo ou função.

tupla = 11, 2, 31, 4
print(tupla.sort())

Traceback (most recent call last):
  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 155, in <module>
    print(tupla.sort())
AttributeError: 'tuple' object has no attribute 'sort'

O sort não funciona com tupla, só com lista. O que funciona com todos é o sorted().

IndentationError -------------------------------------------------------------------------------------------------------

Ocorre quando não respeitamos a identação do Python (4 espaços).

Exemplo:
def nova():
print('Geek')

  File "C:/Python/Seção 11_Debugando e tratando erros/erros_mais_comuns.py", line 170
    print('Geek')
    ^
IndentationError: expected an indented block

Observações ------------------------------------------------------------------------------------------------------------

- Existem muitos outros tipos de erros, mas esses são os principais.
- Exeptions e Erros são sinonimos na programação.
- Importante ler e prestar atenção na saida de erro.
"""
