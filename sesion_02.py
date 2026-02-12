# Tuplas 
mi_tupla = (2,4)
print("Mi tupla: ",mi_tupla)

# Lista
mi_lista = [ 1,3.1416,"ingrid",mi_tupla]
print("El primer elemento de mi lista;",mi_lista[0])
print("El cuarto elemento de mi lista;",mi_lista[3])
print("El tercer elemento de mi lista;",mi_lista[2])

# Diccionarios 
mi_diccionario = {"mi-lista": mi_lista,
                  "Nombre": "ingrid",
                   "Pi": 3.1416,                                   "Pi" : 3.1416,
                  "Tel": "664-2334455"}
print("Llave para acceder a mi diccionario mi_lista",mi_diccionario["mi-lista"])
print("Llave para acceder a mi diccionario Pi",mi_diccionario["Pi"])
print("Llave para acceder a mi diccionario Tel",mi_diccionario["Tel"])
