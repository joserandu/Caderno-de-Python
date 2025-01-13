"""
ATRIBUTOS

Atributos representam as características do objeto. Ou seja, pelos atributos nos conseguimos representar
computacionalmente os estados de um objeto.

Em python dividimos o atributos em 3 grupos:
    - Atributos de instancia:
    - Atributos de classe:
    - Atributos dinamicos
"""

print("Atributos de instância --------------------------------------------class Lampada:/def __init__():self.cor = cor")

"""
São atributos declarados dentro do método construtor
    - O método construtor é um método especial para a construção do objeto.
    - Em Java uma classe Lampada, incluindo o seus atributos ficaria mais ou menos assim:
    
        public class Lampada(){
            private int voltagem;
            private String cor;
            private Boolean ligada = false;
            
            
            public Lampada(int voltagem, String cor){
                this.voltagem = voltagem;
                this.cor = cor;
            }
        }
        
"""


class Lampada:

    def __init__(self, voltagem, cor):  # o método __init__ é o método construtor do python.
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""
Tudo o que está dentro de uma classe chamamos de método.

Perceba que o __init__ é um método
    Toda função dentro de uma classe é um método.
    
SELF é um definidor de atributo que fica dentro de método construtor.
    Não é uma regra essa palavra, mas é uma convenção, e sempre utilizamos ela.
    É o próprio objeto.
    Com ele a gente está querendo mostrar o que é que estamos querendo associar.
"""

print("Atributos públicos e privados -------------------------------------------------------------self.__senha = senha")

"""
Se um atributo é privado, a gente só pode acessar ele dentro da classe na qual ele foi declarado.
    Ele também não fica visivel em outras classes.
    
Se ele é público a gente consegue ver ele em outras partes do projeto.
    Por convenção ficou convencido que todo atributo de uma classe é público. Ou seja, pode ser acessado em todo o 
    projeto, caso quiramos demonstrar que determinado atributo deve ser tratado como privado, utiliza-se duplo 
    underscore no inicio do seu nome (__)
        Isso é conhecido como Name Mangling.
    Até agora colocamos classes de atributos públicos.            
            
A abordagem do python deixou mais flexivel.
"""


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha  # __

    # Name Mangling
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


"""
Isso é uma convenção, pois o python ainda deixa que acessemos os atributos fora da classe.
"""

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)  # AttributeError

print(user._Acesso__senha)  # Name Mangling

"""
Com isso a gente consegue o acesso à atributos privados, mas não devemos fazer.
Nesse exemplo colocamos o _Acesso porque estamos fora da classe.
"""

# Atributos de instancia

"""
Significa que ao criamos instancias de uma classe todas as instâncias terão esses atributos.
"""

user1 = Acesso("user1@gmail.com", "123456")
user2 = Acesso("user2@gmail.com", "654321")

user1.mostra_email()
user2.mostra_email()

print("Atributos de classe---------------------------------------------------------------class Produto:/imposto = 1.03")

"""
São atributos que são declarados diretamente na classe, ou seja, fora do construtor, geralmente já inicalizamos um 
valor e esse valor é compartilhado entre todas as instâncias da classe. Ao invés de cada instancia da classe ter os 
seus próprios valores como é o caso dos atributos de instancia, com esse tipo, terão o mesmo valor para esse atributo.
"""


class Produto2:

    # Atributos de classe:
    imposto = 1.05
    contador = 0  # 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto2.contador + 1  # 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto2.imposto
        Produto2.contador = self.id  # valor do contador atualizado


produto1 = Produto2("PlayStation 2", "Video Game", 2300)
produto2 = Produto2("Xbox S", "Video Game", 4500)

# Acesso a atributo de instância
print(produto2.valor)
print(produto2.valor)

"""
Não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe.
"""

# Acesso correto de um atributo de classe.
print(Produto2.imposto)

print("Contador e id --------------------------------------------------------------------------------print(produto.id)")

"""
O atributo contador vai contar quantas vezes foi colocados objetos na classe
"""

print(produto1.id)
print(produto2.id)
print(produto2.imposto)

"""
OBS: Em linguagens como Java, os atributos de classe são chamados de atributos ESTÁTICOS, o que resume bem a ideia 
deles.
"""

print("Atributos dinâmicos------------------------------------------------------------------------produto2.peso = 5 kg")

"""
Um atributo de instancia que pode ser criado em tempo de execução.

OBS: O atributo dinâmico será exclusivo da instancia que o criou.
"""

produto1 = Produto2("PlayStation 2", "Video Game", 2300)
produto2 = Produto2("Arroz", "Mercearia", 5.99)

# Criando um novo atributo
produto2.peso = "5 Kg"

print(f'Produto: {produto2.nome} \nDescrição: {produto2.descricao} \nValor: {produto2.valor} \nPeso: {produto2.peso}')

"""
Não é muito comum a gente usar esse tipo de atributos, mas é possível.
"""

print("Deletando atributos---------------------------------------------------------------------------del produto.valor")

print(produto1.__dict__)  # Vemos aqui um dicionario com os atributos.
print(produto2.__dict__)

del produto2.valor  # Atributo estático
del produto2.peso  # Atributo dinâmico

print(produto1.__dict__)  # Perceba a mudança
print(produto2.__dict__)

<<<<<<< HEAD
<<<<<<< HEAD
print("Exercício 1 ----------------------------------")
=======
print("Exercício 1 ------------------------------------------------------Marca: {carro.marca} | Modelo: {carro.modelo}")
>>>>>>> 8db86c2 (Venv)
=======
print("Exercício 1 ----------------------------------")
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61

"""
Identificação de Atributos:
a. Crie uma classe chamada Carro com os seguintes atributos de instância:
- marca
- modelo
- ano
b. Instancie dois objetos da classe Carro com informações diferentes e imprima os valores dos atributos de cada objeto.
"""


class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


carro = Carro("Ford", "Ka", "2019")
carro2 = Carro("Chevrolet", "Onix", "2015")

print(f"Marca: {carro.marca} \nModelo: {carro.modelo} \nAno: {carro.ano}\n")
print(f"Marca: {carro2.marca} \nModelo: {carro2.modelo} \nAno: {carro2.ano}\n")

<<<<<<< HEAD
<<<<<<< HEAD
print("Exercício 2 ------------------------------------------------------------")
=======
print("Exercício 2 ------------------------------------------------------(f'Total de pessoas: {Pessoa.total_pessoas}')")
>>>>>>> 8db86c2 (Venv)
=======
print("Exercício 2 ------------------------------------------------------------")
>>>>>>> dc79b85fda33497856b39ea91eb6315d24a04c61

"""
Atributos de Classe e Instância:
a. Defina uma classe chamada Pessoa com um atributo de classe chamado total_pessoas inicializado com o valor 0.
b. Implemente um método de instância chamado registrar_pessoa() que incrementa o valor do atributo de classe 
total_pessoas toda vez que um novo objeto da classe for criado.
c. Instancie três objetos da classe Pessoa e imprima o valor de total_pessoas após a criação de cada objeto.
"""


class Pessoa:

    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1


pessoa1 = Pessoa("Juliana")
print("Total de pessoas:", Pessoa.total_pessoas)

pessoa2 = Pessoa("Rayane")
print("Total de pessoas:", Pessoa.total_pessoas)

pessoa3 = Pessoa("Giovanna")
print("Total de pessoas:", Pessoa.total_pessoas)

print("Exercício 3 ------------------------------------------------------------------------------animal.som = 'Latido'")

"""
Atributos Dinâmicos:
a. Crie uma classe chamada Animal com os atributos de instância padrão nome e tipo.
b. Instancie um objeto da classe Animal e adicione um novo atributo dinâmico chamado som com um valor que represente o 
som que o animal faz.
c. Imprima os valores de todos os atributos do objeto.
"""


class Animal:

    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo


animal = Animal("Cão", "Caramelo")

animal.som = "Latido"

print(f"Animal: {animal.nome} \nTipo: {animal.tipo} \nSom: {animal.som}")
