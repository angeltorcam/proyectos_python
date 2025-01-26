from registro import *
from PIL import Image

class Animal:
    def __init__(self, nombre,especie,dieta,habitat,enlace):
        self.especie = especie.title()
        self.nombre = nombre
        registros.animales[self.nombre]=especie
        self.dieta=dieta
        self.enlace=enlace
        self.habitat=habitat

    def ver_animal(self):
    # Abre una imagen
        print('')
        input(f'{self.especie} animal que se alimenta principalmente de {self.dieta} y que en el zoo lo llamamos {self.nombre}, habita en {self.habitat}. Adjuntamos imagen ')
        if self.enlace!=None:
            imagen = Image.open(f"{self.enlace}")

            # Muestra la imagen
            imagen.show()
            input()
        else:
            input('No hay imagenes para mostar')
    
