"""
SISTEMAS DE ARQUIVOS - MANIPULAÇÃO


"""
import os
from send2trash import send2trash

print("Descobrindo se um arquivo ou diretório existe ------------------------------")

# Path relativos
print(os.path.exists("arquivo.txt"))
print(os.path.exists("frutas.txt"))
print(os.path.exists("geek"))
print(os.path.exists("geek\\university"))  # Subdiretório

# Paths absolutos
print(os.path.exists("C:\\Python\\Seção 13_Leitura e escrita de arquivos"))

"""
E assim você pode verificar qualquer arquivo de qualquer lugar da máquina.
"""

print(os.path.exists("C:\\Arquivos de Programas"))

print("Abrindo um novo arquivo e já fechando -------------------------------------")

# Forma incorreta:
# with open("arquivo-teste.txt", "w").close() as arquivo:
#    pass

# Forma que não funciona do windows
# os.mknod("arquivo-teste2.txt")

"""
- Se você estiver usando o Mac OS, pode haver um erro de PermissionError
Se criando um arquivo via mknod(), se o arquivo já existir, teremos o erro FileExisteError
"""

print("Criando um diretório -------------------------------")

# Comando mkdir() - Make Directory
# os.mkdir('templates')  # Comentei porque fica dando erro se recarrega a página.

"""
A função mkdir() cria um diretório se este não existir, caso exista, teremos um FileExistsError.
Poderia passar um absoluto:
os.mkdir('C:\\Python\\Seção 13_Leitura e escrita de arquivos')

Se não tivermos permissão para criar o diretório, teremos um PermissionError
"""

print("Criando vários diretórios -----------------------------------")

os.makedirs("Geek\\university", exist_ok=True)  # Coloquei para não ficar dando erro toda vez que recarregamos.
os.makedirs("templates\\geek\\university", exist_ok=True)

print("Renomeando arquivos -----------------------------------")

# Renomeando Diretório:
# os.rename('templates', "Templates")

# Renomeando arquivo
# os.rename('Templates\\geek\\teste2.txt', "geek/teste3.txt")

print("Deletando arquivos ---------------------------------------------------------------------------------os.remove()")

"""
ATENÇÃO:
- Tome cuidado com os comandos de deleção, ele não vai para a lixeira, eles somem.

- No windows, se voce for deletar um arquivo que estiver aberto por alguém, dará um erro.
- Caso o arquivo não exista, teremos o FileNotFoundError
- Se informar um diretório ao invés de um arquivo, teremos um IsADirectoryError
"""

# os.remove("geek.txt")  # Não removi, somente exemplifiquei.

print("Deletando Diretórios vazios -------------------------------------------------------------------------os.rmdir()")

# Removendo diretórios vazios:
# os.rmdir('Templates\\geek\\university')

"""
Se não extiver vazio: OSError
Se não existir: FileNotFoundError
"""

print("Deletando uma árvore de diretórios ------------------------------------------------------------------os.rmdir()")

"""
for arquivo in os.scandir('geek'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)
        
# Isso vai excluir todos os arquivos de dentro do diretório geek.
"""

print("Remover uma árvore de diretórios vazios -------------------------------------------")

# os.removedirs("geek2\\outro\\mais")

"""
Esses diretórios não existem, estou só exemplificando

Se algum dos diretórios tiver arquivos ou outros diretórios o processo para.

Ao remover arquivos e diretórios com Python eles não vão para a lixeira, eles desapareçem.
"""

# pip install send2trash

print("Usando send2trash -----------------------------")

"""
Os arquivos e diretórios não somem, eles podem ser recuperados. "enviar para a lixeira".
Se o arquivo não existir teremos OSError.

send2trash('cesta2.txt')
"""


