import os
os.system('clear')

i = 1
pi4 = 0
signo = -1

while True:
    signo = -signo
    pi4 = pi4 + signo*(1.0/i)
    i = i+2
    if not 1.0/i > 0.000000001:
        break

print "pi vale %s" % (pi4*4)
print"Dante esta conectado"
