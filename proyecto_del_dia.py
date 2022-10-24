from typing import final


balance = 20
operacion_terminada = False

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=10):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self,deposito):
        self.balance += deposito
        print(f'Deposito aceptado.')

    def retirar(self, retiro):
        if self.balance >=  retiro:
            self.balance -= retiro
        else:
            print('No tiene suficiente dinero en la cuenta para hacer ese retiro.')
        
    def salir():
        print('Ha salido de su cuenta. Vuelva a ingresar.')

def crear_cliente():
    nombre_cliente = input("Ingrese su nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), o Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print("Gracias por operar en Banco Python")

try:
    inicio()
except:
    print('Algo en el programa no se ejecutó correctamente.')
else:
    print('Todo ha salido OK')
finally:
    print('Operación terminada.')

inicio()

'''def seleccionar_operacion(balance, opcion):
    balance = balance
    print(f'Su saldo actual es: {balance}\n')
    print('Seleccione la operacion que desee ejecutar:\n')
    print(int (input(
        OPCIÓN 1 - IMPRIMIR BALANCE\n
        OPCIÓN 2 - DEPOSITAR DINERO\n
        OPCIÓN 3 - RETIRAR DINERO\n
        OPCIÓN 4 - SALIR DE LA CUENTA\n
    )))
        while  opcion != 4:
                if opcion == 1:
                    print(imprimir_balance())
                elif opcion == 2:
                    print(depositar())
                elif opcion == 3:
                    print(retirar())
                elif opcion == 4:
                    print(salir())
            else: 
                    print('La opción solicitada no está disponible en estos momentos.')
        return(balance)
    

while not operacion_terminada:
    print('Seleccionar operación deseada\n')
    print('Su saldo es de: '+{balance})
    operacion = seleccionar_operacion()

'''