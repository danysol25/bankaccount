#metodos con __
# __init__ para marcar los atributos iniciales
#__mro__ para ordenar
#__bases__
#__subclasses__

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self): #me ayuda a definir la forma en que quiero q se manifieste un str de mi clase.
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self): #establezco que quiero eliminar alguna instancia
        self.titulo
        print('Libro eliminado')

    