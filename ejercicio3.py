"""
Ejercicio 3. Crear un programa que comporuebe si una variable
esta vacia y si esta vacia, rellenarla con texto en minisculas
y mostrarlo en mayusculas
"""
"""
variable_vacia = ""

if variable_vacia != "contenido":
    variable_vacia = "carlos se la come"
    if variable_vacia == "carlos se la come":             # Este ejemplo es funcional pero demasiado limitado,solo cumple lo pedido no me enorgullece para nada
        print("CARLOS SE LA COME")


"""

"""
print("///////////////////////////////////////////////////")

texto = " "

if len(texto.strip()) <= 0:             #aqui lo que sucede es que len comprueba si hay caracteres en la variable,que sucede que si llegan a haber espacios len los tomaria como caracteres,entonces se concatena el comando strip para eliminar esos espacios y que solo queden caracteres como letras o numeros o simbolos.
    texto = "hola me llamo gabriel"  #aca me confundi y no me funcionaa por que habia utilizado doble igual y era usar  1 solo
    print(texto.upper())

    #Mostrar el texto

else:
    print(f"La variable tiene contenido {texto}")



"""




























"""
Ejercicio 3. Crear un programa que comporuebe si una variable
esta vacia y si esta vacia, rellenarla con texto en minisculas
y mostrarlo en mayusculas
"""

variable_vacia = " "

if len(variable_vacia.strip()) <= 0:
    variable_vacia = "soy una poderosa variable"
    print(variable_vacia.upper())
else:
    print("La variable no esta vacia")
