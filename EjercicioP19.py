#Alan Humberto Vega Millan 
#Trabajo 19

PL=int(input("Ingrese los puntos del día Lunes\n"))
PM=int(input("Ingrese los puntos del día Martes\n"))
PMM=int(input("Ingrese los puntos del día Miercoles\n"))
PJ=int(input("Ingrese los puntos del Jueves\n"))
PV=int(input("Ingrese los puntos del día Viernes\n"))
GD=float(input("Ingrese ganancia diaria\n"))
Sancion=GD*0.50

#puntaje total
PT=PL+PM+PMM+PJ+PV/5

if PT>170:
    print (f"Se paga multa de {Sancion}")
    
