"""
SISTEMA DE ARQUIVOS - NAVEGAÇÃO

As informações que temos de tamanho da imagem, resolução e data de criação não são dados no nome da imagem nem na sua
extenção, são METADADOS.

O principal diretório é o root directory (diretório raiz)
    - Para o windows (C:\\)
    - Para mac e linux (/)
        - Chamado de sistema POXIS
        - É bem mais seguro que o windows.
        - Para fazer a arvore hierearquica do seu diretório: sudo apt install tree e depois o comando tree. (linux)

PATH é o caminho para o seu arquivo
    - Path absoluto: ele pega o caminho da raiz até o arquivo
        - No linux para mover para o diretório acima é o ..
    - Path relativo: ele pega um caminho mais curto, não puxando da raiz.
        - No linux para mover para o mesmo diretório é o .
        - Essa informação pode ser importante porque normalmente o local de postagem de uma aplicação é no linux.

Para fazer o uso de manipulação de arquivos do SO, precisamos importar e fazer uso do módulo OS.
    - Operation System
"""
# Bliblioteca os
import os
# Biblioteca para tirar as informações da máquina do windows:
import platform

print("Para saber o caminho completo do diretório que você está -------------------------------os.getcwd()")

print(os.getcwd())

"""
os. getcwd() retorna o path (caminho) absoluto.
"""

# os.chdir("..")

print(os.getcwd())

"""
Pode fazer esse processo varias vezes, mas lembre-se que não passa da raiz
Podemos checar se um diretório é absoluto ou relativo
    - a função isabs() quer dizer 'is absolute' e a resposta é booleana.
"""

print(os.path.isabs('C:\\Python\\Seção 13_Leitura e escrita de arquivos'))  # True
print(os.path.isabs('Python\\Seção 13_Leitura e escrita de arquivos'))  # False, porque tirou a barra. É relative.

"""
É importante usar o \\ se estiver usando windows, para evitar ser confundido com um \n
"""

print("Indentificando o SO -------------------------------------")

print(os.name)

"""
nt -> Windows
posix -> Linux e Mac

Podemos ter mais detalhes do sistema operacional.
"""

print("Obtendo mais dados da máquina ---------------------------------------")

# print(os.uname())

"""
Não dá para usar o us.uname() no windows para ver dados do computador, precisamos usar o platform.uname() 
"""

system_info = platform.uname()

print("System:", system_info.system)
print("Node Name:", system_info.node)
print("Release:", system_info.release)
print("Version:", system_info.version)
print("Machine:", system_info.machine)
print("Processor:", system_info.processor)

print("Juntando diretórios --------------------------------------------------")

# Essa configuração parece não funcionar com Windows
"""
res = os.path.join(os.getcwd(), 'Seção 13_Leitura e escrita de arquivos', 'geek')

os.chdir(res)

print(os.getcwd())
"""

"""
O os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será juntado 
ao atual
"""

print("Listando diretórios ----------------------------------------------------")

print(os.listdir('C:\\'))
print(len(os.listdir('C:\\')))

print("Obtendo mais informações ------------------------------------------------------")

print(os.scandir('C:\\'))
print(list(os.scandir('C:\\')))

"""
Não deu certo também.
"""

print("Trabalhando melhor com o scandir -----------------------------------------------")

# Boa prática para a gente conseguir finalizar o uso do scandir ao final do código.
scanner = os.scandir()
arquivos = list(scanner)

print(arquivos)

# Consultando o nome do arquivo
print(arquivos[0])  # Name com o DirEntry
print(arquivos[0].name)  # name do arquivo

# Caminho até o arquivo
print(arquivos[0].path)

# Funções
print(f"Identificador do node/diretório: {arquivos[0].inode()}")  # Cada diretório recebe um número identificador.
print(f"É um diretório? {arquivos[0].is_dir()}")
print(f"É um link simbólico? {arquivos[0].is_symlink()}")
print(f"Dados do arquivo: {arquivos[0].stat()}")
print(f"Tamanho do arquivo: {arquivos[0].stat().st_size} bytes") 

"""
Quando utilizamos a função scandir, nós precisamos fecha-la, assim como fechamos um arquivo.
"""

scanner.close()
