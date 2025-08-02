#Alan Humberto Vega Millan 
#Trabajo 20

print("Responde con 'Si' o 'No'.")

respuesta1 = input("Colón descubrió América\n ").strip().capitalize()

if respuesta1 == "Si":
    respuesta2 = input("¿La independencia de México fue en el año 1810?\n ").strip().capitalize()
    
    if respuesta2 == "Si":
        respuesta3 = input("The Doors fue un grupo de rock Americano\n ").strip().capitalize()
        
        if respuesta3 == "Si":
            print("Correctas las tres respuestas. Ganaste.")
        else:
            print("Respuesta incorrecta. Fin del juego.")
    else:
        print("Respuesta incorrecta. Fin del juego.")
else:
    print("Respuesta incorrecta. Fin del juego.")


    

