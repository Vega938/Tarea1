#Alan Humberto Vega Millan 
#Ejercicio14

Sexo=input("Ingrese su sexo biológico (M o F) \n").capitalize 
Edad=int(input("Ingrese su edad\n"))
PTF= (220-Edad)/10
PTM= (210-Edad)/10

if Sexo== "F":
    print(f"Sus pulsaciones por cada 10seg sería: {PTF}")
else:
    print(f"Sus pulsaciones por cada 10seg serían: {PTM}")

