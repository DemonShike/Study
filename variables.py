"""
Una variable es un contenedor de informacion
que dentro guardara un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""



texto = "Master en Python"
texto2 = "con victor robles"
numero = 32
decimal = 6.7

#mostrar valor de las variables

print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------------------")

#sustituir el valor de algunas variables / reasignando valores

numero = 77
decimal = 8.9
print(numero)
print(decimal)

#se pueden asignar varias variables del mismo nombre pero
#con diferente resultado,y al usar el cmd muestra ambos

print("------------------------------------")


#concatenacion

nombre = "victor"
apellidos = "robles"
web = "victorroblesweb.es"

print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")
print("hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
print(nombre, apellidos, web,)

#estos 4 metodos sirven de igual manera para concatenar solo que
#sus usos pueden variar dependiendo para que se lo necesite