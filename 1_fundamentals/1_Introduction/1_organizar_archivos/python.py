num1 = 42 # variable de declaracion , numero iniciado
num2 = 2.3 # variable de declaracion , decimal/float iniciado
boolean = True # variable de declaracion, bolleano iniciado
string = 'Hello World' # variable de declaracion, cadena iniciado

# variable de declaracion, lista iniciada
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable de declaracion, dictionary iniciada
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable de declaracion, tuplas iniciada
fruit = ('blueberry', 'strawberry', 'banana')

# print to console, type check
print(type(fruit))

# print to console,list access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

#print to console, dictionary acces value
print(person['name'])

# Dictionary change value
person['name'] = 'George'

# Dictionary change value
person['eye_color'] = 'blue'

#print to console, tuple acces data
print(fruit[2])


# conditional if, evaluation, print to console, conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")


# conditional if - elif - else - print to console
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")



#for loop star at 0 and goes up to 5
for x in range(5):
    print(x)

#for loop star at 2 and goes up to 5
for x in range(2,5):
    print(x)

#for loop star at 2 and goes up to 10, increments by 3
for x in range(2,10,3):
    print(x)

# while loop, variable declaration
x = 0
while(x < 5):
    # printing to console
    print(x)
    # incrementing x
    x += 1

# list detelte value at end
pizza_toppings.pop()

#list delete value at index
pizza_toppings.pop(1)

# print to console of dictionary
print(person)
#Dictionary delete value
person.pop('eye_color')
print(person)


# for loop through a list
for topping in pizza_toppings:
    #coditional if
    if topping == 'Pepperoni':
        #continues
        continue
        #print to console
    print('After 1st if statement')
    #conditional if
    if topping == 'Olives':
        #stops the loop
        break

# funtion declaration
def print_hello_ten_times():

    # for loop starts at 0 goes up until 10
    for num in range(10):
        #print to console
        print('Hello')

#function call
print_hello_ten_times()

#function declaration with parameter x
def print_hello_x_times(x):
    #for loop uo until a given number x
    for num in range(x):
        #print to console
        print('Hello')
# function call arguement of 4
print_hello_x_times(4)

# funtion declaration with default parameter
def print_hello_x_or_ten_times(x = 10):
    # for loop until x
    for num in range(x):
        # printo to console
        print('Hello')
# function call goes to 10
print_hello_x_or_ten_times()
# function call goes to 10
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)



class ClaseVacía:
    pass

for val in mi_cadena:
    pass

lista_vacía = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# salida: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# salida: ['Francis', 'Oliver'


print(type(2.63))		# salida: <class 'float'>
print(type(new_person))		# salida: <class 'dict'>
