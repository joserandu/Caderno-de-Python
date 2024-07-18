"""
DUNDER NAME E DUNDER MAIN

Dunder -> Dubble underline
Dunder name -> __name__
Dunder main -> __main__

Em Python são utilizados dunder para criar funções, atributos, propriedades e etc. utilizando duble dunder para não
gerar conflito com os nomes desses elementos na programação.
    - Na linguagem C, temos um programa da seguinte forma:
        - int main(){      return 0;}
            - Isso é um programa C
    - Em java precisamos:
        - public static void main(String[] args){       }
    - Se executarmos um módulo Python diretamente na linha de comando, internamente o Pyhon atribuirá à variável
    __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.
"""

from dunder_auxiliar import soma_impares

"""
Se importamos uma função de outro arquivo e esse outro arquivo tem um print(), 
será impresso no nosso terminal também o print() do documento que importamos. E para resolver isso, usamos o __name__ e 
__main__.
"""

print(soma_impares([1, 2, 3, 4, 5, 6]))

"""
Perceba que usando o __name__ a função imprimiu só o que a gente queria.

Mas geralmente, quando fazemos módulos não usamos o print() neles.
main significa principal.

A variável name tem como valor o nome do arquivo.
"""
