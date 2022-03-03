# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:14:14 2022

@author: Cristian Brochero
"""

don=int( input ("donacion a ingresar $"))
tele= don*0.2
sis= tele*0.15
admin= sis*0.3
Conta= don -(tele + sis + admin)

print (f"la donacion es: ${tele:,}")
print (f"la donacion es: ${sis:,}")
print (f"la donacion es: ${admin:,}")
print (f"la donacion es: ${Conta:,}")


