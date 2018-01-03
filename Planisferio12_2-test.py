#!/usr/bin/env python
# coding:latin-1

from ephem import *
import time
from datetime import datetime
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
matplotlib.use('TkAgg')
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

global_lugar = Observer()
global_flag_lugar_defecto = 1
global_flag_fecha_defecto = 1

# Coordenadas del observador
# El Puente
#global_lugar.lat = '15.109722'
#global_lugar.long = '-88.79111'
#global_lugar.date = '781/2/8'
#global_lugar.elevation = 478.
#global_alt = '6'

# OACS - UNAH
global_lugar.lat = '14.0875'
global_lugar.long = '-87.1595'
global_lugar.date = '2017/6/28'
global_lugar.elevation = 1077.
global_alt = '8.'

# Yarumela
#global_lugar.lat = '14.3637'
#global_lugar.long = '-87.65'
#global_lugar.date = '2016/1/1'
#global_lugar.elevation = 600.
#global_alt = '8.'

# La Rueda - Las Sabanas/El Castillito - Nicaragua
#global_lugar.lat = '13.350265'
#global_lugar.long = '-86.612964'
#global_lugar.date = '2016/11/1'
#global_lugar.elevation = 1280.
#global_alt = '10.'

# Mayapan
#global_lugar.lat = '20.628889'
#global_lugar.long = '-89.460833'
#global_lugar.date = '950/9/20'
#global_alt = '0'

# Cuevas de Ayasta
#global_lugar.lat = '13.931388889'
#global_lugar.long = '-87.2138889'
#global_lugar.date = '1750/6/20'
#global_alt = '0'

# El Zapotal
#global_lugar.lat = '14:28:05'
#global_lugar.long = '-87:37:29'
#global_lugar.date = '1983/12/20'
#global_lugar.elevation = 670.
#global_alt = '6'

global_lugar.epoch = global_lugar.date
fout = open("output.txt","w")
fout.write("   Fecha          omega         Declinacion       Tipo de            z                 z\n")
fout.write("                                   lunar        parada lunar      salida            puesta\n")
fout2 = open ("Venus.txt", "w")
fout2.write("Maximo Orto Norte              Maximo orto Sur            Maximo ocaso norte         Maximo ocaso Sur\n")

global f, a, aci, fig2, ax2, canvas2

plt.ion()    # Para poder hacer interactivas las graficas que se generen mas adelante en la funcion graficar()
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)

class Chanubih:

    def __init__(self, parent,ancho_p, alto_p):

        global aci, fig2, ax2, canvas2

        def evaluar_e(event):
            global_lugar.date = ent1_fecha.get()+" "   #+ent2_fecha.get()
            print "Fecha de trabajo:",global_lugar.date

        def evaluar():
            global_lugar.date = ent1_fecha.get()+" "   #+ent2_fecha.get()
            print "Fecha de trabajo:",global_lugar.date

        def evaluarl_e(event):
            global_lugar.lat = ent1_lugar.get()
            global_lugar.long = ent2_lugar.get()
            global_lugar.elevation = float(ent3_lugar.get())
            print "Datos de trabajo:\nLatitud",global_lugar.lat,"\nLongitud:",global_lugar.long,"\nAltura (msnm):",global_lugar.elevation

        def evaluarl():
            global_lugar.lat = ent1_lugar.get()
            global_lugar.long = ent2_lugar.get()
            global_lugar.elevation = float(ent3_lugar.get())
            print "Datos de trabajo:\nLatitud",global_lugar.lat,"\nLongitud:",global_lugar.long,"\nAltura (msnm):",global_lugar.elevation

        def evaluarA():
            global aci
            aci = float(ent1_alinmto.get())
            print "Acimut de trabajo: ", aci

        def evaluarA_e(event):
            global aci
            aci = float(ent1_alinmto.get())
            print "Acimut de trabajo: ", aci

        self.myparent = parent

        self.ventana = Frame(parent)                            # Crea la ventana de Chan U'Bih
        self.ventana.pack()

        alt_centro = 550
        ancho_centro = 1350
        aci = 0.
        # Crea las cavidades dentro de la pantalla de Chan U'Bih
        self.creditos = Frame(self.ventana, borderwidth = 2, height = 60, width = ancho_centro, relief = RIDGE)
        self.centro = Frame(self.ventana, borderwidth = 2, height = alt_centro, width = ancho_centro, relief = RIDGE)
        self.aceptar = Frame(self.ventana, borderwidth = 2, height = 30, width = ancho_centro, relief = RIDGE)

        # Crea las cavidades dentro de la cavidad central
        self.centro_izq = Frame(self.centro,borderwidth = 2, height = alt_centro, width = ancho_centro/2, relief = RIDGE)
        self.centro_der = Frame(self.centro,borderwidth = 2, height = alt_centro, width = ancho_centro/2, relief = RIDGE)

        # Definiendo los colores de las cavidades
        color_fecha = "#90A4AE"
        color_fecha_label = "#78909C" #"#797589"
        color_lugar = "#90A4AE"
        color_lugar_label = "#78909C" #"#758589"
        color_astro = "#78909C" #"#758983"
        color_astro_label = "#78909C" #"#758983"
        color_otrosf = "#78909C"
        color_otrosf_label = "#78909C" #"#757B89"

        # Crea las cavidades dentro de las cavidad izquierda
        self.fecha = Frame(self.centro_izq, borderwidth = 5, height=alt_centro/4, width = ancho_centro/4, background = color_fecha, relief = RIDGE)
        self.lugar = Frame(self.centro_izq, borderwidth = 5, height=alt_centro/4+2, width = ancho_centro/4, background = color_lugar, relief = RIDGE)
        self.alinmto = Frame(self.centro_izq, borderwidth = 5, height = alt_centro/4, width = ancho_centro/4, background = color_lugar, relief = RIDGE)
        self.astro = Frame(self.centro_izq, borderwidth = 5, height = alt_centro/4, width = ancho_centro/4, background = color_astro, relief = RIDGE)
        self.otrosf = Frame(self.centro_izq, borderwidth = 5, height = alt_centro/4, width = ancho_centro/4, background = color_otrosf, relief = RIDGE)
        self.results = Frame(self.centro_izq, borderwidth = 5, height = alt_centro/8, width = ancho_centro/4, background = color_otrosf, relief = RIDGE)

        # Crea la cavidad derecha, para que albergue el grafico y le hace la plantilla del gráfico y prepara sus propiedades
        self.grafico = Frame(self.centro_der, height = alt_centro, width = ancho_centro/2, background="white", relief = RIDGE)

        fig = Figure(figsize=(8.6,6.6))
        ax = fig.add_subplot(111)
        fig.tight_layout()
        ax.set_xlim(0.,1.)
        ax.set_ylim(0.,1.)
        ax.set_axis_off()

        fig2 = Figure(figsize=(4.1,0.9))
        ax2 = fig2.add_subplot(111)
        fig2.tight_layout()
        ax2.set_xlim(0.,0.5)
        ax2.set_ylim(0.,0.1)
        ax2.set_axis_off()

        canvas = FigureCanvasTkAgg(fig, master=self.grafico)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        canvas2 = FigureCanvasTkAgg(fig2, master=self.results)
        canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, self.grafico)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        canvas2._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        # Vuelve visibles las diferentes cavidades dentro de Chan U'Bih
        self.creditos.pack(side=TOP,expand=YES)
        self.centro.pack(expand=YES, fill=BOTH)
        self.aceptar.pack(expand=YES, fill=BOTH)

        self.centro_der.pack(side=RIGHT, expand=YES)
        self.centro_izq.pack(side=TOP, expand=YES)
        self.fecha.pack(side = TOP, expand=YES, fill = BOTH)
        self.lugar.pack(expand = YES, fill = BOTH)
        self.alinmto.pack(expand=YES, fill = BOTH)

        self.otrosf.pack(expand = YES)
        self.astro.pack(expand = YES)
        self.results.pack(expand = YES)
        self.grafico.pack(side=TOP,expand=YES)

        # Establecemos ahora las especificaciones para cada una de las cavidades de trabajo creadas
        # Etiqueta del titulo de la ventana
        row_cred = Frame(self.creditos)
        lab_cred = Label(row_cred, width = 126, text=u"Software para Arqueoastronom\u00EDa")
        lab_cred.pack(side = TOP)
        lab2_cred = Label(row_cred, width = 126, text=u'Cr\u00E9ditos: (\u037B) 2017 Eduardo Rodas')
        lab2_cred.pack()
        row_cred.pack(side=TOP, fill=X, padx=5, pady=5)

        # Obteniendo las fechas

        row1_fecha = Frame(self.fecha, relief = RIDGE, borderwidth = 2) # Encabezado del recuadro para captura de fechas
        row2_fecha = Frame(self.fecha, highlightthickness = 0)
#        row3_fecha = Frame(self.fecha, highlightthickness = 0)
        row4_fecha = Frame(self.fecha, highlightthickness = 0)
        row5_fecha = Frame(self.fecha, highlightthickness = 0)
        row6_fecha = Button(self.fecha, text = "Confirmar datos",command = evaluar, background="#B0BEC5")
        row6_fecha.bind("<Return>", evaluar_e)

        lab1_fecha = Label(row1_fecha, width=40, text="FECHA", background = color_fecha_label)
        lab2_fecha = Label(row2_fecha, width=19, text="Fecha (aaaa/mm/dd):", background = color_fecha)
        ent1_fecha = Entry(row2_fecha, background = "white")
        ent1_fecha.bind=("<Return>", evaluar_e)
#        lab3_fecha = Label(row3_fecha, width=39, text="     Formato: aaaa/mm/dd", background = color_fecha)
#        lab4_fecha = Label(row4_fecha, width=19, text="Hora (hh:mm:ss):", background = color_fecha)
#        ent2_fecha = Entry(row4_fecha, background = "white")
#        ent2_fecha.bind=("<Return>",evaluar_e)
        lab5_fecha = Label(row5_fecha, width=39, text=" ", background = color_fecha)
        fechayhora = str(date(global_lugar.date))
        pos_espacio = fechayhora.find(" ")
        fecha = fechayhora[:pos_espacio]
        hora = fechayhora[pos_espacio+1:]
        ent1_fecha.insert(0,fecha)
#        ent2_fecha.insert(0,hora)

        row1_fecha.pack(side=TOP, fill=BOTH)
        row2_fecha.pack(side=TOP, fill=BOTH)
#        row3_fecha.pack(side=TOP, fill=BOTH)
#        row4_fecha.pack(side=TOP, fill=BOTH)
        row5_fecha.pack(side=TOP, fill=BOTH)
        row6_fecha.pack(side=TOP)

        lab1_fecha.pack(side=TOP, fill=BOTH, expand=YES)
        lab2_fecha.pack(side=LEFT, fill=BOTH, expand=YES)
#        lab3_fecha.pack(side=LEFT, fill=BOTH, expand=YES)
#        lab4_fecha.pack(side=LEFT, fill=BOTH, expand=YES)
        lab5_fecha.pack(side=LEFT, fill=BOTH, expand=YES)
        ent1_fecha.pack(side=LEFT, expand=YES)
#        ent2_fecha.pack(side=LEFT, expand=YES)

        # Obteniendo los datos del sitio
        row1_lugar = Frame(self.lugar, borderwidth = 2, relief = RIDGE)   # Encabezado del recuadro para captura de fechas
        row2_lugar = Frame(self.lugar, highlightthickness = 0)
#        row3_lugar = Frame(self.lugar, highlightthickness = 0)
        row4_lugar = Frame(self.lugar, highlightthickness = 0)
#        row5_lugar = Frame(self.lugar, highlightthickness = 0)
        row6_lugar = Frame(self.lugar, highlightthickness = 0)
        row7_lugar = Frame(self.lugar, highlightthickness = 0, background = color_fecha)
        row8_lugar = Button(self.lugar, text = "Confirmar datos", command = evaluarl, background="#B0BEC5")

        lab1_lugar = Label(row1_lugar, width=39, text=u"UBICACI\u00D3N", background = color_lugar_label)
        lab2_lugar = Label(row2_lugar, width=19, text=u"Latitud (\u00B1gg:mm:ss):", background = color_lugar)
        ent1_lugar = Entry(row2_lugar, background = "white")
        ent1_lugar.bind=('<Return>',evaluarl)
#        lab3_lugar = Label(row3_lugar, width=40, text=u"     Formato: \u00B1gg:mm:ss", background = color_lugar)
        lab4_lugar = Label(row4_lugar, width=19, text=u"Longitud: (\u00B1ggg:mm:ss)", background = color_lugar)
        ent2_lugar = Entry(row4_lugar, background = "white")
        ent2_lugar.bind=('<Return>',evaluarl)
#        lab5_lugar = Label(row5_lugar, width=40, text=u"    Formato: \u00B1ggg:mm:ss", background = color_lugar)
        lab6_lugar = Label(row6_lugar, width=19, text=u"Elevaci\u00F3n (msnm):", background = color_lugar)
        ent3_lugar = Entry(row6_lugar, background = "white")
        ent3_lugar.bind=('<Return>',evaluarl)
        lab7_lugar = Label(row7_lugar, width=19, text=" ", background = color_lugar)

        ent1_lugar.insert(0,str(global_lugar.lat))
        ent2_lugar.insert(0,str(global_lugar.long))
        ent3_lugar.insert(0,float(global_lugar.elevation))

        row1_lugar.pack(side=TOP, fill=BOTH)
        row2_lugar.pack(side=TOP, fill=BOTH)
#        row3_lugar.pack(side=TOP, fill=BOTH)
        row4_lugar.pack(side=TOP, fill=BOTH)
#        row5_lugar.pack(side=TOP, fill=BOTH)
        row6_lugar.pack(side=TOP, fill=BOTH)
        row7_lugar.pack(side=TOP, fill=BOTH, expand = YES)
        row8_lugar.pack(side=TOP)
        lab1_lugar.pack(side=TOP, fill=BOTH, expand=YES)
        lab2_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
#        lab3_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
        lab4_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
#        lab5_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
        lab6_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
        lab7_lugar.pack(side=LEFT, fill=BOTH, expand=YES)
        ent1_lugar.pack(side=LEFT, expand=YES)
        ent2_lugar.pack(side=LEFT, expand=YES)
        ent3_lugar.pack(side=LEFT, expand=YES)

        #Obteniendo el acimut de la estructura arqueológica
        row1_alinmto = Frame(self.alinmto, borderwidth = 2, relief = RIDGE)   # Encabezado del recuadro para captura de acimut del alineamiento
        row2_alinmto = Frame(self.alinmto, highlightthickness = 0)
        row3_alinmto = Frame(self.alinmto, highlightthickness = 0)
        row4_alinmto = Button(self.alinmto, text = "Confirmar datos", command = evaluarA, background="#B0BEC5")
        row4_alinmto.bind=('<Return>',evaluarA_e)

        lab1_alinmto = Label(row1_alinmto, width=39, text=u"ALINEACI\u00D3N A EVALUAR", background = color_lugar_label)
        lab2_alinmto = Label(row2_alinmto, width=19, text=u"Acimut (\u00B1gg.xx):", background = color_lugar)
        ent1_alinmto = Entry(row2_alinmto, background = "white")
        lab3_alinmto = Label(row3_alinmto, width=19, text=" ", background = color_lugar)
        ent1_alinmto.insert(0,aci)

        row1_alinmto.pack(side=TOP, fill=BOTH)
        row2_alinmto.pack(side=TOP, fill=BOTH)
        row3_alinmto.pack(side=TOP, fill=BOTH)
        row4_alinmto.pack(side=TOP)

        lab1_alinmto.pack(side=TOP, fill=BOTH, expand=YES)
        lab2_alinmto.pack(side=LEFT, fill=BOTH, expand=YES)
        lab3_alinmto.pack(side=LEFT, fill=BOTH, expand=YES)
        ent1_alinmto.pack(side=LEFT, expand=YES)

        # Seleccionando cual cuerpo celeste graficar
        self.foto_sol = PhotoImage(file = "kin_ico.png")
        self.foto_luna = PhotoImage(file = "Yueliang_ico.png")
        self.foto_venus = PhotoImage(file = "Tanit_ico.png")
        row1_astro = Frame(self.astro, relief = RIDGE, borderwidth = 2)   # Encabezado del recuadro para seleccion del cuerpo celeste
        row2_astro = Button(self.astro, command = lambda arg1="Sol": self.graficar(arg1, fig, ax, canvas))
        row2_astro.configure (text = " Graficar Sol ", image  = self.foto_sol, width = 104, background="#90A4AE")
        row3_astro = Button(self.astro, command = lambda arg1="Luna": self.graficar(arg1, fig, ax, canvas))
        row3_astro.configure (text = "Graficar Luna", image  = self.foto_luna, width = 104, background="#90A4AE")
        row4_astro = Button(self.astro, command = lambda arg1="Venus": self.graficar(arg1, fig, ax, canvas))
        row4_astro.configure (text = "Graficar Venus", image  = self.foto_venus, width = 104, background="#90A4AE")

        lab1_astro = Label(row1_astro, width=40, text="SELECCIONE UN CUERPO CELESTE A GRAFICAR", background = color_astro_label)

        row1_astro.pack(side=TOP, fill=BOTH)
        row2_astro.pack(side=LEFT)
        row2_astro.bind("<Return>", lambda event_arg, arg1="Sol": self.graficar_a(event_arg, arg1, fig, ax, canvas, aci))
        row3_astro.pack(side=LEFT)
        row3_astro.bind("<Return>", lambda event_arg, arg1="Luna": self.graficar_a(event_arg, arg1, fig, ax, canvas, aci))
        row4_astro.pack(side=LEFT)
        row4_astro.bind("<Return>", lambda event_arg, arg1="Venus": self.graficar_a(event_arg, arg1, fig, ax, canvas, aci))

        lab1_astro.pack(side=TOP, fill=BOTH, expand=YES)

        # Seleccionando calculo de otros fenomenos celestes
        row1_otrosf = Frame(self.otrosf, relief = RIDGE, borderwidth = 2)   # Encabezado del recuadro para seleccion del cuerpo celeste
        row2_otrosf = Button(self.otrosf, command = self.coincidir_sol)
        row2_otrosf.configure (text = "Coincidencia\nSol-Acimut", background="#90A4AE", width = 8)
        row3_otrosf = Button(self.otrosf, command = self.decsluna)
        row3_otrosf.configure (text = "Paradas\nlunares", background="#90A4AE", width = 6)
        row4_otrosf = Button(self.otrosf, command = self.decsvenus)
        row4_otrosf.configure (text = "Max/Min\ndec.Venus", background="#90A4AE", width = 6)
        row5_otrosf = Button(self.otrosf, command = self.pstz)
        row5_otrosf.configure (text = "Paso del Sol\npor el Cenit", background="#90A4AE", width = 7)

        lab1_otrosf = Label(row1_otrosf, width=40, text=u"CALCULAR EVENTOS \nTOPOC\u00C9NTRICOS", background = color_otrosf_label)

        row1_otrosf.pack(side=TOP, fill=BOTH)
        row2_otrosf.pack(side=LEFT)
        row2_otrosf.bind("<Return>", self.coincidir_sol)
        row3_otrosf.pack(side=LEFT)
        row3_otrosf.bind("<Return>", self.decsluna)
        row4_otrosf.pack(side=LEFT)
        row4_otrosf.bind("<Return>", self.decsvenus)
        row5_otrosf.pack(side=LEFT)
        row5_otrosf.bind("<Return>", self.pstz)

        lab1_otrosf.pack(side=TOP, fill=BOTH, expand=YES)


        # Boton de terminacion del software
        self.boton_2 = Button(self.aceptar, command = self.salida, text="Salir", background = "#D46A6A", width = 15)
        self.boton_2.pack(side = RIGHT)
        self.boton_2.bind("Return", self.salida)

    def salida(self):
        self.myparent.destroy()

    def mensaje(self, fig2, ax2, canvas2, *args):

        ax2.clear()
        ax2.set_axis_off()
        alin_hor = ['center','center']
        alin_ver = ['bottom', 'top']

                ################ ESCRIBE EL TEXTO SEGUN LOS PARAMETROS QUE SE HAN PASADO #######################

        i = 0
        for arg in args:
            ax2.text(-0.12,2.0-(0.47*float(i)), arg,
                horizontalalignment='left',
                verticalalignment='top',
                fontsize=8.5, color='black',
                transform=ax2.transAxes)
            i += 1

        canvas2.draw()

    def v_aviso(self, fields, titulo):

        def salir():
            aviso.destroy()    # Este comando destruye la ventana
            aviso.quit()       # Este comando devuelve el control o flujo del programa a la rutina que llamó a v_aviso

        def salir_a(event):
            salir()
                    
        def makeform(aviso, fields, ancho): ## Esta funcion solo es para uso dentro de v_aviso()
            entries = ""         ## y da forma al widget para capturar el dato requerido                
            row = Frame(aviso)
            # Evalua el texto de fields para ver si abarca mas de 1 renglon
            lab = Label(row, width = ancho, text=fields)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            return

        aviso = Tk()
        i = fields.find("\n")
        if i == 0:
            ancho = len(fields)
        else:
            ancho = i
        ents = makeform(aviso, fields, ancho)
        screen_width=aviso.winfo_screenwidth()
        screen_height=aviso.winfo_screenheight()

        print "datos de pantalla", int((screen_width - ancho * 5 - 10*5) / 2)
        aviso_xpos = int((screen_width - ancho * 5 - 10*5) / 2)
        aviso_ypos = int((screen_height * 0.5))
        aviso.title(titulo)
        avisoWindowPosition="+" + str(aviso_xpos) + "+" + str(aviso_ypos)
        aviso.geometry(avisoWindowPosition)

        txt_button = "Aceptar"
        b1 = Button(aviso, text=txt_button, command = salir)
        b1.bind('<Return>', (lambda event, ents: salir))
        b1.pack(side = TOP, padx = 5, pady = 5)
        b1.focus_force()

        aviso.mainloop()

    def JDEtoCAL(self,JDE,frac):  # Rutina para obtener la fecha en calendario gregoriano a partir de dias julianos
        JDE += 0.5
        Z = int(JDE)
        F = JDE - Z
        if Z < 2299161:
            A = Z
        else:
            alfa = int((Z - 1867216.25)/36524.25)
            A = Z + 1 + alfa - int(alfa/4)
        B = A + 1524
        C = int((B - 122.1) / 365.25)
        D = int(365.25 * C)
        E = int((B - D)/ 30.6001)
        dia = B - D - int(30.6001 * E) + F
        diae = int(dia)
        hora = float(int((dia - diae) * 240))/10
        if E < 14:
            mes = E - 1
        else:
            mes = E - 13
        if mes > 2:
            anio = C - 4716
        else:
            anio = C - 4715
        if dia < 10:
            diae = "0" + str(diae)
        else:
            diae = str(diae)
        if frac == 0:
            fecha = str(anio) + "/" + str(mes) + "/" + diae + " "
        else:
            fecha = str(anio) + "/" + str(mes) + "/" + str(dia) + " "
        return fecha

    def coincidir_sol(self): # Rutina para calcular fechas en las que Sol pasa x acimut a evaluar (si realmente ocurre)

        global fig2, ax2, canvas2
        fields = "Altura del horizonte en ese punto"

        def salir():
            obtalt.destroy()

        def retornar(alt):
            global aci, global_alt      #, global_lugar
            bandera = True
########################################################
            global_alt = float(alt.get())    ##### INGRESA ALTURA DEL HORIZONTE EN EL ACIMUT A EVALUAR
#            s = Sun()
#            o = Observer()
#            o = global_lugar
#            s.compute(o)
#            iazsol = s.az * 180/np.pi   # Toma el dato del acimut del orto solar
#            deltaz = horizonte[int(iazsol)]/tan(np.pi/2 - o.lat)
#            while deltaz > 1.0:
#                if  o.lat >= 0.:
#                    iazsol2 = iazsol + 0.5*deltaz
#                else:
#                    iazsol2 = iazsol - 0.5*deltaz
#                o.horizon = horizonte[int(iazsol2)]*np.pi/180. # Encuentra para ese acimut cuan alto es el horizonte y lo incorpora a los calculos
#                s.compute(o) # calcula datos lunares nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
#                try:
#                    o.date = s.rise_time
#                except:
#                    o.date = o.date - 24*hour
#                    s.compute(o)
#                    o.date = s.rise_time
#                s.compute(o)
#                iazsol = s.az * 180/np.pi
#                deltaz = s.az*180/np.pi - iazsol2
#            global_alt = float(o.horizon)
#######################################
            print " "
            print "Altura ingresada: ",global_alt  
            print "Buscando coincidencias entre el Acimut ingresado y posición del Sol"
            print "Calculando..."
############ EVALUA SI ES POSIBLE UNA ALINEACION ENTRE ACIMUT DE ESTRUCTURA Y SALIDA DEL SOL EN ESE LUGAR ##############

############# CALCULA LA OBLICUEDAD DE LA ECLIPTICA EN LA EPOCA CORRESPONDIENTE A LA FECHA ACTUAL 
            JDE = julian_date(str(global_lugar.date))
            Tcalc = (JDE - 2451545.) / 36525.
            epsilon_0 = 23.439291111 + (-46.815 *Tcalc - 0.00059 *Tcalc*Tcalc + 0.001813 *Tcalc*Tcalc*Tcalc)/3600.

############# EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE VERANO SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA ÉPOCA DE LA FECHA) ###############
            min_acimut_solar1 = sin(epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
            min_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
            try:
                min_acimut_solar = acos(min_acimut_solar1 / min_acimut_solar2) * 180. / pi
            except:
                min_acimut_solar = 0.
                self.v_aviso(u"No se puede calcular el m\u00EDnimo acimut solar", u"\u00A1AVISO!")

############# AHORA EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE INVIERNO EN SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA EPOCA DE LA FECHA) ########
            max_acimut_solar1 = sin(-epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
            max_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
            try:
                max_acimut_solar = acos(max_acimut_solar1 / max_acimut_solar2) * 180. / pi
            except:
                max_acimut_solar = 180.
                self.v_aviso(u"No se puede calcular el m\u00E1ximo acimut solar", u"\u00A1AVISO!")

############# ENCUENTRA CUAL ES EL ACIMUT DEL SOLSTICIO MAS CERCANO A LA ALINEACION INGRESADA #########################
###### Y EVALUA SI ESTA SE ENCUENTRA DENTRO DEL RANGO DE POSIBLES ALINEACIONES CON EL SOL EN SITIO DE OBSERVACION #####
            if aci > 180.:
                temporal = min_acimut_solar
                min_acimut_solar = 360.0 - max_acimut_solar
                max_acimut_solar = 360.0 - temporal

           #######   ESTO SOLO ES PARA PROPOSITOS DE CONTROL ###################
            if abs(aci-min_acimut_solar) < abs(aci-max_acimut_solar):
                print u"Acimut m\u00EDnimo que puede tener el Sol a esa altura=", min_acimut_solar
                print u"Acimut m\u00E1ximo que puede tener el Sol a esa altura=", max_acimut_solar
            ####################################################################

            if aci < min_acimut_solar:
                self.v_aviso(u"A este acimut no puede existir coincidencia entre\nalineaci\u00F3n de estructura y salida/puesta del Sol", u"\u00A1ERROR!")
                bandera = False
            if aci > max_acimut_solar:
                self.v_aviso(u"A este acimut no puede existir coincidencia entre\nalineaci\u00F3n de estructura y salida/puesta del Sol", u"\u00A1ERROR!")
                bandera = False

########################################################################################################################
########## CALCULA LA DECLINACION QUE TENDRIA EL SOL SI ESTUVIERA ALINEADO CON LA ESTRUCTURA (EPOCA J2000.0)############
########################################################################################################################
            if bandera:
                dec_solar = sin(global_lugar.lat) * sin(global_alt*np.pi/180.)
                dec_solar = dec_solar + cos(global_lugar.lat) * cos(global_alt*np.pi/180.)*cos(aci*np.pi/180.)
                dec_solar = asin(dec_solar) * 180. / np.pi
                if dec_solar >= 0:
                    signo_dec = "+"
                else:
                    signo_dec = "-"
                    dec_solar = dec_solar * -1.
                dec_solarg = int(dec_solar)
                dec_solarm = int((dec_solar-dec_solarg)*60.)
                dec_solars = ((dec_solar-dec_solarg)*60.-dec_solarm)*60.
                dec_solar = str(dec_solarg)+':'+str(dec_solarm)+':'+str(int(dec_solars*10.)/10.)
                print "Declinación del Sol:", dec_solar

########### ENCUENTRA LAS FECHAS EN QUE EL SOL ALCANZA EL ACIMUT A EVALUAR, HALLANDO LA DIFERENCIA ENTRE ############
############# ACIMUT EVALUADO Y ACIMUT DEL SOL, CUANDO ESTA DIFERENCIA ES MINIMA, OCURRE COINCIDENCIA ###############

                s = Sun()
                o = Observer()
                o.date = global_lugar.date
                o.lat = global_lugar.lat
                o.long = global_lugar.long
                o.elevation = global_lugar.elevation
                o.horizon = str(global_alt)
                o.date = previous_solstice(o.date)
                s.compute(o)
                if aci < 180.:
                    o.date=str(s.rise_time)
                else:
                    o.date =str(s.set_time)
                s.compute(o)

                diferencia = abs(float(s.az)*180/np.pi - aci)
                i = 0
                while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    o.date = o.date + (24*hour)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date = str(s.set_time)
                    s.compute(o)
                    i += 1
                o.date = o.date - 24*hour  # Primera fecha encontrada en que el Sol pasa por ese acimut
                d1 = o.date
                print "Intentos:",i, "; ",o.date
                print " "

                o.date = next_solstice(o.date)
                s.compute(o)
                if aci < 180.:
                    o.date=str(s.rise_time)
                else:
                    o.date =str(s.set_time)
                s.compute(o)

                diferencia = abs(float(s.az)*180/np.pi - aci)
                i = 0
                while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    o.date = o.date + (24*hour)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date = str(s.set_time)
                    s.compute(o)
                    i += 1
                o.date = o.date - 24*hour  # Segunda fecha encontrada en que el Sol pasa por ese acimut
                d2 = o.date
                print "Intentos:",i, "; ",o.date

                print d1, "  ", d2

                msj0 = "COINCIDENCIA SOL - ACIMUT"
                m1_1 = str(float(int(aci*10.))/10.)
                msj1 = u"Declinaci\u00F3n del Sol en el Acimut " + m1_1 + " : " + dec_solar
                msj2 = "Fechas de paso del Sol por este acimut, para la latitud "+str(o.lat)
                msj3 = " "
                msj4 = d1
                msj5 = 'o'
                msj6 = d2
                self.mensaje(fig2, ax2, canvas2, msj0, msj2, msj3, msj4, msj5, msj6)

            salir()

        def makeform(obtalt, fields, wwidth): ## Esta funcion solo es para uso dentro de coincidir_sol()
            global aci, global_alt
            entries = ""            ## y da forma al widget para capturar el dato requerido
            row = Frame(obtalt)
            lab = Label(row, width=wwidth, text=fields, anchor='w')
            ent = Entry(row)
            ent.insert(0,str(global_alt))
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            return ent

        obtalt=Tk()
        wwidth = 26
        ents=makeform(obtalt,fields, wwidth)
        b1 = Button(obtalt, text='Confirmar datos', command=(lambda altura=ents: retornar(altura)))
        b1.focus_force()
        b1.pack(side=LEFT, padx=5, pady=5)
        b1.bind('Return', (lambda event, altura=ents: retornar(altura)))
        b2 = Button(obtalt, text='Cancelar', command=salir)
        b2.pack(side=RIGHT, padx=5, pady=5)

        obtalt_xpos=int((screen_width - wwidth * 5 - 10*5) / 2)
        obtalt_ypos=int((screen_height * 0.5))
        obtalt.title("Calcula fecha en que el Sol sale por el acimut de estructura")
        obtaltWindowPosition="+" + str(obtalt_xpos) + "+" + str(obtalt_ypos)
        obtalt.geometry(obtaltWindowPosition)

        obtalt.mainloop()

    def coincidir_sol_a(self):
        self.coincidir_sol()

    def pstz(self): # Rutina para calcular fechas en las que Sol pasa x el cenit

            global fig2, ax2, canvas2
            fields = "Altura del horizonte en ese punto"
    
            global global_alt, global_lugar      #, global_lugar
            bandera = True
            global_alt = 0.    ##### INGRESA ALTURA DEL HORIZONTE EN EL ACIMUT A EVALUAR
            print "Buscando Fecha del paso del Sol por el cenit"
            print "Calculando..."
############ EVALUA SI ES POSIBLE EL PASO DEL SOL POR EL CENIT EN ESE LUGAR ##############

############# CALCULA LA OBLICUEDAD DE LA ECLIPTICA EN LA EPOCA CORRESPONDIENTE A LA FECHA ACTUAL 
            JDE = julian_date(str(global_lugar.date))
            Tcalc = (JDE - 2451545.) / 36525.
            epsilon_0 = 23.439291111 + (-46.815 *Tcalc - 0.00059 *Tcalc*Tcalc + 0.001813 *Tcalc*Tcalc*Tcalc)/3600.

            if float(global_lugar.lat) * 180 / np.pi > epsilon_0:
                self.v_aviso("No puede haber Paso del Sol por el Cenit a esta Latitud","ERROR!")
            else:
                aci = acos(tan(global_lugar.lat))*180/np.pi            

############# EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE VERANO SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA ÉPOCA DE LA FECHA) ###############
                min_acimut_solar1 = sin(epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
                min_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
                try:
                   min_acimut_solar = acos(min_acimut_solar1 / min_acimut_solar2) * 180. / pi
                except:
                   min_acimut_solar = 0.
                   self.v_aviso(u"No se puede calcular el m\u00EDnimo acimut solar", u"\u00A1AVISO!")

############# AHORA EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE INVIERNO EN SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA EPOCA DE LA FECHA) ########
                max_acimut_solar1 = sin(-epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
                max_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
                try:
                    max_acimut_solar = acos(max_acimut_solar1 / max_acimut_solar2) * 180. / pi
                except:
                    max_acimut_solar = 180.
                    self.v_aviso(u"No se puede calcular el m\u00E1ximo acimut solar", u"\u00A1AVISO!")

############# ENCUENTRA CUAL ES EL ACIMUT DEL SOLSTICIO MAS CERCANO A LA ALINEACION INGRESADA #########################
###### Y EVALUA SI ESTA SE ENCUENTRA DENTRO DEL RANGO DE POSIBLES ALINEACIONES CON EL SOL EN SITIO DE OBSERVACION #####
                if aci > 180.:
                    temporal = min_acimut_solar
                    min_acimut_solar = 360.0 - max_acimut_solar
                    max_acimut_solar = 360.0 - temporal

           #######   ESTO SOLO ES PARA PROPOSITOS DE CONTROL ###################
                if abs(aci-min_acimut_solar) < abs(aci-max_acimut_solar):
                    print u"Acimut m\u00EDnimo que puede tener el Sol a esa altura=", min_acimut_solar
                    print u"Acimut m\u00E1ximo que puede tener el Sol a esa altura=", max_acimut_solar
            ####################################################################

                if aci < min_acimut_solar or aci > max_acimut_solar:
                    self.v_aviso(u"A esta latitud no puede haber Paso del Sol por el Cenit", u"\u00A1ERROR!")
                    bandera = False
#                if aci > max_acimut_solar:
#                    self.v_aviso(u"A este acimut no puede existir coincidencia entre\nalineaci\u00F3n de estructura y salida/puesta del Sol", u"\u00A1ERROR!")
#                    bandera = False

########################################################################################################################
########## CALCULA LA DECLINACION QUE TENDRIA EL SOL SI ESTUVIERA ALINEADO CON LA ESTRUCTURA (EPOCA J2000.0)############
########################################################################################################################
                if bandera:
                    dec_solar = sin(global_lugar.lat) * sin(global_alt*np.pi/180.)
                    dec_solar = dec_solar + cos(global_lugar.lat) * cos(global_alt*np.pi/180.)*cos(aci*np.pi/180.)
                    dec_solar = asin(dec_solar) * 180. / np.pi
                    if dec_solar >= 0:
                        signo_dec = "+"
                    else:
                        signo_dec = "-"
                        dec_solar = dec_solar * -1.
                    dec_solarg = int(dec_solar)
                    dec_solarm = int((dec_solar-dec_solarg)*60.)
                    dec_solars = ((dec_solar-dec_solarg)*60.-dec_solarm)*60.
                    dec_solar = str(dec_solarg)+':'+str(dec_solarm)+':'+str(int(dec_solars*10.)/10.)
                    print "Declinación del Sol:", dec_solar

########### ENCUENTRA LAS FECHAS EN QUE EL SOL ALCANZA EL ACIMUT A EVALUAR, HALLANDO LA DIFERENCIA ENTRE ############
############# ACIMUT EVALUADO Y ACIMUT DEL SOL, CUANDO ESTA DIFERENCIA ES MINIMA, OCURRE COINCIDENCIA ###############

                    s = Sun()
                    o = Observer()
                    o.date = global_lugar.date
                    o.lat = global_lugar.lat
                    o.long = global_lugar.long
                    o.elevation = global_lugar.elevation
                    o.horizon = str(global_alt)
                    o.date = previous_solstice(o.date)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date =str(s.set_time)
                    s.compute(o)
    
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    i = 0
                    # Evalua la fecha de cuando la diferencia encontrada entre el acimut calculado del Sol
                    # y el acimut que tiene el Sol en el día del paso del sol por el cenit
                    while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                        diferencia = abs(float(s.az)*180/np.pi - aci)
                        o.date = o.date + (24*hour)
                        s.compute(o)
                        if aci < 180.:
                            o.date=str(s.rise_time)
                        else:
                            o.date = str(s.set_time)
                        s.compute(o)
                        i += 1
                    o.date = o.date - 24*hour  # Primera fecha encontrada en que el Sol pasa por ese acimut
                    d1 = o.date
                    print "Intentos:",i, "; ",o.date
                    print " "

                    o.date = next_solstice(o.date)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date =str(s.set_time)
                    s.compute(o)
    
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    i = 0
                    while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                        diferencia = abs(float(s.az)*180/np.pi - aci)
                        o.date = o.date + (24*hour)
                        s.compute(o)
                        if aci < 180.:
                            o.date=str(s.rise_time)
                        else:
                            o.date = str(s.set_time)
                        s.compute(o)
                        i += 1
                    o.date = o.date - 24*hour  # Segunda fecha encontrada en que el Sol pasa por ese acimut
                    d2 = o.date
                    print "Intentos:",i, "; ",o.date
    
                    print d1, "  ", d2
    
                    msj0 = "PASO DEL SOL POR EL CENIT"
                    m1_1 = str(float(int(aci*10.))/10.)
                    msj1 = u"Declinaci\u00F3n del Sol en el Acimut " + m1_1 + " : " + dec_solar
                    msj2 = "Fechas de paso del Sol por el Cenit, para la latitud "+str(o.lat)
                    msj3 = " "
                    msj4 = d1
                    msj5 = 'o'
                    msj6 = d2
                    self.mensaje(fig2, ax2, canvas2, msj0, msj2, msj3, msj4, msj5, msj6)


    def pstz_a(self):
        self.pstz()
###########################################################################################################################


    def coincidir_sol2(self): # Rutina para calcular fechas en las que Sol pasa x el cenit

            global fig2, ax2, canvas2
            fields = "Altura del horizonte en ese punto"
    
            global global_alt, global_lugar      #, global_lugar
            bandera = True
            global_alt = 0.    ##### INGRESA ALTURA DEL HORIZONTE EN EL ACIMUT A EVALUAR
            print "Buscando Fecha del paso del Sol por el cenit"
            print "Calculando..."
############ EVALUA SI ES POSIBLE EL PASO DEL SOL POR EL CENIT EN ESE LUGAR ##############

############# CALCULA LA OBLICUEDAD DE LA ECLIPTICA EN LA EPOCA CORRESPONDIENTE A LA FECHA ACTUAL 
            JDE = julian_date(str(global_lugar.date))
            Tcalc = (JDE - 2451545.) / 36525.
            epsilon_0 = 23.439291111 + (-46.815 *Tcalc - 0.00059 *Tcalc*Tcalc + 0.001813 *Tcalc*Tcalc*Tcalc)/3600.

            if float(global_lugar.lat) * 180 / np.pi > epsilon_0:
                self.v_aviso("No puede haber Paso del Sol por el Cenit a esta Latitud","ERROR!")
            else:
                aci = acos(tan(global_lugar.lat))*180/np.pi            

############# EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE VERANO SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA ÉPOCA DE LA FECHA) ###############
                min_acimut_solar1 = sin(epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
                min_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
                try:
                   min_acimut_solar = acos(min_acimut_solar1 / min_acimut_solar2) * 180. / pi
                except:
                   min_acimut_solar = 0.
                   self.v_aviso(u"No se puede calcular el m\u00EDnimo acimut solar", u"\u00A1AVISO!")

############# AHORA EVALUA EL ACIMUT DEL SOL EL SOLSTICIO DE INVIERNO EN SITIO DE OBSERVACION (USA LA OBLICUEDAD EN LA EPOCA DE LA FECHA) ########
                max_acimut_solar1 = sin(-epsilon_0 * pi / 180.) - sin(global_lugar.lat) * sin(global_alt*pi/180.)
                max_acimut_solar2 = cos(global_lugar.lat) * cos (global_alt*pi/180.)
                try:
                    max_acimut_solar = acos(max_acimut_solar1 / max_acimut_solar2) * 180. / pi
                except:
                    max_acimut_solar = 180.
                    self.v_aviso(u"No se puede calcular el m\u00E1ximo acimut solar", u"\u00A1AVISO!")

############# ENCUENTRA CUAL ES EL ACIMUT DEL SOLSTICIO MAS CERCANO A LA ALINEACION INGRESADA #########################
###### Y EVALUA SI ESTA SE ENCUENTRA DENTRO DEL RANGO DE POSIBLES ALINEACIONES CON EL SOL EN SITIO DE OBSERVACION #####
                if aci > 180.:
                    temporal = min_acimut_solar
                    min_acimut_solar = 360.0 - max_acimut_solar
                    max_acimut_solar = 360.0 - temporal

           #######   ESTO SOLO ES PARA PROPOSITOS DE CONTROL ###################
                if abs(aci-min_acimut_solar) < abs(aci-max_acimut_solar):
                    print u"Acimut m\u00EDnimo que puede tener el Sol a esa altura=", min_acimut_solar
                    print u"Acimut m\u00E1ximo que puede tener el Sol a esa altura=", max_acimut_solar
            ####################################################################

                if aci < min_acimut_solar or aci > max_acimut_solar:
                    self.v_aviso(u"A esta latitud no puede haber Paso del Sol por el Cenit", u"\u00A1ERROR!")
                    bandera = False
#                if aci > max_acimut_solar:
#                    self.v_aviso(u"A este acimut no puede existir coincidencia entre\nalineaci\u00F3n de estructura y salida/puesta del Sol", u"\u00A1ERROR!")
#                    bandera = False

########################################################################################################################
########## CALCULA LA DECLINACION QUE TENDRIA EL SOL SI ESTUVIERA ALINEADO CON LA ESTRUCTURA (EPOCA J2000.0)############
########################################################################################################################
                if bandera:
                    dec_solar = sin(global_lugar.lat) * sin(global_alt*np.pi/180.)
                    dec_solar = dec_solar + cos(global_lugar.lat) * cos(global_alt*np.pi/180.)*cos(aci*np.pi/180.)
                    dec_solar = asin(dec_solar) * 180. / np.pi
                    if dec_solar >= 0:
                        signo_dec = "+"
                    else:
                        signo_dec = "-"
                        dec_solar = dec_solar * -1.
                    dec_solarg = int(dec_solar)
                    dec_solarm = int((dec_solar-dec_solarg)*60.)
                    dec_solars = ((dec_solar-dec_solarg)*60.-dec_solarm)*60.
                    dec_solar = str(dec_solarg)+':'+str(dec_solarm)+':'+str(int(dec_solars*10.)/10.)
                    print "Declinación del Sol:", dec_solar

########### ENCUENTRA LAS FECHAS EN QUE EL SOL ALCANZA EL ACIMUT A EVALUAR, HALLANDO LA DIFERENCIA ENTRE ############
############# ACIMUT EVALUADO Y ACIMUT DEL SOL, CUANDO ESTA DIFERENCIA ES MINIMA, OCURRE COINCIDENCIA ###############

                    s = Sun()
                    o = Observer()
                    o.date = global_lugar.date
                    o.lat = global_lugar.lat
                    o.long = global_lugar.long
                    o.elevation = global_lugar.elevation
                    o.horizon = str(global_alt)
                    o.date = previous_solstice(o.date)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date =str(s.set_time)
                    s.compute(o)
    
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    i = 0
                    # Evalua la fecha de cuando la diferencia encontrada entre el acimut calculado del Sol
                    # y el acimut que tiene el Sol en el día del paso del sol por el cenit
                    while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                        diferencia = abs(float(s.az)*180/np.pi - aci)
                        o.date = o.date + (24*hour)
                        s.compute(o)
                        if aci < 180.:
                            o.date=str(s.rise_time)
                        else:
                            o.date = str(s.set_time)
                        s.compute(o)
                        i += 1
                    o.date = o.date - 24*hour  # Primera fecha encontrada en que el Sol pasa por ese acimut
                    d1 = o.date
                    print "Intentos:",i, "; ",o.date
                    print " "

                    o.date = next_solstice(o.date)
                    s.compute(o)
                    if aci < 180.:
                        o.date=str(s.rise_time)
                    else:
                        o.date =str(s.set_time)
                    s.compute(o)
    
                    diferencia = abs(float(s.az)*180/np.pi - aci)
                    i = 0
                    while abs(float(s.az)*180/np.pi - aci) <= diferencia and i < 183:
                        diferencia = abs(float(s.az)*180/np.pi - aci)
                        o.date = o.date + (24*hour)
                        s.compute(o)
                        if aci < 180.:
                            o.date=str(s.rise_time)
                        else:
                            o.date = str(s.set_time)
                        s.compute(o)
                        i += 1
                    o.date = o.date - 24*hour  # Segunda fecha encontrada en que el Sol pasa por ese acimut
                    d2 = o.date
                    print "Intentos:",i, "; ",o.date
    
                    print d1, "  ", d2
    
                    msj0 = "PASO DEL SOL POR EL CENIT"
                    m1_1 = str(float(int(aci*10.))/10.)
                    msj1 = u"Declinaci\u00F3n del Sol en el Acimut " + m1_1 + " : " + dec_solar
                    msj2 = "Fechas de paso del Sol por el Cenit, para la latitud "+str(o.lat)
                    msj3 = " "
                    msj4 = d1
                    msj5 = 'o'
                    msj6 = d2
                    self.mensaje(fig2, ax2, canvas2, msj0, msj2, msj3, msj4, msj5, msj6)


    def coincidir_sol2a(self):
        self.coincidir_sol2()




###########################################################################################################################


    def aniodecimal(self,fechat,incldia):      # Transforma el anio dado en aaaa/mm/dd a anios decimales
                                               # 1=incluye los dias en el calculo, 0=no incluye los dias, solo meses
        anio = ""
        mes = ""
        dia = ""
        i = 0
        while fechat[i] <> "/":
            anio = anio + fechat[i]
            i += 1
        i += 1
        while fechat[i] <> "/":
            mes = mes + fechat[i]
            i += 1
        i += 1
        while fechat[i] <> " ":
            dia = dia + fechat[i]
            i += 1
        y = float(anio) + (float(mes) - 1.)/12. + incldia*(float(dia)/365.2422)

        return y

    def lunapasanodo(self,k,E): # CALCULA PASOS DE LA LUNA A TRAVES DE LOS NODOS

        T = k / 1342.23
        D = 183.6380 + 331.73735691*k + 0.0015057*T*T + 0.00000209*T*T*T - 0.000000010*T*T*T*T
        M = 17.4006 + 26.82037250*k + 0.0000999*T*T + 0.00000006*T*T*T
        Mp = 38.3776 + 355.52747322*k + 0.0123577*T*T + 0.000014628*T*T*T - 0.000000069*T*T*T*T
        omega = 123.9767 - 1.44098949*k + 0.0020625*T*T + 0.00000214*T*T*T - 0.000000016*T*T*T*T
        V = 299.75 + 132.85*T - 0.009173*T*T
        P = omega + 272.75 - 2.3*T
        D = D*np.pi / 180.
        M = M*np.pi/180.
        Mp = Mp*np.pi/180.
        omega = omega*np.pi/180.
        V = V*np.pi/180.
        P = P*np.pi/180.

        JDEpasanodo = 2451565.1619 + 27.212220817*k + 0.0002572*T*T + 0.000000021*T*T*T
        JDEpasanodo = JDEpasanodo - 0.000000000088*T*T*T*T - 0.4721*sin(Mp) - 0.1649*sin(2.*D)
        JDEpasanodo = JDEpasanodo - 0.0868*sin(2.*D - Mp) + 0.0084*sin(2.*D + Mp)
        JDEpasanodo = JDEpasanodo - 0.0083*E*sin(2.*D - M) - 0.0039*E*sin(2.*D-M-Mp) + 0.0034*sin(2.*Mp)
        JDEpasanodo = JDEpasanodo - 0.0031*sin(2.*D-2.*Mp) + 0.003*E*sin(2.*D+M) + 0.0028*E*sin(M-Mp)
        JDEpasanodo = JDEpasanodo + 0.0026*E*sin(M) + 0.0025*sin(4.*D) + 0.0024*sin(D)
        JDEpasanodo = JDEpasanodo + 0.0022*E*sin(M+Mp) + 0.0017*sin(omega) + 0.0014*sin(4.*D-Mp)
        JDEpasanodo = JDEpasanodo + 0.0005*E*sin(2.*D+M-Mp) + 0.0004*E*sin(2.*D-M+Mp)
        JDEpasanodo = JDEpasanodo - 0.0003*E*(sin(2.*D-2.*M) - sin(4.*D-M)) + 0.0003*(sin(V)+sin(P))

        return [JDEpasanodo, omega]

    def dextremasluna(self, k, E): # Calcula fechas de decs max y min, asi como la dec. correspondiente a lunacion k
        T = k / 1336.86
        Dn = (152.2029 + 333.0705546 * k - 0.00004025 * T * T + 0.00000011 * T * T * T) * np.pi / 180.
        Ds = (345.6676 + 333.0705546 * k - 0.00004025 * T * T + 0.00000011 * T * T * T) * np.pi / 180.
        Mn = (14.8591 + 26.9281592 * k -0.0000544 * T * T - 0.00000010 * T * T * T) * np.pi / 180.
        Ms = (1.39510 + 26.9281592 * k -0.0000544 * T * T - 0.00000010 * T * T * T) * np.pi / 180.
        Mpn = (4.6881 + 356.9562795 * k + 0.0103126 * T * T + 0.00001251 * T * T * T) * np.pi / 180.
        Mps = (186.21 + 356.9562795 * k + 0.0103126 * T * T + 0.00001251 * T * T * T) * np.pi / 180.
        Fn = (325.8867 + 1.4467806 * k - 0.0020708 * T * T - 0.00000215 * T * T * T) * np.pi / 180.
        Fs = (145.1633 + 1.4467806 * k - 0.0020708 * T * T - 0.00000215 * T * T * T) * np.pi / 180.

                ############## Calculo de los terminos periodicos de la Tabla 50.A del libro de Meeus
        T50An = 0.8975*cos(Fn) - 0.4726*sin(Mpn) - 0.103*sin(2.*Fn) - 0.0976*sin(2.*Dn-Mpn)
        T50An = T50An - 0.0462*cos(Mpn-Fn) - 0.0461*cos(Mpn+Fn) - 0.0438*sin(2.*Dn) + 0.0162*E*sin(Mn)
        T50An = T50An - 0.0157*cos(3.*Fn) + 0.0145*sin(Mpn+2.*Fn) + 0.0136*cos(2.*Dn-Fn)
        T50An = T50An - 0.0095*cos(2.*Dn-Mpn-Fn) - 0.0091*cos(2.*Dn-Mpn+Fn) - 0.0089*cos(2.*Dn+Fn)
        T50An = T50An + 0.0075*sin(2.*Mpn) - 0.0068*sin(Mpn-2*Fn) + 0.0061*cos(2.*Mpn-Fn)
        T50An = T50An - 0.0047*sin(Mpn+3.*Fn) - 0.0043*E*sin(2.*Dn-Mn-Mpn) - 0.004*cos(Mpn-2.*Fn)
        T50An = T50An - 0.0037*sin(2.*Dn-2*Mpn) + 0.0031*sin(Fn) + 0.003*sin(2.*Dn+Mpn)
        T50An = T50An - 0.0029*cos(Mpn+2.*Fn) - 0.0029*E*sin(2.*Dn-Mn) - 0.0027*sin(Mpn+Fn)
        T50An = T50An + 0.0024*E*sin(Mn-Mpn) - 0.0021*sin(Mpn-3.*Fn) + 0.0019*sin(2.*Mpn+Fn)
        T50An = T50An + 0.0018*(cos(2.*Dn-2.*Mpn-Fn) + sin(3.*Fn)) + 0.0017*(cos(Mpn+3.*Fn) + cos(2.*Mpn))
        T50An = T50An - 0.0014*cos(2.*Dn-Mpn) + 0.0013*(cos(2.*Dn+Mpn+Fn)+cos(Mpn))+0.0012*sin(3.*Mpn+Fn)
        T50An = T50An + 0.0011*(sin(2.*Dn-Mpn+Fn)-cos(2.*Dn-2.*Mpn)) + 0.001*(cos(Dn+Fn)+E*sin(Mn+Mpn))
        T50An = T50An - 0.0009*sin(2.*Dn-2.*Fn) + 0.0007*cos(2.*Mpn+Fn) - 0.0007*cos(3.*Mpn+Fn)

        T50As = -0.8975*cos(Fs) - 0.4726*sin(Mps) - 0.103*sin(2.*Fs) - 0.0976*sin(2.*Ds-Mps)
        T50As = T50As + 0.0541*cos(Mps-Fs) + 0.0516*cos(Mps+Fs) - 0.0438*sin(2.*Ds) + 0.0112*E*sin(Ms)
        T50As = T50As + 0.0157*cos(3.*Fs) + 0.0023*sin(Mps+2.*Fs) - 0.0136*cos(2.*Ds-Fs)
        T50As = T50As + 0.0110*cos(2.*Ds-Mps-Fs) + 0.0091*cos(2.*Ds-Mps+Fs) + 0.0089*cos(2.*Ds+Fs)
        T50As = T50As + 0.0075*sin(2.*Mps) - 0.0030*sin(Mps-2*Fs) - 0.0061*cos(2.*Mps-Fs)
        T50As = T50As - 0.0047*sin(Mps+3.*Fs) - 0.0043*E*sin(2.*Ds-Ms-Mps) + 0.004*cos(Mps-2.*Fs)
        T50As = T50As - 0.0037*sin(2.*Ds-2*Mps) - 0.0031*sin(Fs) + 0.003*sin(2.*Ds+Mpn)
        T50As = T50As + 0.0029*cos(Mps+2.*Fs) - 0.0029*E*sin(2.*Ds-Ms) - 0.0027*sin(Mps+Fs)
        T50As = T50As + 0.0024*E*sin(Ms-Mps) - 0.0021*sin(Mps-3.*Fs) - 0.0019*sin(2.*Mps+Fs)
        T50As = T50As - 0.0006*cos(2.*Ds-2.*Mps-Fs) - 0.0018*sin(3.*Fs)-0.0017*(cos(Mps+3.*Fs)-cos(2.*Mps))
        T50As = T50As + 0.0014*cos(2.*Ds-Mps) - 0.0013*(cos(2.*Ds+Mps+Fs)+cos(Mps))+0.0012*sin(3.*Mps+Fs)
        T50As = T50As + 0.0011*(sin(2.*Ds-Mps+Fs)+cos(2.*Ds-2.*Mps)) + 0.001*(cos(Ds+Fs)+E*sin(Ms+Mps))
        T50As = T50As - 0.0009*sin(2.*Ds-2.*Fs) - 0.0007*cos(2.*Mps+Fs) - 0.0007*cos(3.*Mps+Fs)

        JDEn = 2451562.5897 + 27.321582241*k + 0.000100695*T*T - 0.000000141*T*T*T + T50An
        JDEs = 2451548.9289 + 27.321582241*k + 0.000100695*T*T - 0.000000141*T*T*T + T50As

                ############## Calculo de los terminos periodicos de la Tabla 50.B del libro de Meeus
        T50Bn = 5.1093*sin(Fn) + 0.2658*cos(2*Fn) + 0.1448*sin(2.*Dn-Fn) - 0.0322*sin(3.*Fn)
        T50Bn = T50Bn + 0.0133*cos(2.*Dn-2.*Fn) + 0.0125*cos(2.*Dn) - 0.0124*sin(Mpn-Fn)
        T50Bn = T50Bn - 0.0101*sin(Mpn+2.*Fn) + 0.0097*cos(Fn) - 0.0087*E*sin(2.*Dn+Mn-Fn)
        T50Bn = T50Bn + 0.0074*sin(Mpn+3.*Fn) + 0.0067*sin(Dn+Fn) + 0.0063*sin(Mpn-2.*Fn)
        T50Bn = T50Bn + 0.0060*E*sin(2.*Dn-Mn-Fn) - 0.0057*sin(2.*Dn-Mpn-Fn) - 0.0056*cos(Mpn+Fn)
        T50Bn = T50Bn + 0.0052*cos(Mpn+2.*Fn) + 0.0041*cos(2.*Mpn+Fn) - 0.004*cos(Mpn-3.*Fn)
        T50Bn = T50Bn + 0.0038*cos(2.*Mpn-Fn) - 0.0034*cos(Mpn-2.*Fn) - 0.0029*sin(2.*Mpn)
        T50Bn = T50Bn + 0.0029*sin(3.*Mpn+Fn) - 0.0028*(E*cos(2.*Dn+Mn-Fn) + cos(Mpn-Fn))
        T50Bn = T50Bn - 0.0023*cos(3.*Fn) - 0.0021*sin(2.*Dn+Fn) + 0.0019*cos(Mpn+3.*Fn)
        T50Bn = T50Bn + 0.0018*cos(Dn+Fn) + 0.0017*sin(2.*Mpn-Fn) + 0.0015*cos(3.*Mpn+Fn)
        T50Bn = T50Bn + 0.0014*cos(2.*Dn+2.*Mpn+Fn)-0.0012*(sin(2.*Dn-2.*Mpn-Fn) + cos(2.*Mpn))
        T50Bn = T50Bn - 0.0010*(cos(Mpn) + sin(2.*Fn)) + 0.0006*sin(Mpn+Fn)

        T50Bs = -5.1093*sin(Fs) + 0.2658*cos(2*Fs) - 0.1448*sin(2.*Ds-Fs) + 0.0322*sin(3.*Fs)
        T50Bs = T50Bs + 0.0133*cos(2.*Ds-2.*Fs) + 0.0125*cos(2.*Ds) - 0.0015*sin(Mps-Fs)
        T50Bs = T50Bs + 0.0101*sin(Mps+2.*Fs) - 0.0097*cos(Fs) + 0.0087*E*sin(2.*Ds+Ms-Fs)
        T50Bs = T50Bs + 0.0074*sin(Mps+3.*Fs) + 0.0067*sin(Ds+Fs) - 0.0063*sin(Mps-2.*Fs)
        T50Bs = T50Bs - 0.0060*E*sin(2.*Ds-Ms-Fs) + 0.0057*sin(2.*Ds-Mps-Fs) - 0.0056*cos(Mps+Fs)
        T50Bs = T50Bs - 0.0052*cos(Mps+2.*Fs) - 0.0041*cos(2.*Mps+Fs) - 0.004*cos(Mps-3.*Fs)
        T50Bs = T50Bs - 0.0038*cos(2.*Mps-Fs) + 0.0034*cos(Mps-2.*Fs) - 0.0029*sin(2.*Mps)
        T50Bs = T50Bs + 0.0029*sin(3.*Mps+Fs) + 0.0028*(E*cos(2.*Ds+Ms-Fs) - cos(Mps-Fs))
        T50Bs = T50Bs + 0.0023*cos(3.*Fs) + 0.0021*sin(2.*Ds+Fs) + 0.0019*cos(Mps+3.*Fs)
        T50Bs = T50Bs + 0.0018*cos(Ds+Fs) - 0.0017*sin(2.*Mps-Fs) + 0.0015*cos(3.*Mps+Fs)
        T50Bs = T50Bs + 0.0014*cos(2.*Ds+2.*Mps+Fs) + 0.0012*(sin(2.*Dn-2.*Mps-Fs) - cos(2.*Mps))
        T50Bs = T50Bs + 0.0010*(cos(Mps) - sin(2.*Fs)) + 0.0037*sin(Mps+Fs)

        maxdecn = 23.6961 - 0.013004 * T + T50Bn
        maxdecs = 23.6961 - 0.013004 * T + T50Bs

        return [JDEn, maxdecn, JDEs, maxdecs]

        ############ CALCULA MAXIMAS DECLINACIONES DE LA LUNA ############################
    def decsluna(self):

        global fout
        print "###########################"
        print "Calculo de \"Lunasticios\" "

            # Empezamos por hallar la longitud del nodo ascendente (omega) y desde alli empezar a iterar para
            # hallar cuando omega se hace igual a cero (que es cuando ocurren los lunasticios), calculando
            # k += 1 y hallando anios decimales (y) por despeje de fmla para k
        fechat = str(global_lugar.date) 
        JDE = julian_date(fechat)
        y = self.aniodecimal(fechat,1)     # El 3er parametro dice si quiere incluir los dias
                                           # en el calculo del anio decimal, 1=si, 0=no
        Tjde = (JDE - 2451545.) / 36525.
        k = int((y - 2000.05) * 13.4223)
        k = float(k)
        bandera2 = False
        errormax = 3.
        omega_ant = 0. + errormax
        bandera = True
        seguridad = 0
                # A continuacion un loop que calcula las omegas (long. nodo asc.) de las fechas, hasta que llegue a un
                # valor que sea lo mas cercano a un multiplo de 360.

        while bandera:
            seguridad += 1   # Esta variable es para poner un limite al numero de iteraciones a realizar
            if seguridad > 500:
                self.v_aviso("No se alcanza una respuesta","AVISO")
                salir()

            # Usando Ec.(47.7) segunda edicion de "AA"-Meeus, obtenida a su vez de (Chapront,1998)
            omega = 125.04455479-1934.1362891*Tjde+0.0020754*Tjde*Tjde+Tjde*Tjde*Tjde/467441.-Tjde*Tjde*Tjde*Tjde/60616000.
            diferencia = (omega/360. - float(int(omega/360.)))*360.

            if omega >= 0:
                if diferencia >= 180.:
                    omega = omega + 360. - diferencia
                else:
                    omega = omega - diferencia
            else:
                if abs(diferencia) >= 180.:
                    omega = omega - 360. - diferencia
                else:
                    omega = omega - diferencia

            bandera2 = True
            seguridad2= 0
            while bandera2:
                # Esta ecuacion es tomada de la segunda edicion "Astronomical Algorithms" de J. Meeus (47.7)
                Tcalc = (omega - 125.0445479) / (- 1934.1362891 + 0.0020754*Tjde + Tjde*Tjde / 467441. - Tjde*Tjde*Tjde/60616000)
                if abs(Tcalc - Tjde) > 0.0000001:
                    Tjde = Tcalc
                    seguridad2 = seguridad2 + 1
                else:
                    bandera2 = False

            # Encuentra si la long. de la luna esta cerca de 90 o de 270 grados y en base a esto
            # decide si encuentra el T cuando la Luna llega a los 90 o 270 mas cercanos
            # Usando Ec.(47.1) segunda edicion de "AA"-Meeus,
            Lp = 218.3164477+481267.88123421*Tjde-0.0015786*Tjde*Tjde+Tjde*Tjde*Tjde/538841.-Tjde*Tjde*Tjde*Tjde/65194000.
            diferencia = (Lp/360. - float(int(Lp/360.)))*360.
            if diferencia < 0:
                diferencia = diferencia + 360.
            if diferencia <= 180.:
                Lp = Lp + (90.-diferencia)
            else:
                Lp = Lp + (270.-diferencia)

            bandera2 = True
            seguridad2= 0
            while bandera2:
                # Esta ecuacion es tomada de la segunda edicion "Astronomical Algorithms" de J. Meeus (47.1)
                Tcalc = (Lp-218.3164477)/(481267.88123421 - 0.0015786*Tjde + Tjde*Tjde / 538841.-Tjde*Tjde*Tjde/65194000)
                if abs(Tcalc - Tjde) > 0.0000001:
                    Tjde = Tcalc
                    seguridad2 = seguridad2 + 1
                else:
                    bandera2 = False
            bandera = False

            # Calcula el nuevo omega
            omega = 125.04455479-1934.1362891*Tjde+0.0020754*Tjde*Tjde+Tjde*Tjde*Tjde/467441.-Tjde*Tjde*Tjde*Tjde/60616000.
            # Calcula el nuevo Lp
            Lp = 218.3164477+481267.88123421*Tjde-0.0015786*Tjde*Tjde+Tjde*Tjde*Tjde/538841.-Tjde*Tjde*Tjde*Tjde/65194000.
            # Encuentra fecha juliana mas cercana a la fecha de trabajo (fechat)en que omega esta cerca de cero
            # y Lp cerca de 90 o 270
            JDE = 2451545. + Tjde * 36525.
            fechat = self.JDEtoCAL(JDE,0) # El tercer parametro indica que necesitamos la fechat con decimales

            print omega, Lp,fechat


        # Despues de hallar la fecha en que la long. del nodo ascendente esta mas cerca de cero, toma esa fecha
        # como inicio para calcular las fechas en que la Luna alcanza maximas declinaciones

        y = self.aniodecimal(fechat,0) # El 3er parametro dice si quiere incluir los dias
                                           # en el calculo del anio decimal, 1=si, 0=no
        E = 1 - 0.002516 * Tjde - 0.0000074 * Tjde * Tjde
        k = int(abs(y - 2000.03) * 13.3686)
        if y < 2000.03:
            k = -k
        k = float(k)

        print "Calculo de extremas declinaciones de la Luna"
        msj0 = "PARADAS AL NORTE Y SUR DE LA LUNA"
        msj1 = " "

                ### Llama la rutina para determinar las fechas (julianas) de las declinaciones extremas
                ### de la Luna hacia el N y al S, asi como el valor de dichas declinaciones
                ### 0 -> JDEn / 1 -> Maxima decl Norte / 2 -> JDEs / 3 -> Maxima decl Sur
                ### para la lunacion k que hemos encontrado

        i = 0
        maxdecn_ant = 0
        maxdecs_ant = 0
        maxdecn_ant_ant = 0
        maxdecs_ant_ant = 0
        bandera = True
        direccion_k = +1.
        while bandera:
            temporal = self.dextremasluna(k,E)

                # Calcula el valor de la longitud del nodo ascendente de la Luna en las fechas (julianas)
                # en que ocurren las maximas declinaciones de la Luna (segun formula 47.7 de A-A de Meeus), de esta
                # manera, se hace un ajuste (si es necesario) para acercar la fecha de los calculos al
                # momento en que el nodo ascendente de la orbita lunar esta cerca del equinoccio vernal.
            JDEn = temporal[0]
            Tjde = (JDEn - 2451545.) / 36525.
            omegan = 125.0445479-1934.1362891*Tjde+0.0020754*Tjde*Tjde+Tjde*Tjde*Tjde/467441.-Tjde*Tjde*Tjde*Tjde/60616000.
            omegan = ((omegan / 360.) - int(omegan / 360.)) * 360.
            if omegan < 0:
                omegan += 360.

            JDEs = temporal[2]
            Tjde = (JDEs - 2451545.) / 36525.
            omegas = 125.0445479-1934.1362891*Tjde+0.0020754*Tjde*Tjde+Tjde*Tjde*Tjde/467441.-Tjde*Tjde*Tjde*Tjde/60616000.
            omegas = ((omegas / 360.) - int(omegas / 360.)) * 360.
            if omegas < 0:
                omegas += 360.

                # Obtiene las fechas gregorianas en que ocurren las extremas declinaciones lunares
            fechan = self.JDEtoCAL(JDEn,0)
            fechas = self.JDEtoCAL(JDEs,0)

            maxdecn = temporal[1]
            maxdecs = temporal[3]

#            print i, k, maxdecn, maxdecs, JDEn, JDEs
#            raw_input()

            if i == 1 and abs(maxdecn) < abs(maxdecn_ant):
                direccion_k = direccion_k * (-1)
            else:
                if abs(maxdecn) < abs(maxdecn_ant):
                    bandera = False
                    maxdecn = maxdecn_ant
                    JDEn = JDEn_ant
                    fechan = self.JDEtoCAL(JDEn,0)
                    if abs(maxdecs) < abs(maxdecs_ant):
                        maxdecs = maxdecs_ant
                        JDEs = JDEs_ant
                        fechas = self.JDEtoCAL(JDEs,0)
                else:
                    maxdecn_ant = maxdecn
                    JDEn_ant = JDEn
                    if abs(maxdecs) > abs(maxdecs_ant):
                        maxdecs_ant = maxdecs
                        JDEs_ant = JDEs
            i += 1
            k = k + direccion_k

################################################
                # Aqui se calculan los datos relativos a la Luna para el sitio de observacion: acimut a la salida y la
                # puesta, usando las fechas encontradas de maxima declinacion norte y maxima declinacion Sur
                # mostrando previamente las fechas de "lunasticios" mas cercanos a la fecha ingresada por el usuario

        horizonte = self.horizon(float(global_lugar.lat)*180./np.pi, -float(global_lugar.long)*180./np.pi) # Calcula el horizonte local
        print "Max. Declinacion Norte"
        print "Fecha Juliana = ",JDEn, "max. fecha Gregoriana", fechan
        print "Long. Nodo Asc (Chapront)= ", omegan
        print "Declinacion de la Luna:", maxdecn

        msj2 = "Max. Declinacion Norte"
        msj3 = "Fecha Juliana : "+str(int(JDEn*10.)/10.) + ", fecha Gregoriana: " + fechan

        l = Moon()
        o = Observer()
        o.lat = global_lugar.lat
        o.lon = global_lugar.lon
        o.date = fechan
        o.epoch = o.date
        l.compute(o)
        try:
            o.date = l.rise_time
        except:
            o.date = o.date - 24*hour
            l.compute(o)
            o.date = l.rise_time
        l.compute(o) # Calcula caracteristicas de la Luna en la hora de su salida - horizonte ideal

################# Hace las correcciones necesarias para calcular caracteristicas lunares segun horizonte local
        iazluna = l.az * 180/np.pi   # Toma el dato del acimut del orto lunar
        deltaz = horizonte[int(iazluna)]/tan(np.pi/2 - o.lat)
        while deltaz > 1.0:
            if  o.lat >= 0.:
                iazluna2 = iazluna + 0.5*deltaz
            else:
                iazluna2 = iazluna - 0.5*deltaz
            o.horizon = horizonte[int(iazluna2)]*np.pi/180. # Encuentra para ese acimut cuan alto es el horizonte y lo incorpora a los calculos
            l.compute(o) # calcula datos lunares nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
            try:
                o.date = l.rise_time
            except:
                o.date = o.date - 24*hour
                l.compute(o)
                o.date = l.rise_time
            l.compute(o)
            iazluna = l.az * 180/np.pi
            deltaz = l.az*180/np.pi - iazluna2
#######################################
        print "Declinacion de la Luna (eph):", (l.dec + 0.0000001)*180./np.pi
        print "Acimut salida = ", l.az
        print "Altura del horizonte Este= ", o.horizon
        # Crea la linea de salida para el archivo, para la parada Norte
        filelinen = "                " + str(fechan) + "         "+str(int(omegan*10000)/10000.) + "            "
        filelinen = filelinen + str(int(maxdecn*1000)/1000.)+"                  N                  " + str(int(l.az*10*180/np.pi)/10.)
        try:
            o.date = l.set_time
        except:
            o.date = o.date + 24*hour
            l.compute(o)
            o.date = l.set_time
        l.compute(o)
################# Hace las correcciones necesarias para calcular caracteristicas lunares segun horizonte local
        iazluna = l.az * 180/np.pi   # Toma el dato del acimut del orto lunar
        deltaz = horizonte[int(iazluna)]/tan(np.pi/2 - o.lat)
        while deltaz > 1.0:
            if  o.lat >= 0.:
                iazluna2 = iazluna - 0.5*deltaz
            else:
                iazluna2 = iazluna + 0.5*deltaz
            o.horizon = horizonte[int(iazluna2)]*np.pi/180. # Encuentra para ese acimut cuan alto es el horizonte y lo incorpora a los calculos
            l.compute(o) # calcula datos lunares nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
            try:
                o.date = l.set_time
            except:
                o.date = o.date - 24*hour
                l.compute(o)
                o.date = l.set_time
            l.compute(o)
            iazluna = l.az * 180/np.pi
            deltaz = l.az*180/np.pi - iazluna2
#######################################
        print "Acimut puesta = ", l.az
        print "Altura del horizonte Oeste= ", o.horizon
        filelinen = filelinen + "                      " + str(int(l.az*10*180/np.pi)/10.)+"\n"
        print " "
        print "Max. Declinacion Sur"
        print "Fecha Juliana = ",JDEs, "max. fecha Gregoriana", fechas
        print "Long. Nodo Asc (Chapront)= ", omegas
        print "Declinacion de la Luna:", -maxdecs

        msj4 = " "
        msj5 = "Max. Declinacion Sur"
        msj6 = "Fecha Juliana: " + str(int(JDEs*10.)/10.) + ", fecha Gregoriana: " + fechas

        o.date = fechas
        o.epoch = o.date
        l.compute(o)
        try:
            o.date = l.rise_time
        except:
            o.date = o.date - 24*hour
            l.compute(o)
            o.date = l.rise_time
        l.compute(o)
################# Hace las correcciones necesarias para calcular caracteristicas lunares segun horizonte local (orto)
        iazluna = l.az * 180/np.pi   # Toma el dato del acimut del orto lunar
        deltaz = horizonte[int(iazluna)]/tan(np.pi/2 - o.lat)
        while deltaz > 1.0:
            if  o.lat >= 0.:
                iazluna2 = iazluna + 0.5*deltaz
            else:
                iazluna2 = iazluna - 0.5*deltaz
            o.horizon = horizonte[int(iazluna2)]*np.pi/180. # Encuentra para ese acimut cuan alto es el horizonte y lo incorpora a los calculos
            l.compute(o) # calcula datos lunares nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
            try:
                o.date = l.rise_time
            except:
                o.date = o.date - 24*hour
                l.compute(o)
                o.date = l.rise_time
            l.compute(o)
            iazluna = l.az * 180/np.pi
            deltaz = l.az*180/np.pi - iazluna2
#######################################

        print "Declinacion de la Luna (eph):", (l.dec + 0.0000001)*180./np.pi
        print "Acimut salida = ", l.az
        print "Altura del horizonte Este= ", o.horizon

        # Crea la linea de salida para el archivo, para la parada Sur
        filelines = "                " + str(fechas) + "         "+str(int(omegas*10000)/10000.) + "            "
        filelines = filelines + str(int(-maxdecs*100)/100.) + "                  S                  " + str(int(l.az*10*180/np.pi)/10.)
        try:
            o.date = l.set_time
        except:
            o.date = o.date + 24*hour
            l.compute(o)
            o.date = l.set_time
        l.compute(o)
################ Hace las correcciones necesarias para calcular caracteristicas lunares segun horizonte local (puesta)
        iazluna = l.az * 180/np.pi   # Toma el dato del acimut del orto lunar
        deltaz = horizonte[int(iazluna)]/tan(np.pi/2 - o.lat)
        while deltaz > 1.0:
            if  o.lat >= 0.:
                iazluna2 = iazluna - 0.5*deltaz
            else:
                iazluna2 = iazluna + 0.5*deltaz
            o.horizon = horizonte[int(iazluna2)]*np.pi/180. # Encuentra para ese acimut cuan alto es el horizonte y lo incorpora a los calculos
            l.compute(o) # calcula datos lunares nuevamente a la salida en horizonte nuevo, pero buscando la hora de puesta
            try:
                o.date = l.set_time
            except:
                o.date = o.date - 24*hour
                l.compute(o)
                o.date = l.set_time
            l.compute(o)
            iazluna = l.az * 180/np.pi
            deltaz = l.az*180/np.pi - iazluna2
#######################################

        print "Acimut puesta = ", l.az
        print "Altura del horizonte Oeste= ", o.horizon

        self.mensaje(fig2, ax2, canvas2, msj0, msj1, msj2, msj3, msj4, msj5, msj6)
        filelines = filelines + "                      " + str(int(l.az*10*180/np.pi)/10.)+"\n"

                # Imprime los resultados en un archivo externo
        fout.write(filelinen)
        fout.write(filelines)

    def decsvenus(self):

        global fout2
        v = Venus()
        o = Observer()
        o.lat = global_lugar.lat
        o.lon = global_lugar.lon
        o.date = global_lugar.date
        o.epoch = o.date
        maxforton = 0.
        maxfortos = 0.
        maxfocason = 0.
        maxfocasos = 0.
        maxazorton = 90.
        maxazortos = 90.
        maxazocason = 270.
        maxazocasos = 270.
        horizonte = self.horizon(float(global_lugar.lat)*180./np.pi, -float(global_lugar.long)*180./np.pi) # Calcula el horizonte local
        i = 1
        while i < 584*5:

            v.compute(o)
            try:
                o.date = v.rise_time
            except:
                o.date = o.date - 24*hour
                v.compute(o)
                o.date = v.rise_time
            v.compute(o)
################# Hace las correcciones necesarias para calcular caracteristicas venusianas segun horizonte local
            iazvenus = v.az * 180/np.pi   # Toma el dato del acimut del orto de Venus
            deltaz = horizonte[int(iazvenus)]/tan(np.pi/2 - o.lat)
            while deltaz > 1.0:
                if  o.lat >= 0.:
                    iazvenus2 = iazvenus + 0.5*deltaz
                else:
                    iazvenus2 = iazvenus - 0.5*deltaz
                o.horizon = horizonte[int(iazvenus2)]*np.pi/180. # Encuentra para ese acimut altura del horizonte e incorpora a calculos
                v.compute(o) # calcula datos venusianos nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
                try:
                    o.date = v.rise_time
                except:
                    o.date = o.date - 24*hour
                    v.compute(o)
                    o.date = v.rise_time
                v.compute(o)
                iazvenus = v.az * 180/np.pi
                deltaz = v.az*180/np.pi - iazvenus2
#######################################
            if float(v.az)*180 / np.pi < maxazorton:
                maxazorton = float(v.az)*180 / np.pi
                maxforton = v.rise_time
            if float(v.az)*180 / np.pi > maxazortos:
                maxazortos = float(v.az)*180 / np.pi
                maxfortos = v.rise_time

            try:
                o.date = v.set_time
            except:
                o.date = o.date + 48*hour
                v.compute(o)
                o.date = v.set_time
            v.compute(o)
################# Hace las correcciones necesarias para calcular caracteristicas venusianas segun horizonte local
            iazvenus = v.az * 180/np.pi   # Toma el dato del acimut del orto de Venus
            deltaz = horizonte[int(iazvenus)]/tan(np.pi/2 - o.lat)
            while deltaz > 1.0:
                if  o.lat >= 0.:
                    iazvenus2 = iazvenus - 0.5*deltaz
                else:
                    iazvenus2 = iazvenus + 0.5*deltaz
                o.horizon = horizonte[int(iazvenus2)]*np.pi/180. # Encuentra para ese acimut altura del horizonte e incorpora a calculos
                v.compute(o) # calcula datos venusianos nuevamente a la salida en horizonte nuevo, pero buscando la hora de orto
                try:
                    o.date = v.set_time
                except:
                    o.date = o.date - 24*hour
                    v.compute(o)
                    o.date = v.set_time
                v.compute(o)
                iazvenus = v.az * 180/np.pi
                deltaz = v.az*180/np.pi - iazvenus2
#######################################
            if float(v.az)*180 / np.pi > maxazocason:
                maxazocason = float(v.az)*180 / np.pi
                maxfocason = v.set_time
            if float(v.az)*180 / np.pi < maxazocasos:
                maxazocasos = float(v.az)*180 / np.pi
                maxfocasos = v.set_time

            o.date = o.date + 48*hour
            i += 2

                # Construye la linea a imprimir en el archivo externo
                
        fileline = str(maxforton) + "    " + str(int(maxazorton*10.)/10.) + "     " +str(maxfortos) + "    " + str(int(maxazortos*10.)/10.) + "     " + str(maxfocason) + "    " + str(int(maxazocason*10.)/10.) + "     " +str(maxfocasos) + "    " + str(int(maxazocasos*10.)/10.) + "\n"

        print "Resultados:"
        print "Maximo Orto Norte              Maximo orto Sur            Maximo ocaso norte         Maximo ocaso Sur\n"
        print fileline

        msj0 = "      DECLINACIONES EXTREMAS DEL PLANETA VENUS"
        msj1 = " "
        msj2 = "      Maximo Orto Norte                     Maximo orto Sur"
        msj3 = str(maxforton) + "    " + str(int(maxazorton*10.)/10.) + "       " +str(maxfortos) + "    " + str(int(maxazortos*10.)/10.)
        msj4 = " "
        msj5 = "      Maximo ocaso norte                    Maximo ocaso Sur"
        msj6 =str(maxfocason) + "    " + str(int(maxazocason*10.)/10.) + "       " +str(maxfocasos) + "    " + str(int(maxazocasos*10.)/10.)
        self.mensaje(fig2, ax2, canvas2, msj0, msj1, msj2, msj3, msj4, msj5, msj6)

        # Imprime los resultados en un archivo externo
        fout2.write(fileline)

    def graficar(self, n_cuerpoc,fig, ax, canvas):

        global aci
        print "Acimut de evaluacion al inicio de grafica", aci

        color_cielo = '#FFFFFF'
        color_tierra = '#BFBFBF'
        color_linea = '#808080'

        ax.clear()
        ax.set_axis_off()

        # Graduacion de alturas entre 0 y 90 grados
        q1=patches.Circle(xy=(0.5,0.5),radius=0.21, color = color_tierra, fill=True, fc = color_tierra)
        q2=patches.Circle(xy=(0.5,0.5),radius=0.252318, color = color_tierra, fill = False) 
        q3=patches.Circle(xy=(0.5,0.5),radius=0.293973, color = color_tierra, fill = False)
        q4=patches.Circle(xy=(0.5,0.5),radius=0.334229, color = color_tierra, fill = False)
        q5=patches.Circle(xy=(0.5,0.5),radius=0.372204, color = color_tierra, fill = False)
        q6=patches.Circle(xy=(0.5,0.5),radius=0.406787, color = color_tierra, fill = False)
        q7=patches.Circle(xy=(0.5,0.5),radius=0.436567, color = color_tierra, fill = False)
        q8=patches.Circle(xy=(0.5,0.5),radius=0.459847, color = color_tierra, fill = False)
        q9=patches.Circle(xy=(0.5,0.5),radius=0.474816, color = color_tierra, fill = False)
        q10=patches.Circle(xy=(0.5,0.5),radius=0.48, color = color_tierra, fill = True, fc = color_cielo)

        # Graduacion de alturas entre 1 y 9 grados
        q13=patches.Circle(xy=(0.5,0.5),radius=0.2142, color = color_tierra, fill = False) 
        q14=patches.Circle(xy=(0.5,0.5),radius=0.2185, color = color_tierra, fill = False)
        q15=patches.Circle(xy=(0.5,0.5),radius=0.2227, color = color_tierra, fill = False) 
        q16=patches.Circle(xy=(0.5,0.5),radius=0.2270, color = color_tierra, fill = False)
        q17=patches.Circle(xy=(0.5,0.5),radius=0.2312, color = color_tierra, fill = False)
        q18=patches.Circle(xy=(0.5,0.5),radius=0.2354, color = color_tierra, fill = False)
        q19=patches.Circle(xy=(0.5,0.5),radius=0.2397, color = color_tierra, fill = False)
        q20=patches.Circle(xy=(0.5,0.5),radius=0.2439, color = color_tierra, fill = False)
        q21=patches.Circle(xy=(0.5,0.5),radius=0.2481, color = color_tierra, fill = False)

        ax.add_patch(q10)
        ax.add_patch(q9)
        ax.add_patch(q8)
        ax.add_patch(q7)
        ax.add_patch(q6)
        ax.add_patch(q5)
        ax.add_patch(q4)
        ax.add_patch(q3)
        ax.add_patch(q2)
        ax.add_patch(q1)

        ax.add_patch(q13)
        ax.add_patch(q14)
        ax.add_patch(q15)
        ax.add_patch(q16)
        ax.add_patch(q17)
        ax.add_patch(q18)
        ax.add_patch(q19)
        ax.add_patch(q20)
        ax.add_patch(q21)

        ax.set_aspect('equal')

                ############# TRAZA LINEAS Y VALORES DE GRADUACION DE ACIMUT EN EL AREA DEL CIELO ##################
        i = 0.0
        alin_hor = ['center','center']
        alin_ver = ['bottom', 'top']
        while i < 180.0:
            xacimutg = [0.0, 0.0]
            yacimutg = [0.0, 0.0]
            if aci < 180.0:
                acimut2 = float(i) + 180.0
            else:
                acimut2 = float(i) - 180.0
            xacimutg[0] = 0.5 + (sin(float(i) * np.pi / 180.0)*(0.21+0.27*acos((cos(1.5708))**2)/(np.pi/2)))
            yacimutg[0] = 0.5 + (cos(float(i) * np.pi / 180.0)*(0.21+0.27*acos((cos(1.5708))**2)/(np.pi/2)))
            xacimutg[1] = 0.5 + (sin(acimut2*np.pi/180.0) * (0.21 + 0.27*acos((cos(1.5708))**2)/(np.pi/2)))
            yacimutg[1] = 0.5 + (cos(acimut2*np.pi/180.0) * (0.21 + 0.27*acos((cos(1.5708))**2)/(np.pi/2)))
            line, = ax.plot(xacimutg, yacimutg, lw = 1, color = color_tierra , zorder = 1)

                ################ ESCRIBE LA ROTULACION DEL GRAFICO MOSTRADO ####################
                ####################### EMPIEZA CON ACIMUT Y ALTURAS ########################
            if (i / 10.0) % 2 == 0:
                alin_vert = 0.71 + (0.27 * acos((cos(i * np.pi / 360.))**2) / (np.pi / 2))
                ax.text(0.5, alin_vert, int(i/2.),
                horizontalalignment = 'left',
                verticalalignment = 'center',
                fontsize = 6, color = color_linea,
                transform = ax.transAxes)

                alin_vert = 0.29 - (0.27 * acos((cos(i * np.pi / 360.))**2) / (np.pi / 2))
                ax.text(0.5, alin_vert, int(i/2.),
                horizontalalignment = 'right',
                verticalalignment = 'center',
                fontsize = 6, color = color_linea,
                transform = ax.transAxes)

            ax.text(xacimutg[0],yacimutg[0], int(i),
            horizontalalignment = alin_hor[0],
            verticalalignment = alin_ver[0],
            fontsize = 8, color = color_linea,
            transform = ax.transAxes)

            ax.text(xacimutg[1],yacimutg[1], int(i+180),
            horizontalalignment = alin_hor[1],
            verticalalignment = alin_ver[1],
            fontsize = 8, color = color_linea,
            transform = ax.transAxes)

            if i == 0.0:
                alin_hor = ['left', 'right']
                alin_ver = ['center', 'center']

            i += 10.0

                ################ ROTULA LOS PUNTOS CARDINALES #######################
        ax.text(0.5,0.71, 'N',
            horizontalalignment='center',
            verticalalignment='top',
            fontsize=12, color='black',
            transform=ax.transAxes)
        ax.text(0.5,0.29, 'S',
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize=12, color='black',
            transform=ax.transAxes)
        ax.text(0.71,0.48, 'E',
            horizontalalignment='right',
            verticalalignment='bottom',
            fontsize=12, color='black',
            transform=ax.transAxes)
        ax.text(0.29,0.48, 'W',
            horizontalalignment='left',
            verticalalignment='bottom',
            fontsize=12, color='black',
            transform=ax.transAxes)

        line, = ax.plot([0.5], [0.5]) # empty line

        horizonte = self.horizon(float(global_lugar.lat)*180./np.pi, -float(global_lugar.long)*180./np.pi) # Calcula el horizonte local

        # Llama y asigna las funciones para cuerpos astronomicos
        if n_cuerpoc == "Sol":
            cuerpoc = Sun()

        if n_cuerpoc == "Luna":
            cuerpoc = Moon()

        if n_cuerpoc == "Venus":
            cuerpoc = Venus()

        cuerpoc.compute(global_lugar)   # Calcula efemérides del Cuerpo celeste para el lugar
                                        # del observador y fecha/hora/época seleccionadas
        a=0.09                          # Intervalo de tiempo entre puntos a graficar (minutos)
        k_cuerpoc_sale=cuerpoc.rise_time        # Define como inicio de los cálculos para el cuerpo astronomico,
        k_cuerpoc_puesta=cuerpoc.set_time       # la hora de su salida, en la fecha del dí­a seleccionado y asigna
                                                # horas de salida y puesta a constantes

        if not(k_cuerpoc_sale):     # Correcciones para cuando no hay salida de Cuerpo celeste
            print "No hay salida de",n_cuerpoc," en este día... corrigiendo hacia salida del día anterior"
            vp=global_lugar
            vp.date-=hour*24
            cuerpoc.compute(vp)
            k_cuerpoc_sale=cuerpoc.rise_time
            vp.date+=hour*24

        if not(k_cuerpoc_puesta):  # Correcciones para cuando no hay puesta de Cuerpo celeste
            print "No hay puesta de",n_cuerpoc," en este día... corrigiendo hacia puesta del día siguiente"
            vp = global_lugar
            vp.date += hour*24
            cuerpoc.compute(vp)
            k_cuerpoc_sale = cuerpoc.rise_time
            vp.date -= hour*24

        if not(k_cuerpoc_sale):
            print "No hay salida ni puesta de",n_cuerpoc,", tomando fecha originalmente ingresada:", date(global_lugar.date)
            k_cuerpoc_sale = global_lugar.date
            k_cuerpoc_puesta = global_lugar.date
        else:
            global_lugar.date = date(k_cuerpoc_sale)

        vp = global_lugar
        k_pi = 3.141592654

        if k_cuerpoc_puesta<k_cuerpoc_sale:  # Corrección para puesta del Cuerpo celeste ANTES de la salida
            vp.date += hour*24
            cuerpoc.compute(vp)
            k_cuerpoc_puesta = cuerpoc.set_time
            vp.date -= hour*24

        lugarc = Observer()
        lugarc.long, lugarc.lat = global_lugar.long, global_lugar.lat
        lugarc.date, lugarc.epoch = k_cuerpoc_sale, global_lugar.epoch
        iteracion = 0

        intervalo_cuerpoc = 1/(1 + (k_cuerpoc_puesta - k_cuerpoc_sale)/(minute*a)) #Cantidad de intervalos a utilizar

        if k_cuerpoc_sale==k_cuerpoc_puesta:
            print "No se puede hacer trazo para",n_cuerpoc
            print k_cuerpoc_sale, k_cuerpoc_puesta

        rotulo_cuerpoc=int((1/intervalo_cuerpoc)*3/4)   # Prepara variables con Numero de elementos del arreglo
                                                        # que se usará para colocar rotulador de cada objeto

        xcuerpoc=np.arange(0,1,intervalo_cuerpoc) # Crea los arreglos donde se guardarán las coordenadas que sigue
        ycuerpoc=np.arange(0,1,intervalo_cuerpoc) # el cuerpo celeste, según la cantidad de intervalos requeridos,

        ################### CALCULOS PARA EL CUERPO CELESTE ####################
        while lugarc.date <= k_cuerpoc_puesta:
            cuerpoc.compute(lugarc)
            xcuerpoc[iteracion] = 0.5 + (sin(cuerpoc.az)*(0.21+0.27*acos((cos(cuerpoc.alt))**2)/(np.pi/2)))
            ycuerpoc[iteracion] = 0.5 + (cos(cuerpoc.az)*(0.21+0.27*acos((cos(cuerpoc.alt))**2)/(np.pi/2)))
            if iteracion == 0:
                print " "
                print "Epoca:", lugarc.epoch
                print "Salida de "+n_cuerpoc
                print iteracion, date(lugarc.date), cuerpoc.alt, cuerpoc.az # Imprime datos en salida
                print "Declinacion de "+n_cuerpoc+":", cuerpoc.dec
            lugarc.date += a / (24 * 60)
            iteracion += 1

        print " "
        print "Puesta de "+n_cuerpoc
        print iteracion,date(lugarc.date),cuerpoc.alt, cuerpoc.az # Imprime datos en puesta
        print " "

        try: # Corrección para que el último punto a graficar no salga fuera del Histograma
            xcuerpoc[iteracion] = 0.5 + (sin(cuerpoc.az)*(0.21+0.27*acos((cos(cuerpoc.alt))**2)/(np.pi/2))) 
            ycuerpoc[iteracion] = 0.5 + (cos(cuerpoc.az)*(0.21+0.27*acos((cos(cuerpoc.alt))**2)/(np.pi/2)))
        except:
            print "No se pudo hacer corrección para último pto. a graficar"

        print n_cuerpoc+" culmina a las: "+str(lugarc.previous_transit(cuerpoc))+" (UT)" # Imprime datos en el meridiano
        x_rotulo_cuerpoc = xcuerpoc[rotulo_cuerpoc]
        y_rotulo_cuerpoc = ycuerpoc[rotulo_cuerpoc]
                ####################### FIN CALCULOS PARA EL CUERPO CELESTE #########################

                ####################### CALCULOS PARA LINEA ACIMUTAL A COMPARAR #################

        acimut2 = 0.0
        print "Acimut a evaluar:", float(aci)
        xacimut = [0.0, 0.0]
        yacimut = [0.0, 0.0]
        if aci < 180.0:
            acimut2 = float(aci) + 180.0
        else:
            acimut2 = float(aci) - 180.0

        xacimut[0] = 0.5 + (sin(float(aci) * np.pi / 180.0)*(0.21+0.27*acos((cos(0.349066))**2)/(np.pi/2)))
        yacimut[0] = 0.5 + (cos(float(aci) * np.pi / 180.0)*(0.21+0.27*acos((cos(0.349066))**2)/(np.pi/2)))
        xacimut[1] = 0.5 + (sin(acimut2*np.pi/180.0) * (0.21 + 0.27*acos((cos(0.349066))**2)/(np.pi/2)))
        yacimut[1] = 0.5 + (cos(acimut2*np.pi/180.0) * (0.21 + 0.27*acos((cos(0.349066))**2)/(np.pi/2)))

                ##################### FIN CALCULOS PARA ACIMUT ####################################

        line, = ax.plot(xcuerpoc, ycuerpoc, lw = 1, color = color_linea, zorder = 1) # Hace trazo del Cuerpo en el histograma
        line, = ax.plot(xacimut, yacimut, lw = 1, color = color_linea, zorder = 3) # traza línea acimutal en histograma
        th = 0.
        xhor = []
        yhor = []
        print len(horizonte)
        while th < 360.:
            xhor.append(0.5 + sin(th * np.pi / 180.0)*(0.21 + 0.27*acos((cos(horizonte[int(th)] * np.pi / 180.0))**2)/(np.pi/2)))
            yhor.append(0.5 + cos(th * np.pi / 180.0)*(0.21 + 0.27*acos((cos(horizonte[int(th)] * np.pi / 180.0))**2)/(np.pi/2)))
            th += 1.

        line, = ax.plot(xhor, yhor, lw = 1, color = color_linea, zorder = 3) # traza línea del horizonte local

                ############ ROTULA DATOS DEL OBJETO OBSERVADO Y HORAS, ETC. #######################
        ax.text(xcuerpoc[rotulo_cuerpoc],ycuerpoc[rotulo_cuerpoc], n_cuerpoc,
            horizontalalignment='right',
            verticalalignment='bottom',
            fontsize=12, color='black' ,
            transform=ax.transAxes)

        ax.text(-0.13,0.96, 'Salida de '+n_cuerpoc+': '+str(k_cuerpoc_sale)+' (UT)',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=7.5, color='black',
            transform=ax.transAxes)

        lugarc.date = k_cuerpoc_sale
        ax.text(-0.13,0.94, 'Cruza el meridiano: '+str(lugarc.next_transit(cuerpoc))+"(UT)",
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=7.5, color='black',
            transform=ax.transAxes)

        ax.text(-0.13,0.92, 'Altura max. s/horizonte: '+str(cuerpoc.alt),
            horizontalalignment = 'left',
            verticalalignment = 'top',
            fontsize = 7.5, color = 'black',
            transform = ax.transAxes)

        ax.text(-0.13,0.98, 'Lat:'+str(global_lugar.lat)+', Lon:'+str(global_lugar.long),
            horizontalalignment = 'left',
            verticalalignment = 'top',
            fontsize = 7.5, color = 'black',
            transform = ax.transAxes)

        ax.text(-0.13,0.90, 'Acimut evaluado:' + str(aci),
            horizontalalignment = 'left',
            verticalalignment = 'top',
            fontsize = 7.5, color='black',
            transform = ax.transAxes)

        ax.text(0.5,0.5, str(aci),
            horizontalalignment = 'center',
            verticalalignment = 'top',
            fontsize = 7.5, color = color_linea,
            transform = ax.transAxes)

        canvas.draw()

    def graficar_a(self, event, n_cuerpoc, fig, ax, canvas, aci):
        self.graficar(n_cuerpoc, fig, ax, canvas, aci) 

    def horizon(self,la,lo):

        # Construye el nombre del archivo correspondiente, segun las coordenadas ingresadas
        cla = str(int(la))
        clo = str(int(lo+1.))
        nomarch = "N"+cla+"W0"+clo+"c.asc"

                # Localiza dentro del archivo, la posicion de las coordenadas que se ingresaron
        dla = la - int(la)
        dlo = lo - int(lo)
        fila_la = int((1 - dla) * 1200)
        col_lo = int((1 - dlo)*1200)
        print nomarch
        try:
            fhand = open (nomarch)
        except:
            self.v_aviso(u"Coordenadas no est\u00E1n en la Base de Datos\nSe usar\u00E1 horizonte ideal",u"\u00A1AVISO!")
            i = 0
            hor = []
            while i <= 360:
                hor.append(0)
                i += 1
            return hor
        x = []

                # Define la distancia del horizonte ideal
        dhor = 6371000 * acos(6371/(6371+(global_lugar.elevation/1000.)))
#        print "Distancia al horizonte: ",dhor
        if dhor < 5000.:
            dhor_pix = 180     # dhor_pix = 180 entonces dhor/1000 = 16.2 kms
        else:
            dhor_pix = int(dhor/90)

        # Define el horizonte ideal a una distancia de dhor_pix cuadros (o sea a dhor/1000 kms de distancia)
        fila_0 = fila_la - dhor_pix
        fila_f = fila_la + dhor_pix
#        print fila_0, fila_f
        if fila_0 < 0:
            fila_0 = 0
        if fila_f > 1200:
            fila_f = 1200
        deltaf0 = abs(fila_la - fila_0)
        deltaff = abs(fila_f - fila_la)
        maxtop = float(deltaf0)
        maxbott = float(deltaff)

        col_0 = col_lo - dhor_pix
        col_f = col_lo + dhor_pix
        if col_0 < 0:
            col_0 = 0
        if col_f > 1200:
            col_f = 1200
        deltac0 = abs(col_lo - col_0)
        deltacf = abs(col_lo - col_f)
        maxder = float(deltacf)
        maxizq = float(deltac0)

        esqsupder = atan(maxder/maxtop) * 180./pi
        esqinfder = 180. - atan(maxder/maxbott) * 180./pi
        esqinfizq = 180. + atan(maxizq/maxbott) * 180./pi
        esqsupizq = 360. - atan(maxizq/maxtop) * 180./pi

        # Carga de la base de datos las filas y columnas dentro del horizonte ideal calculado
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
#        print "Altura del sitio origen=", x[deltaf0][deltac0]

        while th <= 360:

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
                i = 0
                while abs(y0+i) <= abs(ym):
                    coordx = (xc-1)*factorx + deltac0
                    coordy = deltaf0-(y0+i)
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
                    if amax < althor:
                        amax = althor
                    i += 1*factory

            hor.append(amax)
        return hor

#**********************************************************************************************************************************
root = Tk()

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root_xpos=int((screen_width*0.11))
root_ypos=int((screen_height*0.05))
root.title("Chan U'Bih")
rootWindowPosition="+" + str(root_xpos) + "+" + str(root_ypos)
root.geometry(rootWindowPosition)

myapp = Chanubih(root,screen_width,screen_height)
root.mainloop()
