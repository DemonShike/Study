"""
Ejercicio 2. Escribir un script que
nos muestre todos los numeros pares del 1 al 120


"""

numero_par = 2
numero_maximo = 120

                                                   #script que muestra todos los numeros pares con el comando while,este suma de 2 en 2 hasta llegar a 120 partiendo desde el 2

while numero_par <=120:
    print(f"Los numeros pares son {numero_par}")

    numero_par += 2

print("-----------------------------------------------------")

otro_numero = 2                                               #script que muestra todos los numeros pares con el comando for ambos estan hechos por mi ,este multiplica los numeros impares dando resltados pares 

for numero_tabla in range (1,61):
    print(f"Tus numeros pares son {numero_tabla*otro_numero}")


print("--------------------------------------------")

contador = 1

for contador in range (1,121):
    if contador%2 == 0:
        print(f"par: {contador}")                    #este script hecho por el profesor,tiene el siguiente funcionamiento,utiliza la variable contador para recorrer los 120 numeros
    """
    else:                                            #si esos numeros divididos por 2 dan de resto 0,entonces hara el print y pondra el numero,como adicional puso el else para que muestre los impares
        print(f"impar: {contador}")

        """