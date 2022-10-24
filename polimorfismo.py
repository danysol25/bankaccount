#muchas formas

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muu')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca_uno = Vaca('Aurora')

oveja_uno = Oveja('Lola')

vaca_uno.hablar()
oveja_uno.hablar()

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca_uno)


#Práctica Polimorfismo 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
 
for dato in [palabra, lista, tupla]:
    print(len(dato))

#Práctica Polimorfismo 2
class Mago():
    def atacar(self):
        print("Ataque mágico")
 
class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
 
class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
#instancias
un_mago = Mago()
un_arquero = Arquero()
un_samurai = Samurai()

#los listo
una_lista = [un_mago,un_arquero,un_samurai]

#itero la lista
for instancia in una_lista:
    instancia.atacar()

#Práctica Polimorfismo 3

class Mago():
    def defender(self):
        print("Escudo mágico")
 
class Arquero():
    def defender(self):
        print("Esconderse")
 
class Samurai():
    def defender(self):
        print("Bloqueo")
 
def personaje_defender(personaje):
    personaje.defender()