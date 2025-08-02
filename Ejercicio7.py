#Alan Humberto Vega Millan 
#Ejercicio 6


from datetime import date


dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
año = int(input("Año de nacimiento: "))

#Fecha de hoy
hoy = date.today()

#Fecha de nacimiento
nacimiento = date(año, mes, dia)

# Calculamos edad
edad = hoy.year - nacimiento.year

# Si todavía no ha llegado su cumpleaños este año, restamos 1
if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
    edad -= 1

print(f"Tienes {edad} años.")