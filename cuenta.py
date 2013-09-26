"""
Programa que emula Do While
ingresa una serie de numeros, y cuando es 0 termina, para luego
contar cuanto positivos, negativos, pares, impares existen
"""
# -*- coding: utf-8 -*-

#desde carpeta.programa import funcion
from utilitarios.misUtilitarios import esNegativo
from utilitarios.misUtilitarios import esPositivo
from utilitarios.misUtilitarios import esPar
from utilitarios.misUtilitarios import esImpar


cn = 0
cp = 0
cpares = 0
cimpares = 0
while True:
    n = input("ingrese un numero")

    if esNegativo(n):
        cn = cn + 1

    if esPositivo(n):
        cp = cp + 1

    if esPar(n):
        cpares = cpares + 1

    if esImpar(n):
        cimpares = cimpares + 1
    if not n != 0:
        break

print "negativos = %s" % cn
print "positivos = %s" % cp
print "pares = %s" % cpares
print "impares = %s" % cimpares
