# 1. Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
# igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá
# devolver ['papa', 'a', 'día', 'buen', 'Di'].
# 2. Realizar otra función que invierta la lista, pero en lugar de devolver una nueva,
# modifique la lista dada para invertirla, sin usar listas auxiliares.

def invertirAux(cadena):
    lista=cadena.split(" ")
    lista2=[]
    longitud = len(lista)
    for i in range(longitud):
      lista2.append(lista[longitud-i-1])
    return " ".join(lista2)

def invertirLista(cadena):
    lista=cadena.split(" ")
    longitud = len(lista)
    for i in range(longitud):
      lista.append(lista[longitud-i-1])
      lista.remove(lista[longitud-i-1])
    return " ".join(lista)
    

cadena=input("Ingese una cadena y se va a devolver al reves.")
print(invertirAux(cadena))
print(invertirLista(cadena))

