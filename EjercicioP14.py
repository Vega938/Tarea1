#Alan Humberto Vega Millan 
#Ejercicio12

NA=int(input("Ingrese un número al alzar\n"))
PT=float(input("Ingrese el precio total\n"))
PTA=PT*0.80
PTB=PT*0.85

if NA<=74:
    print(f"Su nuevo total es de {PTB}")
else:
    print(f"Su nuevo total es de {PTA}")