"""

Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%.

Para inferiores ou iguais calcule um aumento de 15%

"""

salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    salarioCalculo = (salario * 15) / 100
    novoSalario = salario + salarioCalculo
    diferenca = novoSalario - salario

    print(f'O novo salário do funcionário será R${novoSalario}')
    print(f'teve um aumento de R${diferenca}')

elif salario > 1250:
    salarioCalculo = (salario * 10) / 100
    novoSalario = salario + salarioCalculo
    diferenca = novoSalario - salario

    print(f'O novo salário do funcionário será R${novoSalario}')
    print(f'teve um aumento de R${diferenca}')
