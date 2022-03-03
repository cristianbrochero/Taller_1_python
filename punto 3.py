# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:23:27 2022

@author: Cristian Brochero
"""


v = int (input( "Su salario es: "))
numven = int (input( "La cantidad de ventas realizadas son: "))
com =0.15
final= v + (numven + com*100)
print (f"El salario final del trabajador es de: ${final:,}")





