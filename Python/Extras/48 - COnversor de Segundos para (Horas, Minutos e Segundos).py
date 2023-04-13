segundos = int(input("Digite o total de segundos: \n"))

horas = segundos / 3600
minutos = (segundos / 60) % 60
segundoM = segundosM = segundos % 60

print(f"Horas: {round(horas, 1)}")
print(f"Minutos: {round(minutos, 1)}")
print(f"Minutos: {round(segundosM, 1)}")