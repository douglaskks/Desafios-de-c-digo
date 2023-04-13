salarioBase = float(input("Digite seu salário base: \n"))
acrescimo = (salarioBase * 5) / 100
imposto = (salarioBase * 7) / 100
salarioTotal = (salarioBase - imposto)
salarioTotal = (salarioTotal + acrescimo)

print(f"O salário agora será de R${salarioTotal}")