class Pajaro:
    def __init__(self,especie):
        self.especie = especie
    
    #METODOS DE INSTANCIA
    def piar(self): #SELF hace referencia a cada instancia del objeto en cuestión.
        print('pio pio, mi especie es {}'.format(self.especie))

    #método que pida argumentos:
    def volar(self, metros):
        print(f'El pájaro voló {metros} metro/s.')

loro_azul = Pajaro('Loro')
print(loro_azul.volar(5))
print(loro_azul.piar())

class Alarma:
    def postergar(self,cantidad_minutos):
        Alarma.cantidad_minutos=cantidad_minutos
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

    #MÉTODOS DE CLASE
    @classmethod
    def mi_metodo(cls,otra_cosa):
        print(f'algo y {otra_cosa}')
    
    #MÉTODOS ESTÁTICOS. No acepta ni self ni cls(clase) como parámetro. 
#No pueden acceder a los atributos de la instancia (loro_azul), ni de la clase (Pajaro)
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
     
Mascota.respirar()
    
        

