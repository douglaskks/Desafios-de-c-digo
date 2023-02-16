"""

Elabore um programa que calcula o valor a ser pago por um produto.
Considerando seu preço normal e consição de pagamento:

-- Á vista / Dinheiro ou Cheque: 10% de desconto
-- Á vista no cartão: 5% de desconto
-- Em até 2x no cartão: Preço normal
-- 3x ou mais no cartão: 20% de juros

"""

print('=+' * 10, 'Lojas Americanas', '=+' * 10)
precoCompras = float(input('Digite o valor das compras: '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro / cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Opção: '))

if opcao == 1:

    valor = (precoCompras * 10) / 100
    valorCompras = precoCompras - valor

    print('=+' * 15)
    print('Como seu pagamento vai ser a vista ou cheque')
    print('Você terá um desconto de 10%')
    print(f'O valor das suas compras será de R${valorCompras}')
    print('=+' * 15)

elif opcao == 2:

    valor = (precoCompras * 5) / 100
    valorCompras = precoCompras - valor

    print('=+' * 15)
    print('Como seu pagamento vai ser no cartão a vista')
    print('Você terá um desconto de 5%')
    print(f'O valor das suas compras será de R${valorCompras}')
    print('=+' * 15)

elif opcao == 3:

    valor = precoCompras / 2

    print('=+' * 15)
    print('Como seu pagamento será em 2x no cartão')
    print('Não será cobrado nenhuma taxa de juros')
    print(f'O valor das suas compras será de 2x de R${valor}')
    print('=+' * 15)

elif opcao == 4:

    valor = (precoCompras * 20) / 100
    opcao2 = int(input('Em quantas parcelas deseja dividir? '))
    novoValor = precoCompras + valor
    mostrarValor = novoValor / opcao2

    print('=+' * 15)
    print(f'Como seu pagamento será de {opcao2}x')
    print('Então será cobrado uma taxa de 20% de Juros')
    print(f'Sua compra fica em {opcao2}x de R${mostrarValor}')
    print(f'Ao todo sua compra de R${precoCompras}, vai ficar por R${novoValor}')
    print('=+' * 15)
