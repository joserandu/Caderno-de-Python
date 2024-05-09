"""
MÉTODOS

Representam os comportamentos do objeto, ou seja, as açoes que o objeto pode realizar.
Em Python dividimos os métodos assim como os atributos em dois grupos:
    - Métodos de instancia
    - Métodos de classe

o método dunder init é um método especial chamado de construtor, e sua função é construir um objeto a partir da classe.
    dunder (underline) = duplo
        Se tem só no inicio, não são métodos dunders, assim como nos atributos privados.
    Os métodos dunder em Python são chamados de métodos mágicos.
    ATENCAO: Por mais que possamos criar as nossas próprias funcoes usando __ no inicio e no fim, Python possui
    vários métodos com essa forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas
    internas da linguagem, então evite ao máximo, de preferência, nunca o faça.
"""

# Método de instancia


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1  # A primeira conta fai ser 5000
        self.__limite = limite
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor


class Produto:

    contador = 0

    # Método Construtor
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id  # Não esqueça do self.

    # Método de instancia
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (100 - porcentagem) / 100


print("Utilizando método de instancia ------------------------------------------------------------------p1.desconto(x)")

p1 = Produto("PlayStation 4", "Video Game", 2300)

print(p1.desconto(15))  # Repare que nessa parte não temos a classe, apenas na declaração da variável.

# Outra maneira
print(Produto.desconto(p1, 15))  # o p1 é o argumento para o parâmetro self

print("Para criptografar senhas ----------------------------------------from passlib.hash import pbkdf2_sha256 as cryp")

"""
Para cripitografar os dados:

from passlib.hash import pbkdf2_sha256 as cryp

Não consegui fazer o import, mas é importante conhecer essa biblioteca.
"""


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        # self.__senha = cryp.hash(senha, rounds=200000, salt_salze=16)  # Vai embaralhar a senha 200000 vezes.

    def correr(self, metros):
        print(f'{self.__nome} está correndo {metros}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if self.__senha == senha:
            return f"Seja bem-vindo(a), {self.__nome}!"
        return f"{self.__nome}, sua senha está incorreta!"

    """
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):  # Vai comparar se a senha escrita nos argumentos é igual a do banco de 
        dados. 
            return True
        return False
    """


"""
Métodos são escritos em letra minúscula, Se o nome for composto, o nome tera as palavras em underline. Regra normal 
de nome de função.
"""

user1 = Usuario("Angelina", "Jolie", "angelinajolie@gmail.com", "123456")
user2 = Usuario("Bred", "Pitt", "bredao@gmail.com", "87654321")

print(user1.nome_completo())
print(user2.nome_completo())

"""
Não tem erro, atributo de instancia está dentro da classe.
O self é o user1 e o user2 nesse caso.
"""

print(Usuario.nome_completo(user1))
print(Usuario.nome_completo(user2))

print("Cadastrando um usuário -----------------------------------------user = Usuario(name, surname, e_mail, password)")

name = input("Nome: ")
surname = input("Sobrenome: ")
e_mail = input("Email: ")
password = input("Senha: ")
confirma_password = input("Confirme a senha: ")

if password == confirma_password:
    user = Usuario(name, surname, e_mail, password)
else:
    print("As senhas estão escritas diferentes entre si...")
    exit(42)  # Número qualquer, não muito grande, para finalizar o código.

print("Usuario criado com sucesso!")

password = input("Informe a senha para acesso: ")

"""
if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")
"""

print(f"Senha User ")

print("Métodos de classe ----------------------------------------------------------def conta(cls): / f'{cls.contador}'")


class Usuario2:

    contador = 0

    # Método de classe
    @classmethod
    def conta_usuarios(cls):
        print(f"Temos {cls.contador} usuarios no sistema")

    def __init__(self, nome2, sobrenome2, email2, senha2):
        self.__id = Usuario2.contador + 1
        self.__nome = nome2
        self.__sobrenome = sobrenome2
        self.__email = email2
        self.__senha = senha2
        Usuario2.contador = self.__id

    def correr(self, metros):
        print(f'{self.__nome} está correndo {metros}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


user4 = Usuario2("Marlon", "Brandon", "brandini@gmail.com", "098765432")
user5 = Usuario2("Marlon", "Brandon", "brandini@gmail.com", "098765432")
user6 = Usuario2("Marlon", "Brandon", "brandini@gmail.com", "098765432")
user7 = Usuario2("Marlon", "Brandon", "brandini@gmail.com", "098765432")
print(user4.conta_usuarios())

print("Exercício 1 ------------------------------------------------")

"""
Adição de Método

Na classe ContaCorrente, adicione um método chamado depositar que permita ao usuário depositar uma certa quantia em 
dinheiro na conta corrente. O método deve receber um parâmetro valor e aumentar o saldo da conta corrente por esse 
valor.

l38:    def depositar(self, valor):
            self.__saldo += valor
"""

print("Exercício 2 ------------------------------------------------")

"""
Validação de Senha

Na classe Usuario, descomente o método checa_senha. Este método deve ser usado para verificar se a senha fornecida pelo 
usuário ao fazer login está correta. Implemente este método de modo que ele compare a senha fornecida com a senha 
armazenada na classe Usuario.


    def checa_senha(self, senha):
        if self.__senha == senha:
            return f"Seja bem-vindo(a), {self.__nome}!"

"""

print("Exercício 3 ----------------------------------------------------")

"""
Contagem de Usuários

Na classe Usuario2, crie um método de classe chamado conta_usuarios que imprima o número total de usuários no sistema. 
Utilize a variável de classe contador para acompanhar o número de usuários e atualizá-la conforme novos usuários são 
criados.
"""


