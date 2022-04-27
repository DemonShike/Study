"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas
en un nombre concreto que pueden reutilizarse invocando a
la funcion tantas veces como sea necesario.

EJ:

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INTRUSCCIONES

nombreDeMiFuncion(mi_parametro)  #para invocarla se hace asi
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1






print("##### EJEMPLO 1 ######")

def muestraNombre():
    print("Juan")
    print("gabriel")
    print("paco")
    print("francisco")
    print("aitor")
    print("nestor")
    print("\n")

# Invocar funcion 

muestraNombre()
muestraNombre()
muestraNombre()


"""# Ejemplo 2:
print("##### EJEMPLO 2 ######")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    
    if edad >= 18:
        print("Eres mayor de edad")
                                               #un parametro es un dato que va en el parentesis que se pasa desde fuera adentro de la funcion,para 
                                            #parametrizar la funcionalidad que hay dentro de una funcion.
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)   """


# Ejemplo 3:
print("##### EJEMPLO 3 ######")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero}x{contador} = {operacion}")


    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1:
print("---------------------------------------------------------------")
print("##### EJEMPLO 3.1 ######")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)



# Ejemplo 4:
print("##### EJEMPLO 4 ######")

# Parametros opcionales
def getEmpleado(nombre, dni = None):     #esto es una forma de hacer que un parametro sea opcional para no tener que agregarlo obligatoriamente
    print("Empleado")                     # se puede definir que parametros tienen que estar si o si ,o cuales pueden ser opcionales,si hay una funcion dni se volvera ese valor,pero si no la definimos tomara el predeterminado en este caso "None"
    print(f"nombre: {nombre}")
    
    if dni != None:
        print(f"Dni: {dni}")



getEmpleado("gabriel", 43334343)

# Ejemplo 5: parametros opcionales y return o devolver datos

print("##### EJEMPLO 5 ######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo   #con el return se define que es lo que se va a devolver,cuando se pida la funcion,es como una especie de print pero para las funciones

print(saludame("Victor robles"))


saludame("Gabriel")

# Ejemplo 6: usar el return para devolver

print("##### EJEMPLO 6 ######")

def calculadora(numero1, numero2, basicas = False):
    
     
    suma = numero1 +  numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    
    if basicas != False:   
        cadena += "Suma:" + str(suma)
        cadena += "\n"
        cadena += "resta: " + str(resta)
        cadena += "\n"                          #aqui lo que se hace es que cadena vale "" es decir nada practicamente,y al hacer cadena += algo, en este caso suma resta etc,se le esta sumando contenido a cadena,se le esta dando mas variables por asi decirlo ,se le esta concatenando mas cosas
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(5, 5))


# Ejemplo 7: conbinar funciones

print("##### EJEMPLO 7 ######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
                                                          
def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):                                  #en este ejemplo,se crea una funcion que tiene dentro las otras 2 funciones,este metodo se usa para ahorrar tiempo y reutilizar codigo
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto


print(devuelveTodo("Gabriel", "Martinez"))      #En este ejemplo se muestra como poner funcion es en con otras funciones



# Ejemplo 8: Funciones lambda

print("\n##### EJEMPLO 8 ######")

dime_el_year = lambda year : f"El año es {year * 50}"     #la funcion lamba sirve para hacer una linea de codigo sola,y se suele utilizar para hacer tareas cortas pero repetitivas, primero se pone la variable,como por ejemplo devolver un dato o hacer una cuenta sencilla
                                                          # en este caso es "dime_el_year" luego se la iguala a "lambda" luego se le pone el parametro en este caso "year"  y luego se define lo que va a devolver la funcion,en este caso el texto y el year como parametro
print(dime_el_year(2034))





#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18528692#questions/14301890