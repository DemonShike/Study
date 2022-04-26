"""
Ejercicio5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario

"""

numero1 = int(input("Dime el primer numero: ")) + 1 #el +1 lo puse para que no mostrara el numero inicial elegido sino el siguiente 
numero2 = int(input("Dime el segundo numero: "))

contador = 0                                                #Mi ejemplo,es funcional pero tiene un defecto y es que si el mumero1 es mayor al numero2 , el programa no funciona

                                                            #por ahora no soy capaz de crear un metodo que detecte este error y haga alrevez el sistema para que los muestre pero de mayor a menor            
for contador in range(numero1, numero2):
    print(f"Los numeros son: {contador}")

    contador += 1   #el contador lo puse pero no es necesario dado que no es comando while,y aca automaticamente iba a ir subiendo de 1 en 1


print("////////////////////////////////////////////////////////////////////")

numero1 = int(input("Dime el primer numero: ")) + 1          # a diferencia de mi el si decidio mostrar los 2 numeros elegidos por el usuario dentro de la tabla
numero2 = int(input("Dime el segundo numero: "))

if numero1<numero2:                                          #este ejemplo hecho por el profesor cuenta con la diferencia de que si el numero 2 es mas chico que el numero 1,manda un mensaje
    for contador in range(numero1, (numero2 + 1)):           #notificando que no se puede realizar ,y que tiene que ser el numero 2 mayor al numero 1
        print(contador)

    contador += 1
else:
    print("El numero 1 debe ser menor al numero 2")


