#Alan Humberto Vega Millan 
#Ejercicio 10

Num1=float(input("Ingrese número\n"))
Num2=float(input("Ingrese el segundo número\n"))

V=input("Ingresa uno: [+], [-], [*], [/], [%]\n")

if V== "+": 
    print(Num1+Num2)
elif V== "-":
    print(Num1-Num2)
elif V== "*":
    print(Num1*Num2)
elif V == "/":
    print(Num1/Num2)
elif V== "%":
    print(Num1%Num2)
else:
    print("Dato  invalido")

