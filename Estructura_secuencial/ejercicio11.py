# coding: utf-8

import math

a = input("Ingrese lado a: ")
b = input("Ingrese lago b: ")
c = input("Ingrese lago c: ")
p = (a + b + c) / 2
at = math.sqrt(p * (p - a) * (p - b) * (p - c))
print "El área del triángulo es: %s" % at
