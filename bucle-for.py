"""

# FOR
for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

El bucle for no lo entiendo de todo,pero se basa en que recorre una serie de elementos dentro de un rango o lista determinada,y con esta se pueden realizar cosas simples como por ejemplo una suma constante con un numero que va en bucle.
el bucle for termina cuando alcanza el rango maximo limitado.
"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("voy por el "+ str(contador))         

    resultado = resultado + contador

print(f"El resultado es: {resultado}")




# Ejemplo 1

# Ejemplo tablas de multiplicar

print("\n////////////// EJEMPLO 1 /////////////")

numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### tabla de multiplicar de numero {numero_usuario} ###")

for numero_tabla in range(1,11):                       #aqui el comando for se usa para realizar una calculadora,multiplica el numero elegido en un rango determinado,y luego se imprime en la consola
    
    if numero_usuario == 45:
        print("No se pueden mostrar numero prohibidos !!")  #el comando if se puede usar para agregar condiciones al bucle,para que por ejemplo no se complete el bucle si pasa x cosa,en este caso si se pone el numero 45
        break                                               #al ponerse el numero 45 el comando if imprimira el mensaje,y con el condicional break,cortara el bucle for 

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")   #y aqui se hace el comando donde se determina como se vera en la consola y se realiza la multiplicacion del for que en este caso es "numero tabla" * "numero usuario" (que es el que pone el usuario)
else:
    print("Tabla finalizada :D")  # a diferencia de cuando usas else con  if,que else se muestra si if no se cumple,en el caso de for ,else se muestra siempre al final del comando for.






# https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18509630#overview
