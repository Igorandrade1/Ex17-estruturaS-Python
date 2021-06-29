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



