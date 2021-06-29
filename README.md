# Ex17-estruturaS-Python
Exercício da estrutura sequencial (PYTHON)


Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.



import math
import math as mt

metros = float(input("QUal o tamanho da área a ser pintada em Metros Quadrados ? "))

l1 = float(metros / 6)

if l1 <= 18:

    print("Vai usar apenas uma lata de tinta, valor de R$ 80.00")

else:

    x = mt.ceil(l1 / 18)

    valor = x * 80

    print("Vão ser necessárias {} Latas, E o valor a ser gasto R${}".format(x, valor))

lgaloes = float(metros / 6)

if lgaloes <= 3.6:

    print("Somente um galão, valor a ser gasto R$ 25.00")


else:

    y = mt.ceil(lgaloes / 3.6)
    valorG = y * 25

    print("É necessário {} galões, e o valor a ser gasto R${}".format(y,valorG))



MisturaLeG = float(metros / 6 )

resto = MisturaLeG % 18

divsG = resto / 3.6

if (divsG !=  int(divsG)):
    divsG = mt.ceil(divsG)
    custo = divsG * 25

    divvs6 = MisturaLeG //  18
    custo2 = divvs6 * 80
    folga = (custo + custo2) * 0.1
    custo3 = (custo + custo2) - folga
    print("Misturando latas e galoes se obtém, {} galoes e {} de latas, e o custo total é de {} ".format(divsG, divvs6,
                                                                                                         custo3))

else:
    custo = divsG * 25
    divvs6 = MisturaLeG // 18
    custo2 = divvs6 * 80
    folga = (custo + custo2) * 0.1
    custo3 = (custo + custo2) - folga
    print("Misturando latas e galoes se obtém, {} galoes e {} de latas, e o custo total é de {} ".format(divsG, divvs6,
                                                                                                         custo3))



  
