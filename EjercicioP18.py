#Alan Humberto Vega Millan 
#Ejercicio18

ST=int(input("Ingrese el número de metros cuadrados\n"))
#Porcentaje de arboles en el primer if 
PP= ST*0.70
PO=ST*0.20
PC=ST*.010
#Porcentaje de arboles en el segundo if 
PP2=ST*.50
PO2=ST*0.30
PC2=ST*0.20

#Arboles priemera variable 
NumP=(PP*8)/10
NumO=(PO*15)/15
NumC=(PC*10)/18


#Arboles segunda variable
NumP2=(PP2*8)/10
NumO2=(PO2*15)/15
NumC2=(PC2*10)/18


if ST>= "1000000": 
    print(f"Pinos {NumP}, Oyamel {NumO}, Cedro {NumC}")
    
else:
    print(f"pinos {NumP2}, Oyamel {NumO2}, Cedro {NumC2}")