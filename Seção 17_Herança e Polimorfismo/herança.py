"""
HERANÇA (INHERITANCE)

A ideia de herança é de reaproveitar código. Também extender nossas classes.
    - Tentar fazer classes genéricas.
    - Com a herança a partir de uma classe existente nós extendemos outra classe que possa herdar atributos e métodos
    da classe herdada.

Imagine um sistema de banco que tem as seguintes entidades e seus atributos:

Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Ambas as classes tem nome, sobrenome e cpf.

Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada e a classe herdada é
conhecida por:

Classe Pessoa:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;

Quando uma classe herda de outra classe ela é chamada de:
    - Sub Classe;
    - Classe Filha;
    - Classe específica;
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # O pulo do gato, método super(). É a super classe sendo executada.
        self.__renda = renda

    def nome_completo(self):
        """Sobrescrita de método"""
        return f"{super().nome_completo()} | Renda: {self.__renda}"  # Atenção aqui.


class Funcionario(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente("Angelina", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

"""
Pode-se acessar dessa maneira também, mas não é comum:
Pessoa.__init__(self, nome, sobrenome, cpf)
"""

print(cliente1.__dict__)
print(funcionario1.__dict__)

print("Sobrescrita de métodos --------------------------------------------------------------------------------")

"""
Ocorre quando reescrevemos um método de uma superclasse na classe filha
"""

print("Exercício 1 -------------------------------------------------------------------------")

"""
Sobrescrita de Método

Considere a classe Cliente que herda da classe Pessoa. Implemente uma classe ClienteVIP que também herda de Pessoa, 
porém, sobrescreva o método nome_completo para incluir informações adicionais específicas para clientes VIP, como um 
status VIP ou benefícios especiais.
"""

print("Exercício 2 -----------------------------------------------------------------------")

"""
Adição de Atributos

Crie uma nova classe chamada Gerente que herda de Funcionario. Adicione um novo atributo específico para gerentes, como 
departamento, e atualize o método nome_completo para incluir essa informação adicional
"""

print("Exercício 3 ----------------------------------------------------------------------")

"""
Adição de Atributos

Crie uma nova classe chamada Gerente que herda de Funcionario. Adicione um novo atributo específico para gerentes, como 
departamento, e atualize o método nome_completo para incluir essa informação adicional
"""
