"""

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo

"""


primeiroSegmento = float(input('Digite o primeiro segmento: '))
segundoSegmento = float(input('Digite o segundo segmento: '))
terceiroSegmento = float(input('Digite o terceiro segmento: '))

somaSegmentos1 = primeiroSegmento + segundoSegmento
somaSegmentos2 = segundoSegmento + terceiroSegmento
somaSegmentos3 = primeiroSegmento + terceiroSegmento

if somaSegmentos1 > terceiroSegmento:
    if somaSegmentos2 > primeiroSegmento:
        if somaSegmentos3 > segundoSegmento:
            print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os Segmentos acima não podem formar um triângulo!')