#Alan Humberto Vega Millan 250169
#Else 

num1=float(input("Ingrese el primer numero"))
num2=float(input("Ingrese el segundo numero"))
num3=float(input("Ingrese el tercer numero"))



#si num1 es mayor o igual que num2 y num1 es mayor o igual que num3
if num1>=num2 and num1 >= num3:
   mayor=num1  

#si num2 es mayor o igual que num1 y num2 es mayor o igual que num3
elif num2>= num1 and num2 >= num3:
   mayor=num2

#si ninguna de las condiciones anteriores es verdadera, num3 es el mayor 
else:
   mayor = num3 

#Imprimir el numero mayor 
print(f"El numero es {mayor}")

   