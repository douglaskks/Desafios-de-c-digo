import sys

valor = int(input("Digite um valor de 3 dígitos: \n"))
if(valor < 100 or valor > 999):
    sys.exit()
else:
    valorConvertido = str(valor)
    valorInvertido = valorConvertido[::-1]
    print(f"O valor {valor} invertido é igual a {valorInvertido}")