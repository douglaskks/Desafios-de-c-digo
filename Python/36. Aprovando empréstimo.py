"""

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

"""

valorRequisitado = float(input('Digite o valor da casa que deseja comprar: '))
salario = float(input('Digite o seu salário: '))
anosPagar = int(input('Digite em quantos anos deseja pagar: '))

anoCorreto = anosPagar * 12
prestacaoMensal = valorRequisitado / anoCorreto
porcentagemSalario = (salario * 30) / 100

if prestacaoMensal > porcentagemSalario:
    print(f'O valor R{porcentagemSalario} é um valor baixo')
    print('Empréstimo negado!')
else:
    print(f'Parcelas de R${prestacaoMensal} por mês')
    print('Empréstimo concedido!')

