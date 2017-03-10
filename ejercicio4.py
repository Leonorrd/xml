#!/usr/bin/python
# -*- coding: utf-8 -*-

#Pide el número de electos y te muestra si hay, los partidos que tienen ese número.


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
    print "Numero de electos "
    respuesta = raw_input("ejercicio: ")

    #Comprobador de respuesta
    if respuesta == "5":
    	salir = True

    elif respuesta == "4":
          os.system('clear')

	  print "Buscador por número de electos"
        
       	  print "Introduzca el número de electos."
          numel = raw_input("Número de electos: ")
          raiz =arbol.getroot()
          hojas = raiz.findall('resultados/partido')
          banpart = False
          lpart = []
          for h in hojas :
              if h.findtext('electos') == numel:
                  lpart.append(h.findtext('nombre'))
                  banpart = True
          if banpart == True:
              print "Partidos con %s electos:" % (numel)
              for l in lpart:
                  print l

          if banpart == False:
              print "Ningun partido tiene ese número de electos"

          raw_input("Pulse enter para continuar")
