"""
TIPO BOOLEANO

Foi criada pelo George Boole

2 constantes: True e False
Atenção: Letras Maiúsculas: True e False.
"""

ativo = True
print(ativo)

print('Operações básicas com not ----------------------------------------------------------------------------------not')

"""
Fazendo a negação, se o valor boleano for verdadeiro, ele será falso e vice-versa
"""

print(not ativo)

print('Operações básicas com or -----------------------------------------------------------------------ativo or logado')

"""
É uma operação binária, ou seja, depende de dois valores, ou um ou outro deve ser verdadeiro:
True or True = True
False or False = False
True or False = True
"""

logado = False
print(ativo or logado)

print('Operações básicas com and ---------------------------------------------------------------------ativo and logado')

"""
Também é uma operação binaria que depende de dois valores, e os dois devem ser True para retornar verdadeiro
True or True = True
False or False = False
True or False = False
"""

print(ativo and logado)

print('Exercício 1 --------------------------------------')

"""
Crie um programa em Python que represente uma porta de acesso. A porta deve estar inicialmente trancada (locked). 
O programa deve realizar as seguintes operações:

- Exibir o estado atual da porta (trancada ou destrancada).
- Solicitar ao usuário que destranque a porta digitando a palavra-chave correta ("open").
- Após destrancar, exibir uma mensagem informando que a porta foi aberta com sucesso.

Dica:

- Utilize uma variável booleana para representar o estado da porta.
- Utilize a função input para receber a palavra-chave do usuário.
- Utilize estruturas condicionais (if, else) para verificar se a porta está trancada e se a palavra-chave está correta.
"""

print('A porta está trancada;')
resposta = input('Escreva a chave de acesso:')

if resposta == 'open':
    print('A porta foi destrancada com sucesso!')
else:
    input('Chave incorreta')

print('Exercício 2 ------------------------------------------------')

"""
Desenvolva um programa que simule uma calculadora simples. O usuário deve fornecer dois números e escolher uma operação 
entre soma, subtração, multiplicação e divisão. O programa deve realizar a operação desejada e exibir o resultado.

Dica:

- Utilize a função input para receber os dois números e a operação desejada.
- Utilize estruturas condicionais (if, elif, else) para determinar qual operação realizar.
- Considere tratar casos especiais, como a divisão por zero.
- Exiba o resultado da operação de forma amigável.
"""

print('Olá, seja bem-vindo a nossa calculadora pré-histórica! \n')
primeiro_numero = float(input('Digite o primeiro número: '))

operacao = input('Escolha a operação: (+, -, / ou *): ')

segundo_numero = float(input('Digite o segundo número: '))

resultado = None

if operacao == '+':
    resultado = primeiro_numero + segundo_numero
elif operacao == '-':
    resultado = primeiro_numero - segundo_numero
elif operacao == '*':
    resultado = primeiro_numero * segundo_numero
elif resultado == '/':
    resultado = primeiro_numero / segundo_numero
else:
    print('Coloque uma operação válida')

print(f'O resultado é {resultado}')

print('Usando um loop para que a pessoa possa voltar ao inicio em caso de erros ----------------------------while True')

while True:
    primeiro_numero = float(input('Digite o primeiro número: '))
    operacao = input('Escolha a operação: (+, -, / ou *): ')
    segundo_numero = float(input('Digite o segundo número: '))

    resultado = None

    if operacao == '+':
        resultado = primeiro_numero + segundo_numero
    elif operacao == '-':
        resultado = primeiro_numero - segundo_numero
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero
    elif operacao == '/':
        # Adicione um bloco para lidar com a divisão por zero
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
        else:
            print('Não é possível dividir por zero. Tente novamente.')
            continue
    else:
        print('Operação não reconhecida. Por favor, escolha uma das operações: +, -, / ou *')
        continue

    print(f'O resultado da operação é: {resultado}')

    reiniciar = input('Deseja realizar outra operação? (s/n): ')
    if reiniciar.lower() != 's':
        print('Programa encerrado.')
        break
