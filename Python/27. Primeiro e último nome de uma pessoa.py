nome = str(input())
nome1 = nome.split()
nome1.reverse()

pessoa = sorted(nome1, reverse=False)

print(f'Prazer em conhecê-lo {pessoa[0]}')
print(f'Seu primeiro nome é {pessoa[0]}')
print(f'E seu último nome é {nome1[0]}')
