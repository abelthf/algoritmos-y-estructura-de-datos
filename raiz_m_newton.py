# coding: utf-8
"""
programa que calcula la raíz de un numero
por el método de newton
"""
import math
# datos de entrada

area = float(input("ingrese el área"))
lado0 = float(input("ingrese el lado"))

while True:
    lado1 = area / lado0
    lado0 = (lado0 + lado1) / 2
    print lado0
    if not math.fabs(lado1 - lado0) == 0.00001:
        break
