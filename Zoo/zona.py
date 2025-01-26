from registro import *
from animal import *
from os import *
from PIL import Image

class Zona:
    def __init__(self, nombre=None, capacidad=None,clima=None,enlace=None):
        self.nombre = nombre
        self.capacidad = capacidad
        self.animales = []
        self.animalitos=[]
        self.enlace= enlace
        self.clima= clima

    def agregar_animal(self, animal,especie,dieta,habitat,enlace=None):
        if len(self.animales) < self.capacidad:
            ani=animal
            ani = Animal(animal,especie,dieta,habitat,enlace)
            self.animales.append(ani)
            registros.animales_o.append(ani)
            self.animalitos.append(especie)
            print(f"{ani.nombre} ha sido añadido a la zona {self.nombre}.")
        else:
            input(f"La zona {self.nombre} está llena.")
            
    def ver_animales_exp(self):

        print('Animales en este habitat:')
        print('Nombre        Especie')
        print('---------------------------------')
        for i,j in registros.animales.items():
            if j in self.animalitos:
                print(f'{i}       {j}')
        
        animal=input('¿De que animal quieres obtener informacion? (Indica su especie, si no desea ver a ningun animal pulse Enter): ').title()
        system('cls')
        if animal!='':
            if animal in self.animalitos:
                for i in self.animales:
                    if i.especie==animal:
                        i.ver_animal()
            else:
                input('Animal no encontrado o mal indicado ')
    def ver_animales_expt(self):
        cont=0
        print('Estos son todos los animales que hay en el zoo:')
        print('Nombre        Especie')
        print('---------------------------------')
        for i,j in registros.animales.items():
            print(f'{i}       {j}')
        
        animal=input('¿De que animal quieres obtener informacion? (Indica su especie, si no desea ver a ningun animal pulse Enter): ').title()
        system('cls')
        if animal!='':
            for i in registros.animales_o:
                if i.especie==animal:
                    i.ver_animal()
                else:
                    cont+=1
            if cont==len(registros.animales):
                input('Animal no encontrado o mal indicado ')
    def ver_zona(self):
            input(f"La zona conocida como {self.nombre} tiene capacidad para albergar a {self.capacidad} animales. Esta posee un clima {self.clima}. Ajuntamos foto.")
            if self.enlace!=None:
                imagen = Image.open(f"{self.enlace}")

            # Muestra la imagen
                imagen.show()
            else:
                print('No hay imagenes para mostrar')
            print('En esta zona podras ver: ')
            print('')



class Zoo():
  
    def crear_zona(self, nombre=None, capacidad=None,clima=None,enlace=None):
        if nombre in registros.zonas:
            input("Ya existe una zona con ese nombre.")
        else:
            zona=nombre
            zona = Zona(nombre, capacidad,clima,enlace)
            registros.zonas[nombre] = zona
            print(f"Se ha creado la zona {zona.nombre} con capacidad para {zona.capacidad} animales.")
            return zona

    def mostrar_zonas(self):
        print("Zonas del zoo:")
        for nombre, zonaita in registros.zonas.items():
            if nombre!=None:
                print(f"{nombre}: {len(zonaita.animales)} animales")

    def escoger_zonas(self):
        print("Zonas del zoo:")
        for nombre in registros.zonas:
            if nombre!=None:
                print(f"{nombre}")
        
        escoge=input('Indica a que zona se va agrgara el animal (escribe el nombre): ')
        if escoge in registros.zonas:
            zona_vip=registros.zonas[escoge] 
            zona_vip.agregar_animal( animal=input('Nombre del animal: '), especie=input('Indique la especie del animal: '), dieta=input('Dieta del animal: '),habitat=escoge ,enlace=None)
        else:
            input('Zona no identificada')
    def escoger_zonas_v(self):
        print("Zonas del zoo:")
        
        
        escoge=input('Indica a que zona que desea ver (escribe el nombre): ')
        if escoge in registros.zonas:
            zona_vip=registros.zonas[escoge] 
            zona_vip.ver_zona()
            zona_vip.ver_animales_exp()
        else:
            input('Zona no identificada')

    

        
        
zonas= Zoo()
todas=zonas.crear_zona()
sabana=zonas.crear_zona('la sabana',10,'tropical','imagenes/sabana.jpg')
selva=zonas.crear_zona('la selva',10,'humedo y frondoso rodeado de vegetacion','imagenes/selva.jpg')
pajarera=zonas.crear_zona('la pajarera',10,'mediterraneo perfecto para aves','imagenes/pajarera.jpg')
desierto=zonas.crear_zona('el desierto',10,'muy arido y seco','imagenes/desierto.jpg')
acuario=zonas.crear_zona('el acuario',10,'acuatico donde hay corales,anemonas...','imagenes/acuario.jpg')
taiga=zonas.crear_zona('la taiga',10,'frio donde se pueden encontrar rios y con mucha vegtacion','imagenes/taiga.jpg')

sabana.agregar_animal('Mufasa','Leon','carne',sabana.nombre,'imagenes/leon.jpg')
sabana.agregar_animal('Benga ','Tigre','carne',sabana.nombre,'imagenes/tigre.jpg')
sabana.agregar_animal('Tanque','Bufalo','plantas',sabana.nombre,'imagenes/bufalo.jpg')
sabana.agregar_animal('Paso  ','Cebra','plantas',sabana.nombre,'imagenes/cebra.jpg')
sabana.agregar_animal('Picudo','Rinoceronte','plantas',sabana.nombre,'imagenes/rinoceronte.jpg')

selva.agregar_animal('Homero','Galago','bichos',selva.nombre,'imagenes/galago.jpg')
selva.agregar_animal('Jorge ','Mono','frutas',selva.nombre,'imagenes/mono.jpg')
selva.agregar_animal('Coche ','Jaguar','carne',selva.nombre,'imagenes/jaguar.jpg')
selva.agregar_animal('Bicha ','Serpiente','carne',selva.nombre,'imagenes/serpiente.jpg')

desierto.agregar_animal('Chepa',' Camello','plantas',desierto.nombre,)
desierto.agregar_animal('Cocota','Cocodrilo','carne',desierto.nombre,'imagenes/cocodrilo.jpg''imagenes/camello.jpg')
desierto.agregar_animal('Robert','Canguro','plantas',desierto.nombre,'imagenes/canguro.jpg')
desierto.agregar_animal('David ','Diablo Espinoso','bichos',desierto.nombre,'imagenes/diablo_espinoso.jpg')
desierto.agregar_animal('Fran  ','Avestruz','de todo',desierto.nombre,'imagenes/avestruz.jpg')

acuario.agregar_animal('Focon ','Foca','peces',acuario.nombre,'imagenes/foca.jpg')
acuario.agregar_animal('Ferran','Tiburon','peces y carne',acuario.nombre,'imagenes/tiburon.jpg')
acuario.agregar_animal('Olga  ','Orca','peces y carne',acuario.nombre,'imagenes/orca.jpg')
acuario.agregar_animal('Fin   ','Delfin','peces',acuario.nombre,'imagenes/delfin.jpg')
acuario.agregar_animal('Cabeza','Pulpo','crustaceos',acuario.nombre,'imagenes/pulpo.jpg')

taiga.agregar_animal('Pardo ','Oso','de todo',taiga.nombre,'imagenes/oso.jpg')
taiga.agregar_animal('Lola  ','Lobo','carne',taiga.nombre,'imagenes/lobo.jpg')
taiga.agregar_animal('Albin ','Ardilla','frutos secos',taiga.nombre,'imagenes/ardilla.jpg')
taiga.agregar_animal('Copi  ','Conejo','plantas y verduras',taiga.nombre,'imagenes/conejo.jpg')
taiga.agregar_animal('Bango ','Alce','plantas y verduras',taiga.nombre,'imagenes/alce.jpg')

pajarera.agregar_animal('Rata  ','Buitre','caarroña',pajarera.nombre,'imagenes/buitre.jpg')
pajarera.agregar_animal('Real  ','Aguila','carne',pajarera.nombre,'imagenes/aguila.jpg')
pajarera.agregar_animal('Avion ','Condor','carne',pajarera.nombre,'imagenes/condor.jpg')
pajarera.agregar_animal('Noche ','Buho','carne',pajarera.nombre,'imagenes/buho.jpg')
pajarera.agregar_animal('Balcon','Halcon','carne',pajarera.nombre,'imagenes/halcon.jpg')
system('cls')




