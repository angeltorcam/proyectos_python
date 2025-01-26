from registro import *
from sqlite3 import * 

class usuario():
    '''Clase que se usa para llevar toda la informacion del usuario'''
    def __init__(self):
        self.dni=None
        self.nombre=None
        self.edad=None
        self.pagado=False

def eliminar_usu():
    #busco usuario
    ver_t()
    
    cliente=input('¿Que usuario quieres eliminar? Escriba su dni: ')
    if cliente in registros.dnis:
        for j in registros.nombres:
            # lo encuentro y lo borro
            if j.dni==cliente:
                input('usuario borrado')
                registros.nombres.remove(j)
                registros.dnis.remove(cliente)
                j=usuario()

def ver_t():
    '''ver toda la informacion de un usuario'''
    if registros.nombres!=[]:
        for i in registros.nombres:
            print(f'DNI: {i.dni}:   Nombre: {i.nombre}    Edad: {i.edad}')
    else:
        input('No hay clientes registrados')

def registrar():
#añado un usuario y lo convierto a objeto
    dni=input('introdizca su dni: ' )
    if dni in registros.dnis:
        input('Ese dni ya ha sido registrado')
    else:
        guardo=dni
        dni=usuario()
        dni.dni=guardo
        dni.nombre=input('Dime tu nombre: ')
        dni.edad=input('Dime tu edad: ')
        dni.edad=comprueba(dni.edad)
        registros.nombres.append(dni)
        registros.dnis.append(guardo)
        registros.edad.append(dni.edad)
        input('cliente registrado')
        print('')

