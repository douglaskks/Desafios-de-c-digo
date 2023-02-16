print('Digite o salário do funcionário: ')
salario = float(input())

print('Este funcionário vai receber um aumento ou diminuição de salário? ')
print('1 - Aumento')
print('2 - diminuição')
ajuste = int(input())

if ajuste == 1:
    print('Digite a porcentagem a ser aumentada no salário do funcionário: ')
    porcentagem = float(input())

    aumento = (salario * porcentagem) / 100
    salarioAumentado = salario + aumento

    print('__' * 20)
    print(f'O funcionário que ganhava R${salario}, com {porcentagem}% de aumento')
    print(f'passa a receber R${salarioAumentado}')
    print('__' * 20)

elif ajuste == 2:
    print('Digite a porcentagem a ser diminuída do salário do funcionário: ')
    porcentagem = float(input())

    diminuicao = (salario * porcentagem) / 100
    salarioDiminuido = salario - diminuicao

    print(print('--' * 20))
    print(f'O funcionário que ganhava R${salario}, com {porcentagem}% de diminuição')
    print(f'passar a receber R${salarioDiminuido}')
    print('__' * 20)
