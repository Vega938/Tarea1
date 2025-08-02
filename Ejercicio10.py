#Alan Humberto Vega Millan 
#Ejercicio 10



while True: 
    print("Menú:\n") 
    print("N:Nombre de cliente")
    print("D:Dirección")
    print("T:Teléfono")
    print("C:Ciudad")
    print("F:Fin (Salir)")

    Opcion=input("Elija una opción:").strip().upper()

    if Opcion== "N":
        Nombre= input("Ingresa nombre del cliente:")
    elif Opcion== "D":
        Direccion= input("Ingresa la dirección")
    elif Opcion== "T":
        Telefono=input("Ingrese el teléfono")
    elif Opcion== "C":
        Ciudad= input("Ingrese la ciudad")
    elif Opcion== "F":
        print("Gracias. Datos capturados:\n")
        print(f"Nombre: {Nombre}")
        print(f"Dirección: {Direccion}")
        print(f"Telefono: {Telefono}")
        print(f"Ciudad:{Ciudad}")
        break
    else: 
        print("Opción invalida")
        
