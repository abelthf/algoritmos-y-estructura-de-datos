# coding: utf-8

"""
Ordene de mayor a menor 3 números ingresados por teclado

Solución:
    definición de variables:
        a,b,c: números que desamos ordenar

Análisis:
    Como se trata de 3 números sabemso que existen 3! = 3 * 2 * 1 = 6
    posibilidades de ordenarlos

    Teniendo en cuenta esto las posibles ocurrencias serán:
        a >= b >= c
        a >= c >= b
        b >= a >= c
        b >= c >= a
        c >= a >= b
        c >= b >= a
"""

a = input("Ingrese número 1: ")
b = input("Ingrese número 2: ")
c = input("Ingrese número 3: ")

print "los números ordenados de mayor a menor son: "

if a >= b and b >= c:
    print "%s, %s, %s" % (a, b, c)
if a >= c and c >= b:
    print "%s, %s, %s" % (a, c, b)
if b >= a and a >= c:
    print "%s, %s, %s" % (b, a, c)
if b >= c and c >= a:
    print "%s, %s, %s" % (b, c, a)
if c >= a and a >= b:
    print "%s, %s, %s" % (c, a, b)
if c >= b and b >= a:
    print "%s, %s, %s" % (c, b, a)
