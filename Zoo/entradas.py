from registro import *
from clientes import *

entrada_a=10
descuento_niños=7
descuento_grupo=8


def entrada():
    importe=0
    personas=input('Cuantas entradas vas a comprar: ')
    personas=comprueba(personas)
    
    if personas>=5:
        for k in range(personas):
            registrar()
        
        for j in registros.nombres:
            if j.pagado==False:
                if j.edad<18:
                    importe+=descuento_niños
                    registros.ganancias_n+=importe
                else:
                    importe+=descuento_grupo
                    registros.ganancias_g+=importe
                
            j.pagado=True

    else:
        for k in range(personas):
            registrar()
        
        for j in registros.nombres:
            if j.pagado==False:
                if j.edad<18:
                    importe+=descuento_niños
                    registros.ganancias_n+=importe
                
                else:
                    importe+=entrada_a
                    registros.ganancias_e+=importe
                
            j.pagado=True
    
    input(f'El importe total son {importe}€')
    input('Que disfruten')
    registros.ganancias+=importe
                