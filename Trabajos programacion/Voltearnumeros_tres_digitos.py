#Alan Humberto Vega Millan 250169
#Voltear 3 numeros 

#define variables
n1= float(input("Ingresa un numero de 3 digitos: "))

#Proceso 
n2= n1//100
n3= (n1 % 100)//10
n4= n1 % 10
invert= (n4*100)+(n3*10)+n2

#Imprimir
print(f"Tu numero invertido es: {invert:.0f}")