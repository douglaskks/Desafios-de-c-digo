soma = 0
confirmacao = str
contagem = 0
maior = 0
menor = 0

entrada = int(input('Digite um número: '))
contagem += 1
if entrada > maior:
    maior = entrada
if entrada < maior:
    menor = entrada
confirmacao = str(input('Deseja continuar? [S/N] '))
soma += entrada

while confirmacao == 'S':
    entrada = int(input('Digite um número: '))
    if entrada > maior:
        maior = entrada
    if entrada < maior:
        menor = entrada
    contagem += 1
    soma += entrada
    confirmacao = str(input('Deseja continuar? [S/N] '))
    
media = soma/contagem

print(f'Você digitou {contagem} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')