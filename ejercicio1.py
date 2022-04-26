"""
Ejercicio 1.
    - Crear variables una "pais" y otra "continente"
    - Mostrar su valor por pantalla (Imprimir)
    - Poner un comentario diciendo el tipo de dato

"""
pais = "argentina"
continente  = "America"

print(pais)   #tipo de dato variable "String"
print(continente) #tipo de dato variable "string"

print(f"{pais} es un pais del continente de {continente}")

#print(f"{pais} - {continente}")

print(type(pais))

print(type(continente))



#Extra 

year = 2021  #integer

print(f"{pais} es un pais del continente de {continente}, y estamos en {str(year)} ")
#el numero lleva el str,para que deje de ser un integer y sea un string pasa de 2021 a ser "2021"