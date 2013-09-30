"""
Se tiene uan lámina rectangular de largo y ancho conocidos
a la que se recorta un cuadrado de lado x en cada esquina
con el objeto de formar una caja.
¿Cuáles son las dimensiones de esta caja,
si se desea que el volumen sea el máximo posible?
calcular máximo volumen de una caja:
    x = ((ancho+largo) - sqrt(pow(ancho,2) - ancho*lafgo + pow(largo,2))/6

definicion de varibales:
    lago: largo de la lámina
    ancho: ancho de la lámina
    x: longitud de lado del cuadrado recortado
    xmax: longitud del lado que hace máximo el volumen
    vol: volumen de la caja
    volmax: volumen máximo de la caja
    0 < x < ancho/2
    x > 0 y x < ancho/2
"""

leer largo, ancho
x = 0
volmax = 0

hacer:
    x = x + 0.0001
    vol = (largo - 2x)(ancho - 2x)x
    si ( vol > volmax):
        volmax = vol
        xmax = x
mientras( x < ancho /2 - 0.0001)

imprimir:
    volumen máximo: volmax
    largo: largo-2xmax
    ancho: ancho-2xmax
    altura: xmax










