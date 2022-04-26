"""
Ejercicio 4. Pedir dos numeros al usuario y hacer todas las 
operaciones basicas de una calculadora y mostrarlo por pantalla.

"""

numero1 = int(input("Inserta el primer numero: "))
numero2 = int(input("Inserta el segundo numero: "))

print(f"Suma = {numero1 + numero2}")
print(f"Resta = {numero1 - numero2}")                                  #Calculadora hecha por mi
print(f"multiplicacion = {numero1 + numero2}")
print(f"division = {numero1/numero2}")



print("####   CALCULADORA   ####")

numero1 = int(input("Introduce el Primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

print("Suma: " + str(numero1+numero2))
print("resta: " + str(numero1-numero2))                          #ejemplo del profesor(el uso otro metodo interesante,dado que no usa el comando f,solo convierte os numeros en str,para que puedan ser concatenados)
print("multiplicacion: " + str(numero1*numero2))
print("division: " + str(numero1/numero2))