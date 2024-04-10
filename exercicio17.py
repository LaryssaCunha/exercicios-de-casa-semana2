#pedir o tamanho em metros quadrados da área a ser pintada xxxxxxxx
#variavel1 = cobertura da tinta = 1litro/6m²
#variavel2 = custo lata = 18l = 80,00
#variavel3 = custo galao = 3,6l = 25,00

#informar ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações
	# comprar latas de 18 l
	# comprar apenas galões de 3,6 l =  area = 3.6 * 6 = 21,6m²
	# misturar latas e galões (fazer por ultimo)
    # area por lata = 18 * 6 = 108m²
# area litro

import math

area_cliente = float(input("Informe a área em metros quadrados que deseja pintar"))
area_lata = 108
area_galao = 21.6
custo_lata = 80
custo_galao = 25

def calcular_latas(area_cliente, area_lata):
    qtd_latas = math.ceil(area_cliente / area_lata)
    print(qtd_latas)
    return qtd_latas

def calcular_galoes(area_cliente, area_galao):
    qtd_galoes = math.ceil(area_cliente / area_galao)
    print(qtd_galoes)
    return qtd_galoes

def calcular_custo_latas(qtd_latas, custo_lata):
    custo_total_latas = math.ceil(qtd_latas * custo_lata)
    print(custo_total_latas)
    return custo_total_latas

def calcular_custo_galoes(area_cliente, qtd_galoes):
    custo_total_galoes = math.ceil(area_cliente * qtd_galoes)
    print(custo_total_galoes)
    return custo_total_galoes


qtd_latas = calcular_latas(area_cliente, area_lata)
qtd_galoes = calcular_galoes(area_cliente, area_galao)
custo_total_latas = calcular_custo_latas(qtd_latas, custo_lata)
custo_total_galoes = calcular_custo_galoes(qtd_galoes, custo_galao)

print("Nós temos três opções de comprar para te oferecer:")
print("A primeira é comprar somente latas. Serão necessários", str(qtd_latas), " latas e seu custo será de", str(custo_total_latas) "reais.")
print("A segunda opção é comprar somente galões. Serão necessários", str(qtd_galoes), " galões e seu custo será de ", str(custo_total_galoes), "reais.")