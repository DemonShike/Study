"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longiud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""


"""
lista = []

contador = 1
owo = 0

while contador <= 120:
    owo = 1 + owo
    lista.append(owo)                                                                    #Mi ejemplo de programa que añade valores,con while,este lo que hace es un contador que suma un numero a la lista,como no me gustaba que  el numero se repitiera hice que despues de cada vuelta ese numero valiera 1 mas
    contador += 1

    
for numeros in lista:
        print(numeros)

"""
"""

print("////////////////////////////////////////////////////////////////////////////////////////////////")

lista2 = []


for numeros in range (1,120):
    lista2.append(numeros)                                                                  # Mi ejemplo usando solo el bucle while me costo bastante menos y me inspire bastante en el while

    
for cantidad in lista2:
    print(cantidad)


print("////////////////////////////////////////////////////////////////////////////////////////////////")

coleccion = []

for contador in range(0, 120):
    coleccion.append(f"Elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])                                            # Este ejemplo del profesor es interesante,por que aqui muestra visualmente el contador iterar con un texto,mientras que mi ejemplo lo hacia  iterar pero sin texto, no contemple lo visual


print(coleccion)   #habia olvidado que simplemente podia hacer print y el nombre de la lista para mostrarlo

print("////////////////////////////////////////////////////////////////////////////////////////////////")


coleccion = []
x = 0

while x <= 120:
    coleccion.append(f"elemento-{x}")
    print("Mostrando el: " + coleccion[x])                                            # Este ejemplo con while es interesante,suma los textos,y el contador para dar sentido visual.

    x += 1

print(coleccion[77])


































"""


"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longiud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""

lista = []
contador = 0

while contador <= 119:
    
    valor = contador + 1
    lista.append(valor)
    contador += 1

    


for listado in lista:
    print(listado)
    






#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18616762#overview