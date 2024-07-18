"""
MODULO COLLECTIONS - DEQUE

Podemos dizer que o deque é uma lista de alta performace. É o mais parecido com lista.
"""

from collections import deque  # Importando

print('Criando deques -----------------------------------------------------------------------------------deque("geek")')

deq = deque('geek')
print(deq)

"""
O Deque irá transformar a string em uma lista de strings, igualzinho o método list, com a diferença que será impresso 
um deque() na frente.
"""

print('Adicionando elementos na lista normal -----------------------------------------------------list("") append("x")')

listaNormal = list('geek')
listaNormal.append('y')
print(listaNormal)

"""
Com esse método, será colocado o elemento sempre ao final da lista.
"""

print('Adicionando no começo da lista --------------------------------------------------------------------appendleft()')

deq.appendleft('k')
print(deq)

"""
appendleft() irá adicionar à esquerda, ou seja, em primeiro.
"""

print('Removendo elementos do inicio e fim-----------------------------------------------------------.pop() .popleft()')

print(deq.pop())  # Tirar o último
print(deq.popleft())  # Tirar o primeiro
print(deq)

print('Exercício 1 -------------------------------')

"""
Manipulação de Lista com Deque

Crie um deque chamado minha_lista contendo os elementos "a", "b", "c". Adicione os elementos "x" e "y" ao final do 
deque. Em seguida, adicione o elemento "z" no início do deque. Por fim, remova o último elemento e o primeiro 
elemento do deque e imprima o resultado.
"""

minha_lista = deque('abc')

minha_lista.append('x')
minha_lista.append('y')
minha_lista.appendleft('z')
minha_lista.pop()

print(minha_lista)

print('Exercício 2 -------------------------')

"""
Fila com Deque

Simule o funcionamento de uma fila utilizando um deque. Adicione os números de 1 a 5 ao deque, representando os 
clientes que chegaram. Em seguida, atenda (remova) os clientes da fila um por um, imprimindo o número de cada 
cliente atendido.
"""

fila = deque('12345')

print(fila.popleft())
print(fila.popleft())
print(fila.popleft())
print(fila.popleft())
print(fila.popleft())

print('Exercício 3 ------------------------------------')

"""
Pilha com Deque

Simule o funcionamento de uma pilha utilizando um deque. Adicione os números de 1 a 5 ao deque, representando itens 
empilhados. Em seguida, desempilhe (remova) os itens da pilha um por um, imprimindo o número de cada item desempilhado.
"""

pilha = deque('12345')

print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
print(pilha.pop())
