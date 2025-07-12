#Alan Humberto Vega Millan 250169
#Suma y promedio de tres numeros 

#solicitar al usuario que ingrese 3 numeros 
num1 = float (input("ingrese el primer número: "))
num2 = float (input("ingrese el segundo número: "))
num3 = float (input("ingrese el tercer número: "))

#calcular la suma de los numeros 
Suma= num1+num2+num3
prom = Suma/3

#imprimir la suma y el promedio 
print(f"la suma de los numeros es:{Suma}")
print(f"el promedio de los numeros es:{prom:.2f}")

