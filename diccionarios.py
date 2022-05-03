"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.

En resumen los diccionarios son parecidos a la listas,pero estos ,sus datos se les puede dar un valor que los represente ej: "antonio" le podes dar el valor nombre y queda asi nombre : antonio
"""




persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorroblesweb.es"
}

print(persona["apellidos"]) #al poner su clave,en la consola reproduce su valor,en este caso Robles

# Lista con diccionarios

contactos = [
    {
        "nombre": "Antonio",
        "email": "antonio@antonio.com"
    },
    {
        "nombre": "Luis",
        "email": "luis@luis.com"
    },
    {
        "nombre": "salvador",
        "email": "salvador@salvador.com"
    }
]

contactos[0]["nombre"] = "Antoñito" #aqui se le cambio el valor a nombre que en el indice es antonio,pero lo transformamos en antoñito
print(contactos[0]["nombre"])

print("\nListado de contactos: ")
for contacto in contactos:
    print("\n------------------------------------------")
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Emial del contacto {contacto['email']}")              #esta es una forma ordenada de mostrar diferentes valores de un diccionario 
    print("\n------------------------------------------")














#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18614648#overview