#!/usr/bin/env python
# coding:latin-1

la = float(raw_input("Latitud ="))
lo = float(raw_input("Longitud="))
correr = True
# Verifica que las coordenadas estan dentro del rango correspondiente a Honduras
#if la < 13. or la > 15.917:
#    print "Latitud fuera de rango"
#    correr = False

#if lo < 83.0833 or lo >= 90.:
#    print "Longitud fuera de rango"
#    correr = False

#if la < 14. and lo < 85.:
#    print "Area fuera de rango"
#    correr = False

#while not correr:
#    raw_input("Presione Ctrl-z para terminar")

# Construye el nombre del archivo correspondiente, segun las coordenadas ingresadas
cla = str(int(la))
clo = str(int(lo+1.))
nomarch = "N"+cla+"W0"+clo+".asc"
nomarchc = "N"+cla+"W0"+clo+"c.asc"

fout = open(nomarchc,"w")
fhand = open(nomarch)
x = []
fila_t = 0
for line in fhand:
    fila_t += 1     # Controla el numero de fila con el que actualmente estamos trabajando
    i = 1
    valor_i = ""
    xadd = []
    for char in line: # Empieza a leer la linea caracter por caracter
        if char == "," or char == "\n":    # Si llega al final de la linea o hay coma...
            i += 1
            if valor_i <> "":
                xadd.append(valor_i)       # ...agrega un dato al listado de datos de la linea actual y vuelve a poner
                valor_i = ""               # en "0" el valor de la variable con que se construye el valor que se lee
            continue
        valor_i = valor_i + char           # Si no se ha llegado al final de la linea, se agrega un digito a la variable
    j = 0                                  # de lectura
    k = 1.
    pendiente = 0.
    ult = 0
    l = 0
    m = 0.
#    print xadd
#    print "i=", i
    while j < i-1:         # Empezamos a analizar valor por valor por si no es un numero que se sale de lo esperado
#        print xadd[j], i, j, k, l, ult, m, pendiente
#        raw_input("Presione <Enter> para siguiente iteracion")
        if int(xadd[j]) > 5000: # Si el valor de altura esta fuera de rango, inicia el conteo de valores erroneos
#            print "xadd[",j,"]=",int(xadd[j])
            k += 1.
            j += 1
            continue
        if k <> 1.:
            pendiente = (float(xadd[j]) - m) / k  # Calcula el valor promedio de variacion entre variables correctas
            l = ult + 1
            while l < k + ult:
                xadd[l] = m + (l - ult) * pendiente  # Ajusta las variables fuera de rango a lo esperado
                l += 1
            k = 1.
        else:             # Si no hay valores fuera de rango, guarda la var anterior para hacer la comparacion
            m = float(xadd[j])   # Guarda la variable anterior
            ult = j       # Guarda su posicion en la lista de valores de la linea actual
        j += 1

    i = 0
    rowdump = ""
#    print xadd

    while i < len(xadd):
        if i > 0:
            rowdump = rowdump + ","
        rowdump = rowdump + str(int(xadd[i]))
        i += 1

    fout.write("%s\n" % rowdump)

fout.close()
