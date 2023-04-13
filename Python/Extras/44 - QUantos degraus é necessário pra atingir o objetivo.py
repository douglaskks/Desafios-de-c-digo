alturaDegrau = float(input("Digite a altura do degrau em centímetros: \n"))
alturaObjetivo = float(input("Qual a altura desejada em metros? \n"))

convertDegrau = alturaDegrau * 0.01
resultadoAltura = alturaObjetivo / convertDegrau

print(resultadoAltura)