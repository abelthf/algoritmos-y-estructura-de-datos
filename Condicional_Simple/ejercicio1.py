# coding: utf-8

"""
Elabore un algoritmo que resuleva una ecuación de primer grado.

Solución:
    Definición de variables
    a:  coeficiente de x. debe ser diferente de 0.
    b: término independiente

    La solución es bastante simple, una ecuación de primer grado es de la forma
    ax + b = 0, de donde despejando x tendremos
    x = -b / a, debiendo considerar que para que exista solución a != de 0 (a
    es diferente de o)

Pseudocódigo:
    1. leer a, b
    2. si a == 0:
            imprimir: "no es de primer grado
       sino:
           x = -b / a
           imprimir: x
"""
x = 0
a = input("Coeficiente de x: ")
b = input("término independiente: ")

if a==0:
    print "no es una ecuación de primer grado"
else:
    x = -b / a
    print "la raiz es: %s " % x
