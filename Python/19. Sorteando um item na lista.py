import random

lista1 = []

for i in range(0, 4):
    print(f'Digite o nome do {i+1}° aluno: ')
    nome = input()
    lista1.append(nome)

aleatorio = random.choice(lista1)
print(f'O aluno escolhido foi {aleatorio}')