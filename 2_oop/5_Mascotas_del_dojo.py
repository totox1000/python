'''ASIGNACION MASCOTAS DEL DOJO''' '''Practicar aun mas la POO y asociacion de classes'''

'''Crea una clase Ninja con los atributos ninja mencionados anteriormente.
Crea una clase Mascota con los atributos mascota mencionados anteriormente.
Implementa caminar(), alimentar(), bañar() en la clase ninja.
Implementa dormir(), comer(), jugar(), sonido() en la clase mascota.
Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.
Haz que el ninja alimente, pasee y bañe a su mascota.
BONUS NINJA: Usa módulos para separar las clases en diferentes archivos.
BONUS SENSEI: Usa la herencia para crear subclases de mascotas.
Comprime la asignación y envíala.'''


class Pet:

    # implementa __init__( name , tipo , golosinas,salud,energia ): Estos son atributos
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    # implementa los siguientes (dormir,comer,jugar,sonido): Estos son metodos
    # dormir() - incrementa la energia de la mascota en 25
    def sleep(self):
        self.energy += 25
        return self

    # comer() - incrementa la energia de la mascota en 5 y la salud en 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # jugar() - incrementa la energia de la mascota en 5
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # ruido() - imprime el sonido que produce la mascota
    def noise(self):
        print(self.noise)



class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implementa los siguientes metodos:
    # caminar() - pasea a la mascota del ninja invocando el metodo de mascota jugar()
    def walk(self):
        self.pet.play()
        return self

    # alimentar() - alimenta a la mascota del ninja invocando el metodo de mascota comer()
    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! necesitas mas comida de mascota!")
        return self

    # bañar() - limpia a la mascota del ninja invocando el metodo de mascota sonido()
    def bathe(self):
        self.pet.noise()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

nibbles = Pet("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",my_treats,my_pet_food, nibbles)

adrien.feed();
adrien.feed();
adrien.feed();


