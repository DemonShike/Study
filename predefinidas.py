nombre = "Victor Robles"

#funciones generales
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, int)   #el isinstance se usa poniendo adentro la variable seguida de un tipo,y luego se usa el if para comprobar si la variable es el tipo que pusimos
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios
frase = "     mi contenido      "
print(frase)
print(frase.strip()) #esta funcion limpia los espacios

# eliminar variables

year = 2022
print(year)
del year     #con esto se puede borrar el valor a una variable
#print(year)

# comprobar variable vacia
texto = "ff"
                                  
if len(texto) <= 0:                 #esto comprueba el valor de la variable
    print("La variable esta vacia")
else:
    print("La variable tiene contenido" ,len(texto)) #al poner len en el print seguido del valor del texto te da el contenido del mismo


# Encontrar caracteres

frase = "La vida es bella"
print(frase.find("vida"))   #este buscador te dice en que caracter esta la palabra que buscas dentro de la variable que definas

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")   #este cumple la funcion de reemplazador de palabras dentro de una funcion,primero eliges la funcion y luego la palabra que vas a reemplazar y luego la siguiente palabra
print(nueva_frase)

# Mayusculas y minusculas

print(nombre)
print(nombre.lower())      #con lower vuelves el contenidos de la variable y los parametros elegidos a minuscula y con upper a mayuscula
print(nombre.upper())