import sys

Valor = int(input("Digite um valor de 4 dígitos: \n"))
if(Valor > 9999 or Valor < 1000):
    print("Valor inorreto!")
    sys.exit()
else:
    valorString = str(Valor)
    print(valorString[0])
    print(valorString[1])
    print(valorString[2])
    print(valorString[3])