"""
Ejercicio 3.Escribir un programa que muestre los cuadrados (un numero 
multiplicado por si mismo de los 60 primeros numeros naturales)

resolverlo con el bucles for y con while

"""


# WHILE
numero_elegido = 0

contador = 0
                                                                                  # Este es el ejemplo de un contador hecho por mi mismo
while contador <= 60:
    print(f"el cuadrado de {numero_elegido} es: {numero_elegido * contador}")

    numero_elegido += 1
    contador += 1
    

print("/////////////////////////////////////////////////////////")


contador = 0

while contador <= 60:                                                                # Ejemplo de profesor 
   
    
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1



print("/////////////////////////////////////////////////////////")

# FOR

contador = 0

for contador in range(0,61):
    print(f"el cuadrado de {contador} es: {contador*contador}")                    # ejemplo con FOR hecho por mi

    contador += 1



print("///////////////////////////////////////////////////////")

for numero in range(61):
    cuadrado = numero*numero                                                        # Ejemplo cuadrado con For hecho por el profesor
    print(f"El cuadrado de {numero} es {cuadrado} ")


#    https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18527268#questions/10040224
    
    

