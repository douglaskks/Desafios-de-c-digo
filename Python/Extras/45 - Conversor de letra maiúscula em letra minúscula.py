entrada = str(input("Digite a letra maiúscula a ser convertida: \n"))

valor_entrada = ord(entrada)
valor_entradaMinuscula = valor_entrada + 32
letraMinuscula = chr(valor_entradaMinuscula)

print(f"A letra {entrada} Maiúscula convertida em Minúscula é {letraMinuscula}")