#crear una clase que contenga los elementos en común para todas las instancias. 
# Por ejemplo: class Animal def nacer(self), respirar(self), morir (self)
# class Pajaro(Animal): / class Mamifero(Animal)
#DRY DON'T REPEAT YOURSELF
class Animal:
    def nacer(self):
        print('Este animal ha nacido.')

class Pajaro(Animal):
    pass

print(Animal.__subclasses__())

piolin = Pajaro()
piolin.nacer()


class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
    
class Automovil(Vehiculo):
    pass