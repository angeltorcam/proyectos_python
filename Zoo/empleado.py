from registro import *
from os import *

class Empleado():
    def __init__(self, nombre, tarea, dni):
        self.nombre = nombre
        self.tarea = tarea
        self.dni = dni

def mostrar_empleados():
    if registros.nombre_e!=[]:
        for i in registros.nombre_e:
            print('------------------------------------------')
            print(f'Nombre = {i.nombre}')
            print(f'DNI = {i.dni}')
            print(f'Tarea = {i.tarea}')
            print('------------------------------------------')

def contratar_empleado( nombre, tarea, dni):
    if  dni in registros.dnis_e:
        print('Ya hay un empleado con es DNI')
    else:
        empleado = Empleado(nombre, tarea,dni)
        registros.dnis_e.append(empleado.dni)
        registros.nombre_e.append(empleado)
        print(f"{empleado.nombre} ha sido contratado para {empleado.tarea}.")

def despedir_empleado():
    #busco usuario
    mostrar_empleados()
    
    empleado=input('¿Que empleado quieres eliminar? Escriba su dni: ')
    if empleado in registros.dnis_e:
        for j in registros.nombre_e:
            # lo encuentro y lo borro
            if j.dni==empleado:
                input('empleado despedido')
                registros.dnis_e.remove(empleado)
                registros.nombre_e.remove(j)
                j=Empleado(None,None,None)
    else:
        print('DNI invalido')

contratar_empleado('Francisco rubiño','Barrendero','111')
contratar_empleado('Angel Tortosa','Gerente','112')
contratar_empleado('Alfonso Ruiz','Especialista en mantenimiento animal','122')
contratar_empleado('Juan Castillos','Veterinario','121')
system('cls')


