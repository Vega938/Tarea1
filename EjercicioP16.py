#Alan Humberto Vega Millan 
#Ejercicio12

Promedio=float(input("Ingrese su promedio\n"))
NumM=int(input("Ingrese el número de materias\n"))
IVA=NumM*0.10
CTSD=NumM*800+IVA
CTCD=NumM*0.70

if Promedio >=9:
    print(f"Su nuevo total es de {CTSD}")

else:
    print(f"Su nuevo total es de {CTCD}")
