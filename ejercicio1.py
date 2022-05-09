"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y que haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)

"""



"""

lista = [2, 6, 5, 56, 45, 9, 7, 8]
cuantos_Elementos = (len(lista))



print("***** Mostrando Numeros de la lista *******")

for numeros in lista:  
    print(numeros)

lista.sort()
                                                                          #este es mi ejemeplo,en algun momento me confundi con las funciones y no lograba hacer que el true pasara por el if y me tomara bien los valores de los numeros ingresados,pero despues de volver a intentarlo lo logre
print("****** Mostrando Numeros de menor a mayor ******")

for ordenados in lista:
    print(ordenados)

print(f"**** En esta lista hay: {cuantos_Elementos} elementos")

buscador = int(input("\nQue elemento quieres buscar: "))

def elbuscador(buscador):

    owo = (buscador in lista)

    return owo


indice = lista.index(buscador)

if elbuscador(buscador) == True:
    print(f"El numero {buscador} esta en la lista,en el indice {indice} !!!")   #ademas despues de ver el ejemplo del profesor,puse el numero de indice en el que se encontraba
    
else:
    print(f"El numero {buscador} no esta en la lista")

  #Mi ejemplo me parecio bueno para haberlo hecho todo sin mirar el video practicamente


"""



print("////////////////////////////////////////////////////////////////////////////////////////")




# Crear la lista 
numeros = [12, 64, 52, 73, 21, 7, 91, 63]

# Recorrer y mostrar
print("######### Recorrer y mostrar #######")

def mostrarLista(lista):
        resultado = ""
        
        for elemento in numeros:
            resultado += "Elemento: " + str(elemento)
            resultado += "\n"
        return resultado

print(mostrarLista(numeros))



"""
# Ordenar y mostrar

print("####### Ordenar y Mostrar #######")
numeros.sort()
print(mostrarLista(numeros))


# Mostrar su longitud

print("####### Ordenar y Mostrar #######")

print(len(numeros))

# Busqueda en la lista

print("####### Busqueda en la lista #######")
try:
    busqueda = int(input("Introduce el numero: "))

    comprobar = isinstance(busqueda, int) #este comando se hace para saber si lo ingresado por el usuario es un numero entero lo que esta en parentesis significaria (busqueda, int) "si busqueda es un entero que la guarde en la funcion comprobar"

    while not comprobar or busqueda <= 0 :            #aqui while se usa para que si el numero de comprobar o de busqueda son menores a 0,que el while te vuelve a pedir un numero y asi en bucle hasta que se cumpla la comdicion
        busqueda = int(input("Introduce el numero"))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"#### Buscar en la lista el numero {busqueda} #####")


    search = numeros.index(busqueda)


    print(f"El Numero buscadoe existe en la lista,es el indice: {search}")
except:
    print("El numero elegido no esta en la lista")



"""















"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y que haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)

"""



"""
lista = [3, 5, 6, 7, 97, 34, 54, 56,]

def buscador():
    ingreso = int(input("Que elemento Quieres buscar?: "))
    return ingreso

def mostrador(lista):
    lista_mostrada = ""
    for elemento in lista:
        lista_mostrada += str(elemento)
        lista_mostrada += "\n"
    return lista_mostrada



print("\n#######################")
print("### Mostrando lista ###")
print("#######################")

print(mostrador(lista)
)    
print("\n################################")
print("### Mostrando lista en orden ###")
print("################################")



lista.sort()
print(mostrador(lista))


print("\n################################")
print("###    Longitud de Lista     ###")
print("################################")

print(f"La longitud de la lista es de {len(lista)} indices\n")

indicador = (lista.index(buscador()))


print(f"\nEl numero ingresado esta en el indice {indicador}")

lector = int(input("Ingresa el numero que quieres buscar: "))

comprobador = isinstance(lector, int)

while not comprobador or lector <= 0:
    lector = int(input("Ingresa el numero que quieres buscar: "))
else:
    print(f"Has introducido el  {lector}")


print("\n################################")
print("###Buscador de numeros en lista###")
print("##################################")

uwu = lista.index(lector)

print(f"El numero ingresador esta en el indice {uwu}")



#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18614658#questions

    

"""

