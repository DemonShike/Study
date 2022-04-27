"""
variables locales: se definen dentro de la funcion y no 
se puede usar fuera de ella, solo estan disponibles dentro.
a no ser que hagamos un return

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas

"""

# Variable global
frase = "Ni los genios son tan genios, ni los medicores tan mediocres"

print(frase)

def holaMundo():
    
    #frase = "Hola mundo!!"
    print("Dentro de la funcion:")
    print(frase)
    
    year = 2022
    print(year)
    global website     #este comando se utiliza para volver una variable local,una global y que pueda ser usada desde cualquier lugar del codigo
    website = "victorroblesweb.es"
    print("DENTRO: ", website)

    return "Dato devuelto " + str(year)



print(holaMundo())
print("FUERA: ", website)














#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18582937#questions/15855455