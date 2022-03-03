# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:52:14 2022

@author: cristian Brochero
"""

r = int ( input("ingrese la cantidad de alumnos de redes: "))
c = int ( input("ingrese la cantidad de alumnos de contabilidad: "))
d = int ( input("ingrese la la cantidad de alumnos de diseño: "))


por= (r + c + d)

print("Porcentaje alumnos de redes es: ", ((r/por)*100))
print("Porcentaje alumnos de contabilidad es:", ((c/por)*100))
print("Porcentaje alumnos de diseño es:", ((d/por)*100))
