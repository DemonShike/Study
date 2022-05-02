


cantantes = ["2pac", "Drake", "Bad Bunny", "Julio Iglesias" ]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar
#print(numeros)
numeros.sort() #con sort , se pueden ordenar numericamente las listas de numeros xd
#print(numeros)

# Añadir elementos

cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal") #con este comando a diferencia de append que sirve para agregar elementos a la lista,este tambien lo hace pero debes indicarle si o si,en que parte de la lista lo colocaras
#print(cantantes)

# Eliminar elementos
cantantes.pop(1)   #aqui se elige el numero de cual eliminar
cantantes.remove("Bad Bunny") #y aqui se elimina por su nombre exacto
#print(cantantes)

# Dar la vuelta
print(numeros)
numeros.reverse()  #este comando hace lo que dice,muestra la lista pero alrevez 
print(numeros) 

# Buscar dentro de una lista
print("Drake" in cantantes)  #este es un buscador de listas,poner el nombre del elemento,seguido del definido in,y luego la lista donde crees que esta,y dara true o false dependiendo si esta o no

# contar elementos
print(len(cantantes)) #aqui se pueden contar cuantas variables hay en una lista


# cuantas veces aparece un elemento 

print(numeros.count(8)) # este comando te dice cuantos elementos del que elijas hay en una lista 

# Conseguir indice
print(cantantes.index("Drake")) # esto te muestra el indice en el que esta el elemento que pidas

# Unir listas 
cantantes.extend(numeros) #aqui primero se pone la lista principal y con extend se agrega entre los parentesis la lista que queremos agregar a la principal,une una lista al lado de la otra

print(cantantes)