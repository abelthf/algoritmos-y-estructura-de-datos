"""
Programa que emula Do While
ingresa una serie de numeros, y cuando es 0 termina, para luego
contar cuanto positivos, negativos, pares, impares existen
"""
# -*- coding: utf-8 -*-


def esNegativo(num):
    if num < 0:
        return True
    else:
        return False


def esPositivo(num):
    if num > 0:
        return True
    else:
        return False


def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


def esImpar(num):
    if num % 2 != 0:
        return True
    else:
        return False
