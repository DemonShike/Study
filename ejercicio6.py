"""
Ejercicio6. Mostrar todas las tabla de multiplicar de 1 al 10.
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10.
"""

multiplicacion = 1

tabla = 1

print(f"La tabla del 1 es:")                           #aqui lo unico que se me ocurrio es ,hacer un else y hacerlo en cadena agregando una variante con un numero superior

for tabla   in range(1,11):
     print(f"{multiplicacion} x {tabla} = {tabla*multiplicacion}")


print("///////////////////////////////////")


for cabecera in range(1,11):
    print("#################################")
    print(f"##### Tabla del {cabecera}#####")
    print("#################################")                           #ejemplo del profesor

    for numero in range(1,11):
        print(f"{cabecera} x {numero} = {cabecera*numero}")
    
    print("\n") 

# 

for titulo in range(1,11):
    print(f"Tabla del {titulo}")


    for codigo_multiplicacion in range(1,11):
        print(f"{titulo} x {codigo_multiplicacion} = {titulo*codigo_multiplicacion}")

    print("\n")    



# 
# ,no tuve en cuenta que podia repetir el comando for siempre respetando la gerarquia,aqui lo que sucede es que cabecera printea lo que tiene dentro,luego le toca a numero
#numero printea la cuenta en la que se multiplica cabecera*numero cabecera vale 1 en ese momento y se multiplica por los 11 numeros de numero,una vez printeado todo eso el ciclo vuelve a empezar solo que 
#en esta ocasion cabecera vale 2 y asi,es simple pero me costo interpretarlo o crearlo .Principalmente por que olvide como funcionan las gerarquias.
            

        

