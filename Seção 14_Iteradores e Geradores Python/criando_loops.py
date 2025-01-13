"""
CRIANDO SUA PRÓPRIA VERSÃO DE LOOP


"""

for numero in [1, 2, 3, 4, 5]:
    print(numero)

for letra in "Geek University":
    print(f"{letra}")

"""
Por baixo dos panos, o python está fazendo isso:
"""

iter([1, 2, 3, 4, 5])
iter("Geek University")

print("Definindo o próprio loop --------------------------------------")


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for("Geek University")
