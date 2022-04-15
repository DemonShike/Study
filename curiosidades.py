mi_texto = " 'Master' " #las comillas simples tambien funcionan siempre que no se repitan afuera de la palabra
mi_texto2 = "en \"python\" " #de esta manera se puede poner un texto o una palabra entre comillas utilizando \

texto_unido = mi_texto + " " + mi_texto2 #de esta manera puedo juntar las cadenas en una variable para ahorrar espacio y tiempo
print(texto_unido)


texto_unido = mi_texto + " \n " + mi_texto2 #hace un salto de linea como cuando apretas enter
print(texto_unido)

texto_unido = mi_texto + " \t " + mi_texto2 #hace una tabulacion es decir hace 4 espacios
print(texto_unido)

texto_unido = mi_texto + " \r " + mi_texto2 #elimina todo lo que este a la izquierda de la misma 
print(texto_unido)

#estos son valores especiales para dar un mejor uso a las variables
