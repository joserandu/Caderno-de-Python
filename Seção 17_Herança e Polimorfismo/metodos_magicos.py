"""
MÉTODOS MÁGICOS

Métodos mágicos são todos os métodos que utilizam dunder (underscore).

dunder init: __init__()
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        """
        Perceba que estamos sobrescrevendo o método object

        Esse método serve para representar melhor a impressão da classe quando ela é impressa de maneira simples:
        print(livro1) por exemplo.

        Pode-se usar o __str__() também, dá o mesmo resultado.
            - Se colocar os dois, o str tem maior ordem de preferência
        """
        return f"Título: {self.titulo}\nAutor: {self.autor}\n"

    def __len__(self):
        return self.paginas

    def __del__(self):
        print("Um objeto do tipo livro foi deletado da memória")

    def __add__(self, outro):
        


livro1 = Livro("Python Rocks!", "Geek University", 400)
livro2 = Livro("Inteligencia Artificial com Python", "Geek University", 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

# del livro1
# print(livro1)

print(livro1.numero_paginas())
