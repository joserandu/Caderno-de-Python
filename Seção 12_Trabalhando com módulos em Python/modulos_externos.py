"""
MÓDULOS EXTERNOS

Utilizamos o gerenciador de pacotes python chamado PIP (Python Installer Package).

Para conhecer todos os pacotes externos oficiais em: https://pypi.org

digitando pip no terminal python ensina o modo de uso e todas as outras funcionalidades:
Usage:
  pip <command> [options]

Indo no site do pypi.org, podemos acessar alguns arquivos especificos na área de pesquisa, por exemplo o "colorama",
e podemos até copiar o comando (pip install colorama).

Tem que estar conectado na internet.
A saida pode falar para a gente atualizar, ai será passado o comando que devemos dar, então é só copiar e colar.

Colorama

É utilizado para permitir a impressão de textos coloridos no terminal.
Na propria página do colorama dentro da página do Python explica como usar, assim como com todos os outros módulos
externos.
"""
# Colorama
from colorama import init, Fore
# Python-pdf
import pydf

print("Mudando as colores das strings com colorama -----------------------------------Fore.MAGENTA + 'Geek University'")

# Documentação: https://pypi.org/project/colorama/

init()

print(Fore.MAGENTA + "Geek University")

print("Manipulando arquivos pdf com python-pdf ----------------------")

# Documentação: https://pypi.org/project/python-pdf/

"""
Aprenderemos a manipular arquivos a partir da próxima seção.
"""

pdf = pydf.generate_pdf('<h1>Geek University</h1><br><br><strong>Programa&ccedil;&atilde;o em Python: '
                        'Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

"""
- Isso não funciona ao passo que o meu SO é Windons e precisaria instalar o wkhtmltopdf (https://wkhtmltopdf.org/). 
Como o SO do professor é linux não foi necessário.
- Os caracteres especiais precisam ser colocados de maneira especial para que possam ser impressos.

Para usar precisaria inclusive especificar o caminho da instalação para usa-lo: 
pdf = pydf.generate_pdf('<h1>Geek University</h1>', wkhtmltopdf='/caminho/para/o/wkhtmltopdf')
"""
