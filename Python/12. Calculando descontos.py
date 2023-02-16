print('Qual é o valor do produto? ')
valorProduto = float(input())
print('Quantos por cento de desconto você quer dar? ')
porcentagemDesconto = int(input())

valorDesconto = (valorProduto * porcentagemDesconto) / 100
valorReal = valorProduto - valorDesconto

print('_' * 30)
print(f'O produto que custava R${valorProduto}, agora com {porcentagemDesconto}% de desconto')
print(f'irá custar R${valorReal}')
print('_' * 30)
