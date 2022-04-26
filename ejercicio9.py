"""
Ejercicio 9.Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111

"""





contador = 1

while contador < 100:
    numero = int(input("Ingresa el numero correcto: "))       #este ejemplo es de profesor a pesar de ser muy simple no pude resolver esta consiga,me cerre mucho en intentar que fuera indefinido     
                                                              # olvide que el comando while no avanza solo,yo pensaba que si ,entonces si le ponia un valor no iba a ser indefinido y tarde o temprano iba a llegar a su limite y parar,sin embargo,sin 
                                                              #si yo no le pongo algo que haga que su valor se sume nunca iba a detenerse,lo confundi con el comando for que si escala solo
    if numero == 111:
        break
    else:
        print(f"Has introducido el {numero}")






print("///////// Mi ejemplo ///////////")


contador = 1

                                                             #una vez comprendi el error me puse a hacerlo por mi cuenta asi que este es mi ejemplo con algunos detalles
while contador < 4:                                       #mientras que contador sea menor a 4,que es el numero que lo limita,va a seguir funcionando el bucle,y como no hay nada que aumente el valor de contandor,como por ejemplo " contador +=1" nunca va a aumentar y llegar a 100 para detener el bucle
    codigo = int(input("Ingrese el codigo correcto: "))
    if codigo == 111:
        print("El codigo es correcto !!")
        break
    else:
        print(f"El codigo {codigo} no es correcto,vuelve a intentarlo: ")
        contador += 1                                                   #inluso le agregue un sistema de intentos,al ser el limite 4 ,en cada vuelta contador vale 1 mas por cada intento,a los 3 intentos fallidos contador valdra 4 y se detendra el bucle,sin permitir ingresar mas intentos del codigo ,supongo que los sistema de contraseña seran similares :D .