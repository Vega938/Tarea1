#Alan Humberto Vega Millan 250169
#Else 



numero = int(input("Ingresa un número entre 1 y 999: "))

if numero < 1 or numero > 999:
    print("El número está fuera del rango (1-999).")
elif numero < 10:
    # Número de una cifra, se queda igual al invertirlo
    print("Número invertido:", numero)
elif numero < 100:
    # Número de dos cifras
    decenas = numero // 10
    unidades = numero % 10
    numero_invertido = unidades * 10 + decenas
    print("Número invertido:", numero_invertido)
else:
    # Número de tres cifras
    centenas = numero // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10
    numero_invertido = unidades * 100 + decenas * 10 + centenas
    print("Número invertido:", numero_invertido)