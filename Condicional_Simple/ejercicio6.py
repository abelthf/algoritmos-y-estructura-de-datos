# coding: utf-8

"""
Encuentre el mayor valor de 3 números dados

Solución:
    Definición de varibles:
        a, b, c: números que deseamos evaluar

Análisis:
    Podemos  ir comparándolos de 2 en 2 tal como se observa en  el código fuente

    Otra forma de evaluar es directamente los 3 posibles casos, tal como
    se muestra  a continuacion:
        si a >= b y a >= c:
            imprimir: el mauor es a
        si b >= a y b >= c:
            imprimir: el mayor es b
        sino:
            imprimir: el mayor es c
"""

a = input("ingrese valor para a: ")
b = input("ingrese valor para b: ")
c = input("ingrese valor para c: ")
if a >= b:
    if a >= c:
        m = a
    else:
        m = c
elif b >= c:
    m = b
else:
    m = c

print "el mayor es %s" % m
