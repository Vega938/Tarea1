#Alan Humberto Vega Millan 250169
#Signos opuestos 

#define variables 
Calif=float(input("Ingrese su calificación\n"))

if Calif< 11:
    print("Insuficinete")

elif Calif >=12 and Calif<=13:
    print("Regular")

elif Calif>=14 and Calif<=15:
    print("Buena")

elif Calif>=16 and Calif<=18:
    print("Muy Buena")

elif Calif >18 and Calif <=20:
    print("Sobresaliente")

else:
    print("Dato no aplica")