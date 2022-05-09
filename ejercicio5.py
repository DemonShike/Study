"""
Crear una lista con el contenido de esta tabla:
ACCION AVENTURA                 DEPORTES 
GTA     ASSASINS                    FIFA 21
COD     CRASH                       PRO 21
PUGB   Prince of persia             MOTO GP21

Mostrar esta informacion ordenada 
"""
"""




'''
for lista in listado_Juego:
    print(f"Categoria : {lista['categoria']}")
    print(f"Lista de juegos {lista['juegos']}")
'''
  
#ejemplo del profesor

for juego in listado_Juego:
    print(f"Categoria : {juego['categoria']}")
    for lol in juego['juegos']:
        print(lol)



"""
























"""
Crear una lista con el contenido de esta tabla:
ACCION AVENTURA                 DEPORTES 
GTA     ASSASINS                    FIFA 21
COD     CRASH                       PRO 21
PUGB   Prince of persia             MOTO GP21

Mostrar esta informacion ordenada 
"""


listado_Juego = [{

            "categoria" : "ACCION", 
            "juegos" : ["GTA ", "COD ", "PUGB"]},{
            "categoria" : "AVENTURA",
            "juegos" :  ["ASSASINS", "CRASH",  "Prince of persia"]},{
             "categoria" :  'DEPORTES', 
            "juegos": ["FIFA 21", "PRO 21", "MOTO GP21"  ]
            
            }
]


lista_juegos = [{
    "CATEGORIA" : "ACCION",
    "JUEGOS" : ["GTA", "COD", "PUGB"]
},{ "CATEGORIA" : "AVENTURA",
    "JUEGOS" : ["ASSASINS", "CRASH", "PRINCE OF PERSIA"]
},{ "CATEGORIA" : "DEPORTES",
    "JUEGOS" : ["FIFA 21", "PRO 21", "MOTO GP21"]
}

]

for categorias in lista_juegos:
    print(f"Estas en la categoria: {categorias['CATEGORIA']}")
    print(f"Juegos: {categorias['JUEGOS']}")






#https://www.udemy.com/course/master-en-python-aprender-python-django-flask-y-tkinter/learn/lecture/18627494#questions