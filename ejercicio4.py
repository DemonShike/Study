"""
Ejercicio 4. 
Crear un script que tenga 4 variables,una lista, un string, 
un entero y un booleano y que imprima un  mensaje
segun el tipo de dato de cada variable
"""
"""
#en est ejercicio no pude hacer un ejemplo,por que entendi mal la consigna,entendi que debia de hacer un script que comprobara el tipo de contenido que esta dentro de las variables

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"          #esta funcion lo que hace es que al recibir un tipo de dato,que lo recibe a travez de comprobarTipado,lo analiza dentro de su if,y si el tipo de dato coincide con una de las opciones
    elif tipo == bool:            # pone el texto,por ejemplo si uno es tipo list,pondra lista en el texto de comprobarTipado,asi es mas entendible el tipo que sea la variable
        result = "BOOLEANO"
    elif tipo == int:
        result = "ENTERO"
    elif tipo == str:
        result = "CADENA DE TEXTO"

    return result
         


def comprobarTipado(variable, tipo):
    comprobador = (isinstance(variable, tipo))
    result = ""
                                                                #esta funcion lo que hace es usar isinstance,para comprobar la variable elegida y el tipo elegido ,seguido de esto,comprueba con el if si la variable es del tipo que pusimo ponda lo de if y sino lo de else
    if comprobador:
        result = f"Este dato es del tipo {traducirTipo(variable)}"
    else:
        result = "El tipo de dato no es correcto"

    return result
        

lista = ["hola", "uwu", "demon", 78] #un string es una variable que alverga letras y numeros
nombre = "demonshike"
numero_clave = 57
casa = False


print(comprobarTipado(lista, list))
print(comprobarTipado(nombre, list))
print(comprobarTipado(numero_clave, list))
print(comprobarTipado(casa, bool))




"""

























"""
Ejercicio 4. 
Crear un script que tenga 4 variables,una lista, un string, 
un entero y un booleano y que imprima un  mensaje
segun el tipo de dato de cada variable
"""

lista = [2, 4, 6,]
cacatua = "demon"
numero = 3
fumar = False

def identificador(variable, tipo):

    comprobar = isinstance(variable, tipo)
    if comprobar:
        variables1 = f"La variable {variable} es del tipo {tipo}"
    else:
        variables1 = f"La variable {variable} no es de tipo {tipo}"

    return variables1

print(identificador(lista, int))







#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18627492#questions/14546174