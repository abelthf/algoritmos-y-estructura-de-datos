# coding: utf-8

"""
Una llamada de un teléfono fijo a otro, también fijo, en HORARIO NROMAL (todos
los días de 7:00 a 22:59 hrs), cuesta sin IGV S/. 0.078, mientras que en
HORARIO REDUCIDO (todos los días de 23:00 a 6:59 hrs), cuesta S/. 0.039.
Calcule el costo total de una llamada telefónica, si considera 1 minuto adicional
de cargo por establecimiento de llamada y solo se considera la hora de incio
para determinar a que tafija se sujeta.

Solución: Definición de variables:
    hora: hora de incio de la llamada
    min: minuto de inicio de la llamada
    inicio: minuto de inicio del día
    dura: duración de la llamada

Análisis:
    El horario normal comienza en el minuto 7 * 60 = 420 del día y terminal en
    el minuto 22 * 60 + 59 = 1379 del día. Toda hora de inicio válida que no
    este en este rango se realiza en horario reducido.

    Por lo tanto, basta con preguntar si la hroa de incio en minutos está dentro
    de ese rango y calcular el costo total de la llamada. Además hay que tener
    en cuenta que el impuesto general a las ventas es de 18%

Pseudocódigo:
    1. Leer: hora, minuto, dura
    2. inicio = hora * 60 + min
    3. si incio > 419 y inicio < 1380:
            costo = (dura + 1) * 0.078
       sino:
            costo = (dura + 1) * 0.039
    4. imprimir: 1.18 * costo
"""


hora = input("ingrese hora de inicio de la llamada : ")
min = input("ingrese minutos de incio de la llamada: ")
dura = input("ingrese duración de la llamada: ")
inicio = hora * 60 + min
if (inicio > 419) and (inicio < 1320):
    costo = (dura+1) * 0.078
else:
    costo = (dura + 1) * 0.039
print "el costo es: %s " % ((1.18 * costo)+costo)
