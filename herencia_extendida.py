#una clase puede heredar atributos de distintas clases. Se amplía y se multiplica.
# una clase puede heredar un método, pero sobreescribirlo.

class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Nacido')

    def hablar(self):
        print('Habla desde la clase Animal')

class Pajaro(Animal):
    def __init__(self,edad, color, altura_vuelo):
        #self.edad = edad
        #self.color = color
        #es lo mismo q usar la kw super
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('Pio pio')
    def volar(self, metros):
        print(f'El pájaro vuela {metros} metros')

canario = Pajaro(3,'amarillo',180)
loro = Animal(50,'verde')

canario.hablar()
loro.hablar()
canario.volar(37)

mi_animal = Animal(5,'Azul')

mi_animal.nacer()

#EL ORDEN DE LOS PARÁMETROS ALTERA EL RESULTADO. Siempre respeta el primer parámetro.
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre,Padre):
    pass