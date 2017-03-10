#!/usr/bin/python
# -*- coding: utf-8 -*-

#Pide el nombre de un partido y muestra sus datos:nombre, número de electos, ide de partido.

#importación de librerías
#import xpath
import os
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#Carga el fichero xml en una variable
arbol = etree.parse('ficheroxml.xml')

#Bucle del programa
salir = False

while salir == False:
    os.system('clear')
    print "Datos de un partido "
    respuesta = raw_input("ejercicio: ")

    #Comprobador de respuesta
    if respuesta == "4":
    	salir = True

    elif respuesta == "3":
          os.system('clear')
        
          print "Datos  de un partido."
        
          print "Introduzca el nombre del partido:"
          nonpartido = raw_input(":")
          raiz =arbol.getroot()
          hojas = raiz.findall('resultados/partido')
          for h in hojas:
              if h.find('nombre').text == nonpartido :
               
		print "|Código:"+h.findtext('id_partido'), "|Partido: ", h.find('nombre').text, "|Electos: ", h.find('electos').text

                raw_input("Pulse enter para continuar")

