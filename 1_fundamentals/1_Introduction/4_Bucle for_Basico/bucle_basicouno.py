
#1 imprime todos los numeros enteros del 0 al 150
'''
for valor in range(0,151,1):
    print(valor)
'''

#2 Multiplo de cinco: imprime todos los multiplos de 5 entre 5 y 1000
'''
for valor in range(5,1001,5):
    print(valor)
'''
#3 Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
'''
for multiplos in range(1,101,1):
    if(multiplos%10==0):
        print("Coding Dojo")
    elif(multiplos%5==0):
        print("Coding")
    else:
        print(multiplos)
'''

#4 Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
'''
for x in range(1,500000,2):
    print(x)
else:
    print("la suma final")
'''
#5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
'''
for x in range (2018,1980,-4):
    print(x)
'''
#6 Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
for x in range (0,20,3):
    print (x)