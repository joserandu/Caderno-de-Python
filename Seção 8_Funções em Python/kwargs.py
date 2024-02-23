"""
**KWARGS

Poderiamos chamar esse parâmetro de **qualquer_coisa, mas por convenção, chamamos de **kwargs.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parâmetros nomeados e transforma esses parâmetros extras em um DICIONÁRIO.
"""

print('Exemplo ---------------------------------------------------------------------------------------------(**kwargs)')


def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(Marcos='verde', Julia='rosa', Manoel='Vermelho', Fernando='Azul')

"""
Fazendo isso, os dados são impressos em formato de dicionário: {chave: valor}.
"""

print('Passando mais de um kwargs para a função ----------------------------------------------------------chave, valor')


def cores_favoritas2(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.lower()}')


cores_favoritas2(marcos='verde', Julia='rosa', manoel='Vermelho', Fernando='Azul')
cores_favoritas2()

"""
Não esqueça de utilizar o método .items(), pois estamos acessando um dicionário.

Deixei alguns nomes com letra minúscula para poder relembrar o método title() e coloquei .lower() para deixar a 
primeira letra das cores em minúscula.
Os parâmetros *args e **kwargs não são obrigatórios, portanto, podemos não mardar nenhum argumento que o sistema 
funciona normalmente.
"""

print('Aumentando a complexidade ----------------------------------if "geek" in kwargs and kwargs["geek"] == "Python":')

"""
Esse é um exemplo bem besta mas ajuda a entender a idea principal. Com isso podemos fazer uma função que se mandar 
uma chave ou um valor é possivel ter retornos específicos para cada um.
"""


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

"""
Nesse exemplo, encaminhamos na função de que se o valor da chave ['geek'] == 'Python', caso seja retornado outra 
coisa, a função retorna o que foi enviado e geek logo em seguida. E se não for mandado nada, nem mesmo a chave 
'geek', imprime a última opção.
"""

print('Ordem dos parâmetros para entrada nas funções ---------------------------(nome, *args, solteiro=True, **kwargs)')

"""
A ordem dos primeiros parâmetros para os últimos é:

1º Parâmetros obrigatórios
2º *args
3º Parâmetros default (parâmetros não-obrigatórios)
4º *kwargs
"""


def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos de idade')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Júlia')
minha_funcao(18, 'Maycon', 4, 5, 3, solteiro=True)
minha_funcao(18, 'Felipe', eu='Não', voce='vai')

"""
Os parâmetros vão se encaixar aonde os argumentos estiverem no formato, por isso a ordem dos parâmetros é tão 
importante.
"""

print('Mais um exemplo da importância da ordem dos parâmetros ------------------(a, *args, instrutor="geek", **kwargs)')


def mostra_info(a, b, *args, instrutor='geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

print('Desempacotando com **kwargs -------------------------------------------------------------------{kwargs["nome"]}')


def mostra_kwargs(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Leonardo', 'sobrenome': 'Di Caprio'}

print(mostra_kwargs(**nomes))

"""
A partir do duplo asterisco a gente desempacota o dicionário. Repito, não precisa ser kwargs, mas é convenção, 
então use.
"""

print('Exercício 1 ----------------------------------------------------------operação = kwargs.get("operacao", "soma")')

"""
Função de Calculadora com kwargs

Crie uma função chamada calculadora_personalizada que aceita dois números como parâmetros obrigatórios (num1 e num2). 
Além disso, permita que a função receba parâmetros adicionais usando **kwargs para realizar operações personalizadas.

A função deve suportar as seguintes operações:

Soma: Se o parâmetro operacao for 'soma' ou não for fornecido.
Subtração: Se o parâmetro operacao for 'subtracao'.
Multiplicação: Se o parâmetro operacao for 'multiplicacao'.
Divisão: Se o parâmetro operacao for 'divisao'.
Retorne o resultado da operação. Se a operação não for reconhecida, retorne uma mensagem indicando que a operação não é
suportada.

Exemplo de uso:

resultado1 = calculadora_personalizada(num1=10, num2=5)
print(resultado1)  # Saída esperada: 15 (soma)

resultado2 = calculadora_personalizada(num1=10, num2=5, operacao='subtracao')
print(resultado2)  # Saída esperada: 5 (subtração)

resultado3 = calculadora_personalizada(num1=5, num2=2, operacao='multiplicacao')
print(resultado3)  # Saída esperada: 10 (multiplicação)

resultado4 = calculadora_personalizada(num1=8, num2=2, operacao='divisao')
print(resultado4)  # Saída esperada: 4 (divisão)
"""


def calculadora_personalizada(num1, num2, **kwargs):
    operacao = kwargs.get('operacao', 'soma')

    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'divisao':
        return num1 / num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    else:
        return 'Digite uma operação válida'


"""
A linha operacao = kwargs.get('operacao', 'soma') serve para obter o valor associado à chave 'operacao' no dicionário 
kwargs.

A função get é usada para acessar o valor associado a uma chave em um dicionário. Neste caso, se a chave 'operacao' 
estiver presente em kwargs, operacao receberá o valor correspondente a essa chave. Se a chave não estiver presente, o 
método get retornará o valor padrão, que neste caso é 'soma'.

Essa abordagem é útil porque permite que a função seja chamada sem a necessidade de fornecer explicitamente a chave 
'operacao' em todos os casos. Se a chave estiver ausente, a função assume a operação padrão como sendo uma soma. Isso 
torna o código mais flexível e evita erros quando a chave não é fornecida.
"""

resultado1 = calculadora_personalizada(num1=10, num2=5)
print(resultado1)  # Saída esperada: 15 (soma)

resultado2 = calculadora_personalizada(num1=10, num2=5, operacao='subtracao')
print(resultado2)  # Saída esperada: 5 (subtração)

resultado3 = calculadora_personalizada(num1=5, num2=2, operacao='multiplicacao')
print(resultado3)  # Saída esperada: 10 (multiplicação)

resultado4 = calculadora_personalizada(num1=8, num2=2, operacao='divisao')
print(resultado4)  # Saída esperada: 4 (divisão)

print('Exercício 2 ---------------------------------------------if list(palavra.lower() == list(palavra[::-1].lower():')

"""
Verificação de Palíndromo com kwargs

Crie uma função chamada verifica_palindromo que aceita uma string como parâmetro obrigatório (palavra). Utilize **kwargs 
para permitir parâmetros adicionais.

A função deve verificar se a palavra é um palíndromo (uma palavra que se lê da mesma forma de trás para frente). Retorne 
True se for um palíndromo e False caso contrário.

Adicione suporte para um parâmetro opcional chamado ignorar_maiusculas que, se for True, ignorará diferenças entre 
letras maiúsculas e minúsculas ao verificar o palíndromo.

Exemplo de uso:

resultado1 = verifica_palindromo(palavra='radar')
print(resultado1)  # Saída esperada: True (radar é um palíndromo)

resultado2 = verifica_palindromo(palavra='Python')
print(resultado2)  # Saída esperada: False (Python não é um palíndromo)

resultado3 = verifica_palindromo(palavra='AnA', ignorar_maiusculas=True)
print(resultado3)  # Saída esperada: True (ignora maiúsculas, 'AnA' é um palíndromo)
"""


def verifica_palindromo(palavra, **kwargs):
    if list(palavra.lower()) == list(palavra[::-1].lower()):
        return f'{palavra} é um palindromo'
    return f'{palavra} não é um palindromo'


resultado1 = verifica_palindromo(palavra='radar')
print(resultado1)  # Saída esperada: True (radar é um palíndromo)

resultado2 = verifica_palindromo(palavra='Python')
print(resultado2)  # Saída esperada: False (Python não é um palíndromo)

resultado3 = verifica_palindromo(palavra='Ana', ignorar_maiusculas=True)
print(resultado3)  # Saída esperada: True (ignora maiúsculas, 'AnA' é um palíndromo)

print('Exercício 3 ------------------------------------------------------------inverter = kwargs.get("inverter", True)')

"""
Concatenação de Listas com kwargs

Crie uma função chamada concatena_listas que aceita duas listas como parâmetros obrigatórios (lista1 e lista2). Use 
**kwargs para permitir parâmetros adicionais.

A função deve suportar um parâmetro opcional chamado inverter que, se for True, inverterá a ordem dos elementos nas 
listas antes de concatená-las.

Retorne a lista resultante após a concatenação.

Exemplo de uso:

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado1 = concatena_listas(lista1=lista_a, lista2=lista_b)
print(resultado1)  # Saída esperada: [1, 2, 3, 4, 5, 6] (concatenação padrão)

resultado2 = concatena_listas(lista1=lista_a, lista2=lista_b, inverter=True)
print(resultado2)  # Saída esperada: [6, 5, 4, 3, 2, 1] (concatenação com inversão)
"""


def concatena_listas(lista1, lista2, **kwargs):
    inverter = kwargs.get('inverter', False)

    if inverter:
        lista1.reverse()
        lista2.reverse()

    resultado = lista1 + lista2
    return resultado


# Exemplo de uso
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado1 = concatena_listas(lista1=lista_a, lista2=lista_b)
print(resultado1)  # Saída esperada: [1, 2, 3, 4, 5, 6] (concatenação padrão)

resultado2 = concatena_listas(lista1=lista_a, lista2=lista_b, inverter=True)
print(resultado2)  # Saída esperada: [6, 5, 4, 3, 2, 1] (concatenação com inversão)
