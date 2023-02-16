"""

Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.

"""

listaMaioridade = []
listaMenoridade = []

for i in range(1, 8):
    pergunta = int(input(f'Digite o ano de nascimento da {i}° pessoa: '))
    maioridade = 2017 - pergunta

    if maioridade < 18:
        listaMenoridade.append(pergunta)
    else:
        listaMaioridade.append(pergunta)

tamanhoMaioridade = len(listaMaioridade)
tamanhoMenoridade = len(listaMenoridade)

print(f'Ao todo tivemos {tamanhoMaioridade} pessoas maiores de idade!')
print(f'E também tivemos {tamanhoMenoridade} pessoas menores de idade')
