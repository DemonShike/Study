"""
# BUCLE WHILE 
Estructura de control que itera o repite la ejecucion de una serie
de instrucciones tantas veces como sea necesario,
hasta que deje de cumplirse la condicion 

es necesario marcarle un limite al cual detenerse


while condicion:
    bloque de intrucciones
    actualizacion de contador

"""





contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1           #esto es lo mismo que poner " contador = contador + 1" 



print("-------------------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:

    muestrame = muestrame + ", " + str(contador)       #en este comando lo que sucede es lo siguiente, al valer muestrame 0 se le suma una "," y luego se le suma contador(en string) esto da de resultado 0,1
    contador += 1                                      #luego al 0,1 se le suma ,2 esto se debe a que "muestrame" que en la vuelta anterior valia 0 ahora es igual a 0,1 ,y a este se le suma ,2,entonces 
                                                       # en la siguiente  vuelta muestrame valdra 0,1,2 y luego se le sumara contador que sera 3 dado el bucle,y se sumara y queda 0,1 ,2 ,3 (al solo ser la coma texto
print(muestrame)                                       # no tiene significativo matematico entonces los numeros no se suman solo se concatenan "se pegan " por asi decirlo)


# Ejemplo 1

print("###### EJMPLO 1 ###### ")

numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if numero_usuario  < 1:
    numero_usuario = 1

print(f"### Tabla del {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1


else:
    print("\nTabla terminada.")
""" mas info en los comentarios del video,hay un men que explica mejor esto """




#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18527258#overview





























