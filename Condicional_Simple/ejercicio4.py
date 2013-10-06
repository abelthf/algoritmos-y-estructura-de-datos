# coding: utf-8

"""
Un número puede ser menor, igual o mayor que otro. Escriba un algoritmo
que lea 2 números y determine cómo es uno respecto al otro.

Solución:
    definición de variables:
        a, b: números ingresados

Análisis:
    Podemos hacer las comparaciones tal como se muestra en el pseudocodigo


Pseudocódigo:
    1. Leer: a,b
    2. si a == b:
            imprimir: a "es igual a" b
       sino:
           si a > b:
               imprimir: a, "es mayor que" b
           sino:
               imprimir: b "es mayor que" a
"""


a = input("ingrese valor de a: ")
b = input("ingrese valor de b: ")

if a == b:
    print "%s es igual a %s" % (a,b)
else:
    if a > b:
        print "%s es mayor que %s" % (a,b)
    else:
        print "%s es mayor que  %s" % (b,a)
