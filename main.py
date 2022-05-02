"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico 
nombre.
Para acceder a esos valores podemos usar un indice numero.


Una lista es una variable que dentro puede contener muchas variables que pueden contener un conjunto de datos
"""



pelicula = "Batman"   #variable normal

#Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]   #esto es una lista,todo lo que se ponga entre los corchetes seran los diferentes elementos de la lista
                                                                  #al ejecutarlos se muestran todas las variables y estos van por indice numero,es decir 0 1 2 3 ,etc
cantantes = list(("2pac", "Drake", "jennifer Lopez"))    #esta es otra forma de hacer una lista ,solo que aqui los elementos no se pueden modificar,se crea una tupla,que uan tupla son  datos dentro de un parentesis que iran dentro del parentesis de "list" y no son modificables
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4 ,True, "Texto"]  #incluso en una lista se pueden poner diferentes tipos de datos
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""


# Indices  #es una forma de acceder a los elementos dentro de las listas
pelicula = "otra cosa"

peliculas[1] = "Gran torino"#de esta manera se le puede cambiar el valor a uno o varios valores que estan dentro de una lista eligiendo el numero del elemento y su nueva variante
peliculas[2] = "El hobbit"  #se suele utilizar para sacar indices o actualizarlos 


print(peliculas[1])    #al poner peliculas que es la lista,y elegir entre corchetes el numero del dato dentro de la lista sale solo el dato pedido
print(peliculas[-2])   #al usar el indice en negativo en vez de buscar de izquierda a derecha cuenta de derecha a izquierda
print(cantantes[1:3])  #esta es una forma para sacar elementos de cual a cual numero va a ir sacandolos
print(peliculas[1:])   #al no poner nada despues del 1,esto va a sacar todos los elementos que hay en la lista a partir de 1

# Añadir elementos a una lista
cantantes.append("Kase o")
cantantes.append("Natos y waor") #al poner el nombre de la lista seguida de .append y poner entre parentesis la nueva variable,esta se agrega a la lista
print(cantantes)

# Recorrer lista

"""
nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ") #esto lo comente para que no estorbe
    
    if nueva_pelicula != "parar":    #este if se agrega para que no muestre para dentro del listado de peliculas
        peliculas.append(nueva_pelicula)                            #este comando lo que hace es un contador while que nos va a pedir datos hasta que le demos la orden de que pare,y los datos tomados los pondra en la lista de peliculas que elegimos mas abajo con el comando append


print("\n*******LISTADO PELICULAS*******")

for pelicula in peliculas:         #este comando lo que hace es guardar las variables que estan en la lista peliculas,dentro de la variable del for llamada peliculas,al darle print peliculas,muestra el contenido de lista uno debajo de otro
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")      #al hacer peliculas.index y poner de parametro pelicula.muestra los parametros de pelicula con la enumeracion de peliculas,es decir le pasa la enumeracion de peliculas a pelicula.saca el numero de indice de una lista y la pasa a la otra elegida,y con el +1 hace que pelicula empiece desde el 1 y no el 0

"""
# Listas multidimensionales 
print("\n********** Listado de contacto *************") #Esta es una lista que contiene otras listas con sus datos propios dentro de ellas
contactos = [
    [
       "Antonio",
       "antonio@antonio.com" 
    ],[                                                                              
        "Luis",
        "luis@luis.com"
    ],[
        "salvador",
        "salvador@salvador.com"
    ]


]

#print(contactos[1][1])  #para elegir la lista se pone el numerico deseado dentro de los corchetes,y para acceder al elemento dentro de esa lista se hace lo mismo

"""
for uwu in  contactos:   # nota al utilizar for,para recorrer una lista no es necesario poner "range" dado que el ramgo se determina con la lista
    print(uwu[0]) #al poner entre corchetes se puede definir que indice de las listas se quieren ver
"""
for contacto in contactos:
    for elemento in contacto:  #aqui lo que sucede es que muestra la lista,y seguido muestra lo que tiene esa misma lista,que vendria a ser los elementos que estan en las listas que estan en la lista mayor
        if contacto.index(elemento) == 0:

            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")











#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18614598#notes