'''
El condicional If explica que,su funcion se basa en condiciones,es decir
si algo sucede el comando if hace una cosa y si otra cosa sucede el condicional if hace otra

Es decir si una condicion se cumple pasa una cosa,y si no se cumple pasa otra

El condicional else ,es el que dara la intruccion si el condicional if no se cumple


# Condicional IF

SI se_cumple_esta_condicion:
   Ejecutar grupo de instrucciones
SI NO:
   Se ejecuitan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras intrucciones

# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos (son herramientas con las que se pueden hacer logicas,de forma diferente ,pero que pueden dar el mismo resultado segun se las emplee,variando de la comodida del desarrollador.En base al resultado que este quiera)

and Y
or o      
! negacion
not no

'''


# Ejemplo 1



print("############# EJEMPLO 1 ##############")

color = "rojo"
#color = input("Adivina cual es mi color favorito: ") #aqui se utiliza la entrada para que el usuario ponga un color y el condicional if decida

if color == "rojo": # el doble igual "==" se utiliza como comparador ,en este ejemplo compararia si color es igual a rojo se hace una cosa y si no otra,que en este caso lo es por que la variable de arriba asi lo determina "color = rojo"
    print("Enhorabuena!!")
    print("El color es Rojo")
else:
    print("El color NO es rojo")

# Ejemplo 2

print("\n############# EJEMPLO 2 ##############")

year = 2020
#year = int(input("¿En que año estamos? ")) #al poner el resultado int el numero que lo toma como texto ,se vuelve un numero con el que "if" puede realizar su operacion

if year >= 2021:
    print("Estamos de 2021 en adelante!! ")
else:
    print("Es un año anterior a 2021")

    # Ejemplo 3

print("\n############# EJEMPLO 3 ##############")

nombre = "Victor Robles"
ciudad = "Barcelona"
continente = "oceanida"
edad = 18
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")

    if continente != "Europa":
        print("El usuario no es europeo")        #se pueden anidar if dentro de otros if siempre que el de dentro este mas adelante que el anterior a el,y los else tienen que estar
    else:                                        #con el if al que le correspondan para que no haya errores
        print(f"es Europeo y de {ciudad}")

else:
    print(f"{nombre} No es mayor de edad")


# Ejemplo 4

print("\n############# EJEMPLO 4 ##############")

#dia = int(input("Introduce el numero del dia de la semana: "))
dia = 2
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")               #esta estructura esta mas desordenada a comparacion de la de abajo,y es mas dificil de leer
        else:
            if dia == 4:
                print("El dia es Jueves") 
            else:
                if dia == 5:
                    print("El dia es Viernes")
                else:
                    print("Ya es finde semana :D !!")

"""

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es miercoles")          #elif es una estructura de control,que mezcla if y else,esta se suele utiliza
elif dia == 4:                     #para hacer una estructura de comandos mas limpia y legible. 
    print("Es jueves")             #sirve principalmente para hacer condiciones una detras de otra (si no se cumple la primera pasa la segunda y asi infinitamente ,y si no se cumple ninguna se ejecuta el else final.)
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")



# Ejemplo 5

print("\n############# EJEMPLO 5 ##############")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Cual es tu edad oficial?"))
edad_oficial = 19

if edad_oficial >=18 and edad_oficial <= 65:      #and es un operador logico,este se utiliza para agregar mas condiciones a un if,si no se cumplen todas,no se pasa al if ,y se pasa al else automaticamente
    print("Esta en edad de trabajar !!")
else:
    print("No esta en edad de trabajar")


# Ejemplo 6

print("\n############# EJEMPLO 6 ##############")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":          #el operador or ,("o" en español) se utiliza para dar varias opciones en las que tiene que coincider una variable para que if funcione,en caso de que ninguna opcion se cumpla,se activara else
    print(f"{pais} es un pais de habla hispana !!")
else:
    print(f"{pais} no es un pais de habla hispana")


# Ejemplo 7

print("\n############# EJEMPLO 7 ##############")

pais = "alemania"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):       #el operador not (en español "no") se basa en que si no se cumple lo que esta entre parentesis de mismo,se activa el if,pero si si se cumple,pasa a activarse else,dado que not,si se cumplio
    print(f"{pais} NO es un pais de habla hispana !!")
else:
    print(f"{pais} SI es un pais de habla hispana")


# Ejemplo 8

print("\n############# EJEMPLO 8 ##############")

pais = "inglaterra"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un pais de habla hispana !!")                    #el operador and (en español y) sirve para agregar varias variables que se tienen que cumplir una almenos  para que se active if ,y si no  coinciden se activa else
else:
    print(f"{pais} Si es un pais de habla hispana")


