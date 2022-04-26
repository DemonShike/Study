"""
Ejercicio 8.¿Cuanto es el x porciento de x numero?
                            20% de 150

"""



numero = int(input("¿De que numero quieres saber el porcentaje?: "))
porcentaje = int(input("¿Cuanto es el porcentaje?: "))
                                                                  #mi ejercicio es funcional,incluso para hacerlo mas prolijo podria poner la cuenta de resultado dentro de el print
Resultado = (numero* (porcentaje/100))                   #aqui antes habia puesto "Resultado = numero % porcentaje" pero me estaba confundiendo dado que % no saca el porcentaje sino el resto y puse el del profesor (y mi ejemplo solo servia con divsiones de numeros pares)

print(f"El {porcentaje} % de {numero} es = {Resultado}")


print("//////////////////////////////////////////////")

numero = int(input("Introduce el numero: "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {numero}? "))

operacion = (numero* (porcentaje/100))                                    #ejemplo de profesor,uso una tecnica de multiplicacion para sacar el porcentaje que no conocia, carencias en mis matematicas :(

print(f"El {porcentaje}% del {numero} es: {operacion}")