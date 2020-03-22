print("Este programa invierte las cifras de un numero entero")
print("El numero es introducido por el usuario :D ")

num = input("Escribe un digito: ")
numInv = ""

for i in range(len(num)):
    k = i+1
    numInv = numInv+num[-k]
    
print(f"El numero {num} escrito al reves es {numInv}")
print("ola k ase?")
    