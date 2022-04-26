"""
Ejercicio10. Crear un programa que le pida al usuario la nota de 15 alumnos y sacar por pantalla cuantos han aprobado
y cuantos han suspendido
"""



"""

for alumnos in range (1,16):
    nota = int(input(f"Nota del alumno numero {alumnos }: "))
    if nota >= 7:
        print(f"el Alumno {alumnos} aprobo con {nota}")                           #este es el primer intento,en este caso te responde despues de poner la nota quien aprobo o desaprobo,intentare hacer que los diga con todos al final
    else:
        print(f"El alumno suspendio con {nota}")
        """




print("///////////////////////////////////////////////////////////////////////")

alumnos_aprobados = 0
alumnos_suspendidos = 0

for alumnos in range (1,16):
    nota = int(input(f"Nota del alumno numero {alumnos }: "))                       #este ejemplo cumple las normas pedidas 
    if nota >= 7:
        alumnos_aprobados += 1

    else:
        alumnos_suspendidos += 1

print(f"Los alumnos aprobados son {alumnos_aprobados}")
print(f"Los alumnos suspendidos son {alumnos_suspendidos}")



print("///////////////////////////////////////////////////////////////////////")


contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"Que nota quieres ponerle al \"alumno {contador}\"?"))     #este ejemplo de profesor es interesante por que uso el bucle while,pero ademas ,decidio crear una variable que te dejara elegir los alumnos que quisieras ,que a diferencia de mio limita los estudiantes a 15 como se pidio en la consigna.aun asi podria mejorar el mio basandome en este y usando el bucle for
    if  nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f"\nAlumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")