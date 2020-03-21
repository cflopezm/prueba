# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:21:01 2020

@author: Fabian Lopez
"""

print("Este programa invierte las cifras de un numero entero")

num = input("Escribe un digito: ")
numInv = ""

for i in range(len(num)):
    k = i+1
    numInv = numInv+num[-k]
    
print(f"El numero {num} escrito al reves es {numInv}")
    