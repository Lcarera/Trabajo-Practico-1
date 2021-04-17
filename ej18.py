"""Ingresa una cadena que se convierte en una lista y la devuelve revertida"""
def invertirAux(cadena):
  """Convierte la cadena en una lista y la revierte en una lista auxiliar"""
  lista=cadena.split(" ")
  lista2=[]
  longitud = len(lista)
  
  for i in range(longitud):
    lista2.append(lista[longitud-i-1])
  
  return " ".join(lista2)

def invertirLista(cadena):
  """Convierte la cadena en una lista y la revierte
  en si misma sacando las palabras y volviendolas a ingresar"""
  lista=cadena.split(" ")
  longitud = len(lista)
  
  for i in range(longitud):
      lista.append(lista[longitud-i-1])
      lista.remove(lista[longitud-i-1])
  
  return " ".join(lista)
    

cadena=input("Ingese una cadena y se va a devolver al reves.")
print(invertirAux(cadena))
print(invertirLista(cadena))

