"""

Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.

"""

entrada = int(input('Digite um valor para a tabuada: '))

for i in range(0, 11):
    print(f'{entrada} X {i} = {entrada * i}')