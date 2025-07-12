#Alan Humberto Vega Millan 250169
#sumas basicas 


#define variables 
CEM=float (input("Ingrese calificacion de examen de matematicas, perro"))
CTM=int (input("Ingrese las tareas realizadas"))
CEF=float (input("Ingrese calificacion de examen de física"))
CTF=int (input("Ingrese las tareas realizadas"))
CEQ=float (input("Ingrese calificacion de examen de química"))
CTQ=int (input("Ingrese las tareas realizadas"))

#proceso 
CEMP=CEM*9
CTMP=(CTM*10)/3 
CEFP=CEF*8
CTFP=(CTF*20)/2 
CEQP=CEQ*8.5
CTQP=(CTQ*15)/3 

PM=CEMP+CTMP
PF=CEFP+CTFP
PQ=CEQP+CTQP

#IMPRIMIR 
print(f"Su promedio en matematicas es {PM}")
print(f"Su promedio en fisica es {PF}")
print(f"Su promedio en química es {PQ}")
