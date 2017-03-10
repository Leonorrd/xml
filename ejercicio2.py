#!/usr/bin/python
# -*- coding: utf-8 -*-

#Muestra el nombre da cada partido y el número de electos de cada uno.


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
    print "Número de electos por partido"
    respuesta = raw_input("ejercicio: ")
    
    #Comprobador de respuesta
    if respuesta == "3":
    	salir = True

    elif respuesta == "2":
        os.system('clear')
        
    	print "Número de electos por partido"
        
        hojas =arbol.xpath('/escrutinio_sitio/resultados/partido')
        
        #print hojas
        
        for h in hojas:
            print "Partido: " , h[1].text,"Electos:",h[2].text
            
        raw_input("Pulse enter para continuar")

 
