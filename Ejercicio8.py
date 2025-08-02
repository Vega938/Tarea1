#Alan HHumberto Vega Millan 
#Ejercicio 8

Vocal=input("Ingrese una vocal\n").capitalize()

if Vocal in ["A","E","O"]: 
    print("Tu vocal es Abierta")

elif Vocal in ["I","U"]:
    print("Tu vocal es cerrada")

else:
    print("Dato invalido") 
