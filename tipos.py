
nada = None
cadena = "hola soy victor robles web"
cadena = "desarollador web"
entero = 99 #este tipo de dato refiere a los numeros enteros
flotante = 4.2 #el float o flotante refiere a un numero decimal
booleano = False #indica true o false ,es decir si una variable es true or false,ademas se los asigna en mayuscula la primera letra
lista = [10, 20, 30, 40, 200] #se utiliza para mostrar una lista de algo numneros en este caso
listaString = [44, "treinta", 30, "cuarenta"] #se utiliza para hacer una lista de varios valores,por ejemplos numeros y textos
tuplaNoCambia = ("master", "en", "python")#lista de datos que no cambian,es como la lista pero sus datos se definen entre parentesis
diccionario = {
    "nombre": "victor",
    "apellido": "robles",
    "curso": "master en python"
} #el diccionario es un tipo de dato cuyo metodo es para guardar datos,para definirle un dato y un valor al mismo
rango = range(9) #muestra un rango de datos ,por ejemplo en este caso mostrara un rango del 0 al 9
dato_byte = b"probando" #con la b se vuelve un dato byte

#imprimir la variable  de arriba
print(dato_byte)

#mostrar tipo de dato
print(type(dato_byte))


#como convertir un tipo de dato en otro tipo de dato. ej: concadenar un numero en un texto
texto = ("hola soy un texto")
numerito = str(776) #al transformar un numero en string con "str" convertimos el numero en una variable ej:
#el numero es 776 pero con el str,se vuelve "776"

print(texto + "\t" + numerito)

numerito = int(776)
print(type(numerito))
numerito = float(776)
print(type(numerito))
#diferentes ejemplos de datos que se pueden usar para hacer que la funcion sea otro tipo de dato