"""
EJERCICIO7.hacer un programa que muestre todos los numeros 
impares entre dos numeros que elija el usuario.

"""

numero1 = int(input("Ingrese su primer numero: "))
numero2 = int(input("Ingrese su segundo numero: "))

if numero1 > numero2:
    print("Numero 1 no puede ser mayor que Numero 2")           #Mi ejemplo, utilice el if not,para que cada vez que hubiese un numero par no se activara,pero cuando no lo hubise se activara  y printiara el texto
else:
    for impar in range(numero1, (numero2 + 1)):   #aqui me corregi solo poniendome el +1,por que no tuve en cuenta que no se mostraba el numero impar elegido por el usuario.
        if not impar%2 == 0:
            print(f"Los numeros impares son: {impar}")  



print("///////////////////////////////////////////////////////////////")


if numero1 < numero2:
    for x in range(numero1, (numero2+1)):
        if x%2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} no es par")                        #este ejemplo de profesor no me gusto,por que muestra los numeros par,cuando la consigna era que muestre todos los impares,estaria bien que hubiera enseñado a solo mostrar los par

else:
    print("El numero 1 debe ser menor al numero 2")
