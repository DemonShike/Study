"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden
"""

personas = {
    "Victor",
    "Manolo",     # Dato curioso no  tengo que olvidarme,
    "Francisco"
}

personas.add("Paco")  #con add se pueden agregar elementos a un set
personas.remove("Francisco") # con remove se pueden remover elementos de un set

print(type(personas)) #con esto se comprueba el tipo de dato en este caso lo toma como uns set
print(personas)