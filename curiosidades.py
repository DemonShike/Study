def mi_funcion(nombre):
    return "Hola que tal "  + nombre        # Lo recomendable es hacer siempre las variables y funciones arriba de todo junto
    
def mi_segunda_funcion(apellidos):
    return "Hola que tal 2 " + apellidos

nombre = "Victor"
apellidos = "Robles"    #la variable siempre tiene que estar definida antes que la funcion donde se las llama nunca despues.

print("Hola mundo")
print(f"Bienvenido {nombre}")      #es mucho mas recomendable que una funcion devuelva un dato con return,que hacer un print dentro de la misma
                                    #supongo que es mejor usar el return,por que el print se lo pude definir cuando sea necesario y es mas practico que tener que borrar el print en la funcion base y que todos los lugares  donde se la pida no funcionen.
print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))         #para recordar,una funcion lo que hace es que al llamarla.esta trae el pedazo de codigo que le escribimos dentro anteriormente














#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/19049246#notes