def comprueba(acc):
    while not acc.isdigit():
        acc=input('Debe ser un numero entero: ')
    
    return int(acc)

class registro():
    def __init__(self) :
        

        #clientes
        self.nombres=[]
        self.dnis=[]

        #animales de cada zona y zona
        self.animales={}
        self.animales_o=[]
        self.zonas={}

        #empleado
        self.dnis_e=[]
        self.nombre_e=[]
        self.edad=[]

        self.ganancias=0
        self.ganancias_n=0
        self.ganancias_e=0
        self.ganancias_g=0
        
    
registros=registro()