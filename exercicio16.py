	#o programa deve pedir o tamanho em metros quadrados da área a ser pintada;
 	#informar o usuário a quantidade de latas de tinta a serem compradas; e
	#o preço total.
    #variavel2 = 1 lata de tinta = 18litros
    #variavel3 = preço lata = 80 reais
    # area_por_lata = 54 = 18 litros * 3 m²

import math

area_cliente = float(input("Informe a área em metros quadrados que deseja pintar: "))
lata_tinta = 18
custo_lata = 80
area_por_lata = 54

def calcular_latas(area_cliente, area_por_lata):
    qtd_latas = math.ceil(area_cliente / area_por_lata)
    print(qtd_latas)
    return qtd_latas

def calcular_total(qtd_latas, custo_lata):
    custo_total = math.ceil(qtd_latas * custo_lata)
    print(custo_total)
    return custo_total

qtd_latas = calcular_latas(area_cliente, area_por_lata)
custo_total = calcular_total(qtd_latas, custo_lata)

print("Você deverá comprar", str(qtd_latas), " latas. O preço total é de R$", str(custo_total))