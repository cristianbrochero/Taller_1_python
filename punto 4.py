# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:50:59 2022

@author: Cristian Brochero
"""

taller1 = float ( input("ingrese la nota de taller 1: ")) 
taller2=float(input("ingrese la nota de taller 2: "))
taller3=float(input("ingrese la nota de taller 3: "))
exam=float(input("ingrese la nota de examen: "))
pf=float(input("ingrese la nota del proyecto final: "))

tal= (taller1 + taller2 + taller3)/3
nofin = (tal * 0.50) + (exam * 0.30) + (pf * 0.20)

print ("la nota final es: ",(nofin))