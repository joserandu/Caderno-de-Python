"""
ESTRUTURAS LÓGICAS: AND, OR, NOT, IS

São operadores:
    Unários:
        not: não
        is: é

    Binários:
        and: Os dois tem que ser True.
        or: Um ou outro, ou até os dois, tem que ser True.
"""

ativo = True
logado = False

print('AND ----------------------------------------------------------------------------------------if ativo and logado')

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu email.')

print('OR ------------------------------------------------------------------------------------------if ativo or logado')

if ativo or logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu email')

print('NOT ----------------------------------------------------------------------------------------------if not ativo:')

if not ativo:  # Se NÃO ativo
    print('Você precisa ativar a sua conta. Por favor, cheque seu email.')
else:
    print('Bem vindo usuário!')

print('IS ------------------------------------------------------------------------------------------if ativo is False:')

if ativo is False:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque seu email')

# Outra forma de escrever:
ativo = True
logado = False

print(ativo is True)

"""
Essa ultima forma é como se fosse uma pergunta: ativo é verdadeiro?
"""

print('Exercício 1 --------------------------------------------------------------------if tem_permissao or esta_logado')

"""
Dada a seguinte situação, utilize os operadores lógicos aprendidos para determinar se a ação deve ser realizada ou não.

Situação:
tem_permissao = True
esta_logado = False

Tarefa:
- Se a pessoa tem permissão OU está logada, exiba a mensagem "Acesso concedido".
- Caso contrário, exiba a mensagem "Acesso negado".
"""

tem_permissao = True
esta_logado = False

if tem_permissao or esta_logado:
    print('Acesso concedido.')
else:
    print('Acesso negado.')

print('Exercício 2 ---------------------------------------------------------------elif idade < 18 and tem_responsavel:')

"""
Considere o seguinte cenário e elabore uma expressão condicional usando os operadores lógicos aprendidos para determinar
o resultado final.

- Cenário:
idade = 25
tem_carteira = True
tem_responsavel = False

Tarefa:
- Se a pessoa tem mais de 18 anos E possui carteira de motorista, exiba a mensagem "Pode dirigir".
- Se a pessoa tem menos de 18 anos E tem um responsável, exiba a mensagem "Pode dirigir com supervisão".
- Caso contrário, exiba a mensagem "Não pode dirigir".
"""

idade = 25
tem_carteira = True
tem_responsavel = False

if idade > 18 and tem_carteira:
    print('Pode dirigir')
elif idade < 18 and tem_responsavel:
    print('Pode dirigir com supervisão')
else:
    print('Não pode dirigir')
