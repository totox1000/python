
#1 Actualizar valores en diccionarios y listas
'''
1.1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
1.2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
1.3 En el directorio_deportes, cambia "Messi" por "Andrés".
1.4 Cambia el valor 20 en z a 30.
'''
#1.1 Ejercicio

'''x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15'''

#1.2 Ejercicio

'''estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(estudiantes[0]['last_name'])
estudiantes[0]['last_name'] = 'Bryan'
print(estudiantes)'''



#1.3 Ejercicio
'''
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['futbol'][0] = 'Andres'
'''

#1.4 Ejercicio

'''
z = [ {'x': 10, 'y': 20} ]

print(z[0]['y'])
z[0]['y'] = 30
print(z)
'''

#2 Iterar a traves de una lista de diccionarios
'''Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
Por ejemplo, dada la siguiente lista:'''

'''estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'},
    ]


for diccionario in estudiantes:
    for llave,valor in diccionario.items():
        print(f"LLave:{llave}, Valor:{valor}")'''
    # print(f"Dict:{diccionario}")


#3 Obtener valores de una lista de diccionarios
#'''Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
#la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) 
#debería'''

alumnos = [
{"nombre":  "Michael", "Apellido" : "Jordan"},
{"nombre" : "John", "Apellido" : "Rosales"},
{"nombre" : "Mark", "Apellido" : "Guillen"},
{"nombre" : "KB", "Apellido" : "Tonel"},
]




'''def iterateDictionary2(lista_de_alumnos):
    for dict in lista_de_alumnos:
        alumno=''
        for llave in dict:
            #print(f"Llave:{llave}, Valor:{dict[llave]}")
            alumno+=llave +' - '+dict[llave]+', '
            print(alumno)'''




#4 Iterar a través de un diccionarios con valores de lista
'''Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
asociados dentro de la lista de cada clave. Por ejemplo:'''


'''dojo = {
"ubicaciones" : ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
"instructores" : ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}'''


'''print(len(dojo["ubicaciones"]))
print(dojo["ubicaciones"][0])
print(dojo["ubicaciones"][1])
print(dojo["ubicaciones"][3])
print(dojo["ubicaciones"][4])
print(dojo["ubicaciones"][5])
print(dojo["ubicaciones"][6])'''

'''print(len(dojo["instructores"]))
print(dojo["instructores"][0])
print(dojo["instructores"][1])
print(dojo["instructores"][3])
print(dojo["instructores"][4])
print(dojo["instructores"][5])
print(dojo["instructores"][6])'''




