#!/usr/bin/env python
# coding:latin-1

from numpy import *
from math import *

#la = float(raw_input("Latitud ="))
#lo = float(raw_input("Longitud="))
# El Puente
#la = 15.109722
#lo = 88.79111
# Ayasta
#la = 13.9313889
#lo = 87.213889
# Hotel Maya Colonial SPS
#la = 15.51
#lo = 88+2/60+10/3600
# OACS
#la = 14.0875
#lo = 87.1595
#elevation = 1077.
# Espresso Americano Minitas
la = 14.+5./60.+41./3600.
lo = 87.+11./60.+30./3600.
elevation = 980.

fout = open("horizonte.csv","w")

#correr = True
# Verifica que las coordenadas estan dentro del rango correspondiente a Honduras
#if la < 13. or la > 15.917:
#    print "Latitud fuera de rango"
#    correr = False

#if lo < 83.0833 or lo > 90.:
#    print "Longitud fuera de rango"
#    correr = False

#if la < 14. and lo < 85.:
#    print "Area fuera de rango"
#    correr = False

#while not correr:
#     raw_input("Presione Ctrl-z para terminar")


# Construye el nombre del archivo correspondiente, segun las coordenadas ingresadas
cla = str(int(la))
clo = str(int(lo+1.))
nomarch = "N"+cla+"W0"+clo+"c.asc"

# Localiza dentro del archivo, la posicion de las coordenadas que se ingresaron
dla = la - int(la)
dlo = lo - int(lo)
fila_la = int((1 - dla) * 1200)
col_lo = int((1 - dlo)*1200)
print "Archivo de la base de datos: ",nomarch

try:
    fhand = open (nomarch)
    print "Coordenadas en la imagen:x=", col_lo, "y=", fila_la
except:
    while True:
        print ""
        print "Area no esta en la base de datos"
        raw_input("Presione Ctrl-z para terminar")
x = []

dhor = 6371000 * acos(6371./(6371.+(elevation/1000.)))
if dhor < 5000.:
        dhor_pix = 180     # dhor_pix = 180 entonces dhor/1000 = 16.2 kms
else:
        dhor_pix = int(dhor/90)
print "Dist. al Horizonte (pix, kms):",dhor_pix, dhor_pix*90/1000

# Define el horizonte ideal a una distancia de dhor_pix cuadros (o sea a dhor/1000 kms de distancia)
fila_0 = fila_la - dhor_pix
fila_f = fila_la + dhor_pix

print "Filas sin corregir: ",fila_0, fila_f
if fila_0 < 0:
    fila_0 = 0
if fila_f > 1200:
    fila_f = 1200
deltaf0 = abs(fila_la - fila_0)
deltaff = abs(fila_f - fila_la)
maxtop = float(deltaf0)
maxbott = float(deltaff)
print "Filas corregidas:", fila_0, fila_f
print "distancias desde el pto de interes al horizonte N y S (mts):", maxtop*90, maxbott*90

col_0 = col_lo - dhor_pix
col_f = col_lo + dhor_pix
print "Columnas sin corregir: ",col_0, col_f
if col_0 < 0:
    col_0 = 0
if col_f > 1200:
    col_f = 1200
deltac0 = abs(col_lo - col_0)
deltacf = abs(col_lo - col_f)
maxder = float(deltacf)
maxizq = float(deltac0)
print "Columnas corregidas:", col_0, col_f
print "Max top=", maxtop, ", Max bottom=", maxbott
print "Max izq=", maxizq, ", Max der=", maxder
print "distancias desde el pto de interes al horizonte E y O (mts):", maxizq*90, maxder*90

esqsupder = atan(maxder/maxtop) * 180./pi
esqinfder = 180. - atan(maxder/maxbott) * 180./pi
esqinfizq = 180. + atan(maxizq/maxbott) * 180./pi
esqsupizq = 360. - atan(maxizq/maxtop) * 180./pi
print "Angulos:"
print "Cuadrante(1): ",esqsupder
print "Cuadrante(2): ",esqinfder
print "Cuadrante(3): ",esqinfizq
print "Cuadrante(4): ",esqsupizq

# Carga de la base de datos las filas y columnas dentro del horizonte que hemos definido en 10.8 kms de distancia
fila_t = 0
for line in fhand:
    fila_t += 1     # Controla el numero de fila con el que actualmente estamos trabajando
    if fila_t >= fila_0 and fila_t <= fila_f:
        i = 1           # Controla el numero secuencial del valor que estamos extrayendo de la fila fila_t
        valor_i = ""    # Con esta variable construimos el valor a adicionar al arreglo de valores de trabajo
        xadd = []        # Es el arreglo de valores de la fila actual que usaremos para calcular el viewshed
        for char in line:  # Empezamos a analizar la fila de caracteres actual
            if char == "," or char == "\n":
                i += 1      # Si encuentra una coma, aumenta el numero del valor en la cadena de valores
                if valor_i <> "":
                    xadd.append(valor_i)  # se agrega el valor al arreglo de valores de la fila actual
                    valor_i = ""          # y se vuelve a dejar vacia la variable para valor para que empiece
                continue                  # a capturar el siguiente valor en la linea (ubicado entre dos comas)
            if i >= col_0 and i <= col_f: # Se construye el valor despues de la coma
                valor_i = valor_i + char
        x.append(xadd)

th = 0
hor = []
print "Altura del sitio origen=", x[deltaf0][deltac0]
raw_input("Presione <Enter> para continuar....")

while th < 360:

#    if th > 135 and th < 140:
#        raw_input("Nueva iteracion, presione <Enter> para continuar....")
    th += 1
    amax = 0
    althor = 0.

    if th > 0 and th <= 90:
        factorx = 1
        factory = 1
    elif th > 90 and th <= 180:
        factorx = 1
        factory = -1
    elif th > 180 and th <= 270:
        factorx = -1
        factory = -1
    elif th > 270 and th <= 360:
        factorx = -1
        factory = 1

    if th > 0 and th <= esqsupder:  # I
        ycmax = maxtop * factory
        xcmax = int(maxtop*abs(tan(th*pi/180.))) * factorx
    if th > esqsupder and th <= 90: # II
        xcmax = maxder * factorx
        ycmax = int(maxder*abs(tan((90.-th)*pi/180.))) * factory
    elif th > 90 and th < esqinfder:  # III
        xcmax = maxder * factorx
        ycmax = int(maxder*abs(tan((th-90.)*pi/180.))) * factory
    elif th >= esqinfder and th <=180:  # IV
        xcmax = int(maxbott*abs(tan((180.-th)*pi/180.))) * factorx
        ycmax = maxbott * factory
    elif th > 180 and th <= esqinfizq:   # V
        xcmax = int(maxbott*abs(tan((th-180.)*pi/180.))) * factorx
        ycmax = maxbott * factory
    elif th > esqinfizq and th <= 270:  # VI
        xcmax = maxizq * factorx
        ycmax = int(maxizq*abs(tan((270.-th)*pi/180.))) * factory
    elif th > 270 and th < esqsupizq:
        xcmax = maxizq * factorx
        ycmax = int(maxizq*abs(tan((th-270.)*pi/180.))) * factory
    elif th >= esqsupizq:                # VIII
        xcmax = int(maxtop*abs(tan((360.-th)*pi/180.))) * factorx
        ycmax = maxtop * factory

    print "Angulo=", th, "XCmax=", xcmax
    xc = 0
    while xc <= abs(xcmax):
        xc += 1
        y0 = int((xc-1)/(abs(tan(th*pi/180)))) * factory
        ym = int((xc-0.5)/(abs(tan(th*pi/180)))) * factory
        y1 = int(xc/(abs(tan(th*pi/180)))) * factory

        if abs(ym) > abs(ycmax):
            ym = abs(ycmax) * factory
        if abs(y1) > abs(ycmax):
            y1 = abs(ycmax) * factory

#        print "y0=", y0, "ym=", ym, "y1=", y1
        i = 0
        while abs(y0+i) <= abs(ym):
            coordx = (xc-1)*factorx + deltac0
            coordy = deltaf0-(y0+i)
#            if th > 130 and th < 145:
#                print xc, y0+i, coordx, coordy, "---> altitud= ", x[coordy][coordx] , "hmax=", amax, "h=", althor
            if coordx > maxder+maxizq or coordx < 0:
                i += factory
                continue
            if coordy > maxtop+maxbott or coordy < 0:
                i += factory
                continue
            althor = 90.*sqrt(((xc-1)*factorx)*((xc-1)*factorx)+(-(y0+i))*(-(y0+i)))

            try:
                if althor <> 0:
                    althor = atan((float(x[coordy][coordx])-float(x[deltaf0][deltac0]))/althor)*180/pi
            except:
                i += 1*factory
                break

            if amax < althor:
                amax = althor
            i += 1*factory

        while abs(y0+i) <= abs(y1):
            coordx = xc*factorx + deltac0
            if coordx > maxder+maxizq or coordx < 0:
                i += factory
                continue
            if coordy > maxtop+maxbott or coordy < 0:
                i += factory
                continue
            althor = 90.*sqrt((xc*factorx)*((xc-1)*factorx)+(-(y0+i))*(-(y0+i)))

            try:
                if althor <> 0:
                    althor = atan((float(x[coordy][xc*factorx + deltac0])-float(x[deltaf0][deltac0]))/althor)*180/pi
            except:
                i += 1*factory
                break

#            if th > 178 and th < 182:
#                print coordx, coordy, "---> altitud= ", x[coordy][xc*factorx +deltac0], "hmax=", amax, "h=", althor
            try:
                if amax < althor:
                    amax = althor
            except:
                print "error"
#                print "i=",i, "xc+deltac0=", xc*factorx + deltac0, amax
            i += 1*factory
    hor.append(amax)

for i in hor:

    var = float(int(i*10.))/10.
#    i += 1
    fout.write(str(var)+",")

fout.close()
