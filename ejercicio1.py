#!/usr/bin/python
# -*- coding: utf-8 -*-

#1.Lista el número de partidos que aparecen en el escrutinio.

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
    print "Conteo de partidos "
    respuesta = raw_input("ejercicio: ")

    #Comprobador de respuesta
    if respuesta == "2":
    	salir = True

    elif respuesta == "1":
    	os.system('clear')
    	print "Conteo de partidos."
    	hojas = arbol.xpath('/escrutinio_sitio/resultados/partido/nombre')
    	print "El número de partidos que se han presentado es: %i " %(len(hojas))
    	
	raw_input("Pulse enter para continuar")

