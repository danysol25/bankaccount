class Pajaro:
    #los atributos de clase, son IGUALES para todos los objetos que crees bajo esa clase. ej:
    alas = True 
    def __init__(self, color, mi_parametro): #init es un método CONSTRUCTOR. Inidica los atributos que la clase requerirá.
        self.color = color #self representa LA INSTANCIA del objeto que será creado. 
        self.mi_atributo = mi_parametro
mi_pajaro = Pajaro('negro','elefante')

print(mi_pajaro.mi_atributo)
print(Pajaro.alas)