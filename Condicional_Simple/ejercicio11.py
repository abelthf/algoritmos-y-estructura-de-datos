# coding: utf-8
"""
Muestre un algoritmo que nos permita evaluar la función:

         |  log(x - 8), si  x > 8
g(x)    <   2x - ln x , si 0 < x <= 8
         |  x + sen x , si x <= 0


Solución:
    Definción de variables
    x: Variable idependiente
    y: Variabel dependeinte

Notamos que g(x) tiene 3 posibles soluciones de acuerdo a cada condición.
entonces se puede apreciar que existen tres condiciones:
    si x > 8, la solución es log(x - 8)
    si x < x <= 8, la solución es 2x - ln x, finalmente
    si x <= 0, la solución es x + sen x

Pseudocódigo:
    1. leer x
    2. si x <= 0:
            y = x + sen x
       sino:
           si x <= 8:
               y = 2x - ln x
           sino:
               y = log(x - 8)
    2 imprimir y

"""

import math
y = 0
x = input("Ingrese el valor para x: ")

if x<=0:
    y = x + math.sin(x)
elif x <= 8:
    # math.log(primer_argumento, segundo_argumento)
    # primer_argumento: el número del cual se desea obtener el logaritmo
    # segundo_argumento: la báse del logaritmo

    y = 2 * x - math.log(x,10)
elif x <= 0:
    y = log(x - 8)

print y
