"""Pide un telegrama, el maximo de letras que puede tener cada palabra y los costos de las palabras largas y cortas.
Reemplaza las letras que excedan el maximo ingresado por un "@" y calcula el costo del telegrama""" 

def cortarPalabras(cadena,longMax,costoCorto,costoLargo):
    """Separa la cadena por palabras, remplaza las palabras que excedan el limite y calcula el costo"""
    palabras = cadena.split(" ")
    palabras[-1]=palabras[-1].rstrip(".")
    longPalabras = 0
    shortPalabras = 0  
    frase=""
    for i in range(len(palabras)):
        if len(palabras[i])>longMax:
            frase += palabras[i][0:longMax]+"@" +" "
            longPalabras = longPalabras + 1
        else:
            frase +=palabras[i]+" "
            shortPalabras = shortPalabras + 1
        for letra in palabras[i]:
            if letra== ".":
                frase = f"{frase.strip()}{palabras[i].replace(palabras[i], 'STOP ')}" 
    
   
    frase = frase.strip() + "STOPSTOP"
    costoT = longPalabras*costoLargo + shortPalabras*costoCorto
    return f"El telegrama queda {frase}, y tiene un costo total de {costoT}$ con {longPalabras} palabras largas y {shortPalabras} palabras cortas."

cadena= input("Ingrese el telegrama:\n")
maxLetras= int(input("Ingrese el maximo de letras por palabra: "))
costoC=float(input("Ingrese el costo de las palabras cortas: "))
costoL=float(input("Ingrese el costo de las palabras largas: "))
print(cortarPalabras(cadena, maxLetras, costoC, costoL))