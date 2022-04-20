# Entrada
nombre = input("¿cual es tu nombre?: ") # input se usa para darle la accion al usuario de ingresar algo
edad = input("¿Cual es tu edad?: ")

# Salida
#print(f"Me alegro de conocerte, bienvenido {nombre}, veo que tienes {edad} años!!") #en caso de querer sumar algun numero en la entrada de datos
#habria que  usar el comando int para volver el numero en un entero,dado  que es una cadena de texto no se sumaria,el comando a usar en este caso
#por ejemplo seria {int(edad) + 2} al volverse un numero me dejara hacer la operacion

print("Me alegro de conocerte, bienvenido {}, veo que tienes {} años!!".format(nombre, edad))

#print("Me alegro de conocerte, bienvenido", nombre) #este comando tambien es funcional pero solo sirve con 1 palabra