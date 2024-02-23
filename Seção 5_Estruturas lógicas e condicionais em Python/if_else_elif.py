"""
ESTRUTURAS CONDICIOANAIS IF/ELSE/ELIF

O ELIF é o ELSE IF do JavaScript.
"""

idade = 29

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem dezoito anos')
elif idade == 30:
    print('Tem 30 anos')
else:
    print('Maior de idade')

"""
Veja como fica bem limpo o código
Podemos colocar varios elifs inclusive, com exclusividade para um, como nos 30 anos que colocamos acima.
"""

"""
Para ficar de acordo com a PEP8, temos que deixar uma linha vazia no final do código.
"""

"""
Considere a seguinte situação e utilize estruturas condicionais para determinar a categoria de idade:

idade = 22

Tarefa:
- Se a pessoa tem menos de 20 anos, exiba a mensagem "Jovem".
- Se a pessoa tem exatamente 20 anos, exiba a mensagem "Vinte anos".
- Se a pessoa tem exatamente 25 anos, exiba a mensagem "Vinte e cinco anos".
- Caso contrário, exiba a mensagem "Idade desconhecida".
"""

idade = 22

if idade < 20:
    print('Jovem')
elif idade == 20:
    print('Vinte anos')
elif idade == 25:
    print('Vinte e cinco anos')
else:
    print('Idade desconhecida')

print('Exercício 2 ---------------------------------------')

"""
Dado um sistema de classificação de produtos com as seguintes categorias, elabore uma estrutura condicional utilizando 
if, elif e else:

codigo_produto = 'B123'
quantidade = 5

Categorias:
- A: Se a quantidade for maior que 10, exiba "Produto da categoria A: estoque alto".
- B: Se o código do produto começar com 'B', exiba "Produto da categoria B: verifique o estoque".
- C: Se a quantidade for menor ou igual a 10 e o código não for 'B123', exiba "Produto da categoria C: estoque baixo".
- D: Caso contrário, exiba "Produto de categoria desconhecida".
"""

codigo_produto = 'B123'
quantidade = 5

if quantidade > 10:
    print('Produto da categoria A: estoque alto')
elif codigo_produto.strip()[0] == 'B':
    print('Produto da categoria B: verifique o estoque')
elif quantidade < 10 and codigo_produto != 'B123':
    print('Produto da categoria C: estoque baixo')
else:
    print('Produto de categoria desconhecida')

"""
Mais uma vez: split() é para dividir variáveis que já contam com divisões internas, já o strip() serve para dividir 
uma paravra única em uma string.
"""
