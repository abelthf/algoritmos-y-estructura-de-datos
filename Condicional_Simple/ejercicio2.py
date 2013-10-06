# coding: utf-8

"""
Una llamada telefónica en cualquier teléfono público cuesta S/. 0.5 por los
primeros 3 minutos o menos. cada minuto adicional es un caso de contador y
cuesta S/. 0.1. Calcule el monto de una llamada cualquiera.

Solución:
    Definición de variables:
        duración: duración de la llamada
        costo: costo total de la llamada

Análisis:

Si la duración de la llamada es menor a 3 minutos entonces la llamada cuesta
0.5, mientas que si excede los 3 minutos costará 0.5 por los primeros tres
minutos y 0.1 por los (duración - 3) minutos adicionales

Pseudocódigo:
    1. leer: duración
    2. si duración <= 3
            costo = 0.5
       sino:
            costo = 0.5 + 0.1 * (duración - 3)
    3. imprimir: costo
"""

duracion = input("ingrese minutos de duración: ")
if duracion <= 3:
    costo = 0.5
else:
    costo = 0.5 + 0.1 * (duracion - 3)
print "el costo de la llamada será: %s" % costo

