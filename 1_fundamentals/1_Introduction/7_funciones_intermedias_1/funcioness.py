#2 Iterar a traves de una lista de diccionarios
'''Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
Por ejemplo, dada la siguiente lista:'''

mi_dicc = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'},
    ]

for first_name,last_name in mi_dicc.values():
    print(first_name,last_name)
    