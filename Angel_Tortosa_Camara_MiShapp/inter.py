from interfaces import *
from colorama import Back, Fore, init
import os


credit=True
i=0
abecedario='qwertyuioplkjhgfdsazxcvbnm<-,_:;>+-*/¡¿"()&%$!?.'
n=-1
p=0
nom='  Usuario  '
usuario=False
usu_g='Soy_MiShapp@gesto.com'
contra_g='homeroponmeun10'
gestor=False
user={}
carrito={}
devoluciones={}
pedidos_pr={}
saldo=0
prendas_espe=[]
prendas=['sudadera','pantalon de chandal','vaqueros','pantalon corto','vaqueros cortos''camiseta','chaqueta','chaqueta vaquera']
precios={'sudadera':12,'pantalon de chandal':10,'vaqueros':15,'pantalon corto':7,'vaqueros cortos':12,'camiseta':5,'chaqueta':17,'chaqueta vaquera':20}
cantidades={'sudadera':100,'pantalon de chandal':100,'vaqueros':100,'pantalon corto':100,'vaqueros cortos':100,'camiseta':100,'chaqueta':100,'chaqueta vaquera':100}
reseñas=['Muy buen programa sin duda un gran trabajo','Este programa me ha cambiado la vida haciendomela comodisima','Buen trabajo seguro que el maestro te pone un 10']

def descripcion(prenda,precio,cantidad):
    print(f'{prenda.title()} prenda comoda con un precio de {precio}€, esta es ideal para vestirla en diferentes ocasiones, ¡Incluso todos los dias!\nQuedan {cantidad} en stock\nPara comprar pulse 1,\n2 para añadir al carrito, y cualquier otra tecla para salir')
def compra(prenda,precio,cantidad,nom,usuario,saldo,pedidos_pr):
   
    if usuario==True:
        seguridad=input('Esta se guro que quieres comprar, escriba "si" para continuar la compra: ').lower()
        if seguridad=='si':
            user[nom].append(prenda)
            if saldo >= precios[prenda] and cantidades[prenda]>0:
                saldo=saldo-precios[prenda]
                cantidades[prenda]-=1
                pedidos_pr[nom].append(precios[prenda])
                print(Fore.GREEN+'Muchas gracias por comprar en MiShapp'+Fore.RESET)
                input()
                return saldo
            elif saldo<precios[prenda]:
                print('no tienes saldo suficiente')
                input()
                return saldo
            else:
                print('No quedan prendas en stock')
                input()
                return saldo
    else:
        print('Debes iniciar sesion primero')
        input()
        return saldo  
def carritillo(prenda,carrito,nom,usuario):
    if usuario==True:
        carrito[nom].append(prenda)
        print(Fore.BLUE+'Añadido al carrito con exito'+Fore.RESET)
        input()
    else:
        print('Debes iniciar sesion primero')
        input()
def comprueba(acc):
    while not acc.isdigit():
        acc=input('Debe ser un numero: ')
    
    acc=int(acc)
    return acc

while True:
    nom_m='      MENU      '
    os.system('cls')
    print(inter,nom_m,inter_c,nom,inter_m)
    acc_menu=input('¿Que quieres hacer?: ')

    match acc_menu:
        case '1':
            while True:
                nom_m='     VENTAS     '
                os.system('cls')
                print(inter,nom_m,inter_c,nom,inter_v)
                acc_v=input('¿Que quieres hacer? Pulse cualquier otra cosa paras salir: ')
                match acc_v:
                    case '1':
                        prenda='sudadera'
                        nom_m='   SUDADERAS    '
                        while True:
                            os.system('cls')
                            print(inter,nom_m,inter_c,nom,inter_s)
                            acc_sud=input('Elige una o escriba cualquier otra cosa para salir: ')
                            match acc_sud:
                                case '1':

                                    os.system('cls')
                                    color_obj=Fore.RED
                                    print(color_obj+sudadera+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                        
                                case '2':
                                
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+sudadera+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '3':
                                    os.system('cls')
                                    color_obj=Fore.MAGENTA
                                    print(color_obj+sudadera+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '4':
                                    os.system('cls')
                                    color_obj=Fore.WHITE
                                    print(color_obj+sudadera+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case _:
                                    break
                    case '2':
                        nom_m=' PANTALON LARGO '
                        while True:
                            os.system('cls')
                            print(inter,nom_m,inter_c,nom,inter_pan)
                            acc_sud=input('Elige una o escriba cualquier otra cosa para salir: ')
                            match acc_sud:
                                case '1':
                                    prenda='pantalon de chandal'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+pantalon+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '2':
                                    prenda='pantalon de chandal'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+pantalon+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '3':
                                    prenda='vaqueros'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+vaqueros+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '4':
                                    prenda='vaqueros'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+vaqueros+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case _:
                                    break
                    case '3':
                        nom_m=' PANTALON CORTO '
                        while True:
                            os.system('cls')
                            print(inter,nom_m,inter_c,nom,inter_pan)
                            acc_sud=input('Elige una o escriba cualquier otra cosa para salir: ')
                            match acc_sud:
                                case '1':
                                    prenda='pantalon corto'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+corto+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '2':
                                    prenda='pantalon corto'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+corto+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '3':
                                    prenda='vaqueros cortos'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+vaque_c+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '4':
                                    prenda='vaqueros cortos'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+vaque_c+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case _:
                                    break
                    case '4':
                        nom_m='    CAMIESETA   '
                        while True:
                            os.system('cls')
                            print(inter,nom_m,inter_c,nom,inter_ca)
                            acc_sud=input('Elige una o escriba cualquier otra cosa para salir: ')
                            match acc_sud:
                                case '1':
                                    prenda='camiseta'
                                    os.system('cls')
                                    color_obj=Fore.RED
                                    print(color_obj+camiseta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '2':
                                    prenda='camiseta'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+camiseta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '3':
                                    prenda='camiseta'
                                    os.system('cls')
                                    color_obj=Fore.MAGENTA
                                    print(color_obj+camiseta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '4':
                                    prenda='camiseta'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+camiseta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case _:
                                    break
                    case '5':
                        nom_m='   CHAQUETAS    '
                        while True:
                            os.system('cls')
                            print(inter,nom_m,inter_c,nom,inter_ch)
                            acc_sud=input('Elige una o escriba cualquier otra cosa para salir: ')
                            match acc_sud:
                                case '1':
                                    prenda='chaqueta'
                                    os.system('cls')
                                    color_obj=Fore.RED
                                    print(color_obj+chaqueta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '2':
                                    prenda='chaqueta'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+chaqueta+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '3':
                                    prenda='chaqueta vaquera'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTBLUE_EX
                                    print(color_obj+chaqueta_v+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case '4':
                                    prenda='chaqueta vaquera'
                                    os.system('cls')
                                    color_obj=Fore.LIGHTWHITE_EX
                                    print(color_obj+chaqueta_v+Fore.RESET)
                                    descripcion(prenda,precios[prenda],cantidades[prenda])
                                    acc_obj=input(':')
                                    if acc_obj=='1':
                                        saldo=compra(prenda,precios[prenda],cantidades[prenda],nom,usuario,saldo,pedidos_pr)
                                    if acc_obj=='2':
                                        carritillo(prenda,carrito,nom,usuario)
                                case _:
                                    break
                    case '6':
                        os.system('cls')
                        if prendas_espe==[]:
                            print('No hay prendas especiales aun')
                            input()
                        else:
                            print('Estas son las prendas especiales')
                            j=0
                            for i in prendas_espe:
                                j+=1
                                print(f'{j}, {i} un precio de {precios[i]}€, quedan {cantidades[i]}')
                            print('Estas son las prendas añadidas recientemente')
                            acc_obj=input('Para comprar una de estas prendas pulsa 1, pulsa 2 para añadirla al carrito: ')
                            
                            if acc_obj=='1':
                                elec=input('Que prenda de las que tenemos quieres comprar, indicala con el numero de su derecha: ')
                                elec=comprueba(elec)
                                
                                prenda_esp=prendas_espe[elec-1]
                                saldo=compra(prenda_esp,precios[prenda_esp],cantidades[prenda_esp],nom,usuario,saldo,pedidos_pr)
                            if acc_obj=='2':
                                carritillo(prenda_esp,carrito,nom,usuario)
                    case _:
                        break

        case '2':
                nom_m='    Usuarios    '
                while True:
                    os.system('cls')
                    print(inter,nom_m,inter_c,nom,inter_us)
                    acc_usu=input('Que quieres hacer: ')
                    os.system('cls')
                    match acc_usu:
                        case '1':
                            if usuario==True:
                                os.system('cls')
                                saldo=str(saldo)
                                saldoapa=saldo
                                while lon2<=10:
                                    saldoapa=' '+saldoapa
                                    lon2=len(saldoapa)
                                
                                lon=len(saldoapa)    
                                
                                saldoapa=saldoapa+'€'
                                while lon<21 :
                                    saldoapa=saldoapa+' '
                                    lon=len(saldoapa)
                                nom_m='    PERFILES    '
                                print(inter,nom_m,inter_c,nom,tarjeta(numero,saldoapa))
                                input()
                                os.system('cls')
                                saldo=int(saldo)
                            else:
                                print('inicia el usuario')
                                input()
                                os.system('cls')
                        case '2':
                            os.system('cls')
                            while True:
                                print(f'''                                        {color}╔═══════════════════════╗
                                        ║  {quitar} USUARIO DE GESTOR   {color}║
                                        ╚═══════════════════════╝{quitar}''')
                                usu_ge=input('Pon 0 para salir:')
                                if usu_g==usu_ge or usu_ge=='0':
                                    break
                                else:
                                    print('Usuario incorrecto')
                                    input()
                                    os.system('cls')
                                
                            while True:
                                print(f'''                                        {color}╔═══════════════════════╗
                                        ║  {quitar}CONTRASEÑA DE GESTOR {color}║
                                        ╚═══════════════════════╝{quitar}''')
                                contra=input('Pon 0 para salir:')
                                if  contra==contra_g:
                                    usuario=False
                                    print(Fore.BLUE+'Mod gestor activado'+Fore.RESET+' para salir inicie sesion con otro usuario')
                                    nom='   Gestor  '
                                    gestor=True
                                    input()
                                    break
                                elif contra=='0':
                                    break
                                else:
                                    print('Contraseña incorrecta')
                                    input()
                                    os.system('cls')
                        case '3':
                            while True:
                                print(f'''                                        {color}╔═══════════════════════╗
                                        ║  {quitar}CORREO ELECTRONICO   {color}║
                                        ╚═══════════════════════╝{quitar}''')
                                
                                correo=input(': ')
                                if ('@' in correo) and ('.com'in correo or '.es' in correo):
                                    break
                                else:
                                    print('El correo debe estar compuesto de una "@" y ".com" o ".es"')
                                    input()
                                    os.system('cls')
                            while True:
                                print(f'''                                        {color}╔═══════════════════════╗
                                        ║{quitar}   NOMBRE DE USUARIO   {color}║
                                        ╚═══════════════════════╝{quitar}''')
                                nom=input('(maximo 10 caracacteres): ')
                                lon=len(nom)
                                if lon>0 and lon<11:
                                    lon2=int(lon/2)
                                    while lon2<=6:
                                        nom=' '+nom
                                        lon2=len(nom)
                                    lon=len(nom)    
                                    
                                    while lon<11 :
                                        nom=nom+' '
                                        lon=len(nom)
                                    break
                                else:
                                    print('El nombre debe ser mas corto') 
                                    input() 
                                    os.system('cls')
                            
                            
                            credit=True
                            p=0
                            n=-1
                            while credit==True:
                                
                                print(f'''                                        {color}╔═══════════════════════╗
                                        ║{quitar}  TARJETA DE CREDITO   {color}║
                                        ╚═══════════════════════╝{quitar}''')
                                tarjet=input('16 digitos: ')
                                lon=len(tarjet)
                                if lon==16:
                                    while True:
                                        n+=1
                                        if tarjet=='':
                                            n=-1
                                            p=0
                                            print('Debes introducir un numero')
                                            input() 
                                            os.system('cls')
                                            n=-1
                                            p=0
                                            break
                                        elif tarjet[n] in abecedario  :
                                            n=-1
                                            p=0
                                            print('Debes introducir un numero') 
                                            input()
                                            os.system('cls')
                                            n=-1
                                            p=0
                                            break   
                                        else:
                                            p=p+1
                                        if p==lon and tarjet!='':
                                            credit=False
                                            break
                                else:
                                    print('La tarjeta debe de tener dieciseis digitos')
                                    input()
                                    os.system('cls')
                            k=0
                            numero=' '
                            i=0
                            while i<lon:
                                if k==4:
                                    k=0
                                    numero=numero+' '
                                else:
                                    numero=numero+tarjet[i]
                                    k+=1
                                    i+=1
                            p=0
                            n=-1
                            credit=True
                                                         
                            print(f'''                                        {color}╔═══════════════════════╗
                                        ║{quitar}         SALDO   {color}      ║
                                        ╚═══════════════════════╝{quitar}''')
                            saldo=input(': ')
                            saldo=comprueba(saldo)
                                
                            usuario=True
                            gestor=False
                            if not nom in user:
                                user[nom]=[]
                                carrito[nom]=[]
                                devoluciones[nom]=[]
                                pedidos_pr[nom]=[]
                        case _:
                            break
        case '3':
            
            
            while True:
                os.system('cls')
                importe=0
                nom_m='  FACTURACION   '
                print(inter,nom_m,inter_c,nom,inter_fact)
                if usuario==False:
                    print('Carrito vacio')
                    input()
                    break
                elif carrito[nom]==[]:
                    print('carrito vacio')
                    input()
                    break
                else:
                    print('Estos son todos los elementos que has añadido al carrito')
                    for prenda in carrito[nom]:
                        print(prenda)
                        importe=importe+precios[prenda]
                    print(f'Tiene un coste actual de {importe}€')
                    acc_obj=input('Para pagarlos pulse 1, pulse 2 para eliminar objetos del carrito, y cualquier otra tecla para salir: ')
                
                    if acc_obj=='1':
                        pedido=' '
                        if usuario==True:
                            seguridad=input('Esta se guro que quieres comprar, escriba "si" para continuar la compra: ').lower()
                            if saldo>=importe and seguridad=='si':
                                for prenda in carrito[nom]:
                                    saldo=saldo-importe
                                    cantidades[prenda]-=1
                                    
                                    pedido=f'{pedido}, {prenda}'
                                user[nom].append(pedido)
                                pedidos_pr[nom].append(importe)
                                print(Fore.GREEN+'Muchas gracias por comprar en MiShapp'+Fore.RESET)
                                carrito[nom]=[]
                                input()
                            if saldo<importe:
                                print('No dispones de suficiente saldo')
                        else:
                            print('Inicia sesion primero')
                    elif acc_obj=='2':
                        acc_obj=input('Quieres eliminar algun elemento del carrito, escriba "si" para eliminar algo: ').lower()
                        if acc_obj=='si':
                            print('Que qieres eliminar')
                            for prenda in enumerate(carrito[nom],start=1):
                                print(prenda)
                            acc_obj=input('Escriba el numero que aparece a la derecha: ')
                            while not acc_obj.isdigit():
                                acc_obj=input('Escriba el numero que aparece a la derecha: ')
                            acc_obj=int(acc_obj)
                            lon=len(carrito[nom])

                            if acc_obj<=lon and acc_obj>0:
                                carrito[nom].remove(carrito[nom][acc_obj-1])
                                print('eliminado con exito')
                                input()
                            else:
                                print('No se ha podido completar la eliminacion vuelva a intentarlo')
                    else:
                        break
                
        case '4':
            os.system('cls')
            nom_m='  DEVOLUCIONES  '
            print(inter,nom_m,inter_c,nom,inter_dev)
            if usuario==False:
                print('No has realizado ningun pedido')
            else:
                print('Estos son tus pedidos realizados hasta la fecha')
                lon=len(user[nom])
                for pedido in enumerate(user[nom],start=1):
                    print(pedido)
                print('Quieres hacer alguna devolucion, escriba "si" para realizar alguna devolucion')
                acc_obj=input(':').lower()
                if acc_obj=='si':
                    print('Que pedido quieres devolver')
                    acc_obj=input(':')
                    while (not acc_obj.isdigit()) and (acc_obj<=lon+1) and (acc_obj>0):
                        print('Debes escribir un numero que aparezaca en la lista')
                        acc_obj=input(':')
                    seguro=input('Seguro que quieres relizar esta devolucion, escriba si para continuar: ')
                    if seguro=='si':
                        acc_obj=int(acc_obj)
                        devoluciones[nom].append(user[nom][acc_obj-1])
                        user[nom].remove(user[nom][acc_obj-1])
                        saldo=saldo+pedidos_pr[nom][acc_obj-1]
                        pedidos_pr[nom].remove(pedidos_pr[nom][acc_obj-1])
                        print(Fore.GREEN+'Pedido devuelto y saldo rembolasado'+Fore.RESET)
                        

            input()
        case '5':
            os.system('cls')
            if gestor==True:
                while True:
                    os.system('cls')
                    nom_m='   INVENTARIO   '
                    print(inter,nom_m,inter_c,nom,inter_ges)
                    acc_obj=input('Que quieres hacer, cualquier otra cosa para salir: ')
                    match acc_obj:
                        case '1':
                            print('Estas son todas las prendas que estan disponibles en la tienda: ')
                            for j in precios:
                                print(j)
                            print('En MiShapp tienes la posibilidad de añadir prendas para vender: ')
                            add=input('Quieres añadir alguna para probarla, escribe si para añadir: ').lower()
                            if add=='si':
                                os.system('cls')
                                prenda_esp=input('Como se llamara tu prenda: ')
                                prendas_espe.append(prenda_esp)
                                while True:
                                    pr=input('Que precio tendra: ')
                                    pr=comprueba(pr)
                                    if pr>0:
                                        break
                                    else:
                                        print('El precio debe ser mayor a 0')
                                precios[prenda_esp]=pr
                                cant=input('Cuantas unidades de esta prenda quieres poner a la venta: ')
                                cant=comprueba(cant)
                                cantidades[prenda_esp]=cant
                                os.system('cls')
                                print(Fore.GREEN+'Prenda añadida con exito'+Fore.RESET)
                                input()
                        case '2':
                            print('Estas son todas las prendas que estan disponibles en la tienda: ')
                            i=0
                            for j in prendas:
                                i+=1
                                print(f'{i}, {j}')
                            if prendas_espe!=[]:
                                i+=1
                                for j in prendas_espe:
                                    print(f'{i}, {j}')
                            
                            add=input('Quieres modificar el precio de alguna de ellas, escriba "si" para hacerlo: ').lower()
                            
                            if add=='si':
                                while True:
                                    elec=input('Introduzca la prenda que quiere modificar, indicando el numero de su derecha: ')
                                    elec=comprueba(elec)
                                    lon=len(prendas_espe)
                                    if elec>0 and elec<=7+lon:
                                        if elec<=7:
                                            prenda=prendas[elec-1]
                                            break
                                        else:
                                            prenda=prendas_espe[elec-8]
                                            break
                                while True:
                                    pr=input('Que precio tendra: ')
                                    pr=comprueba(pr)
                                    if pr>0:
                                        break
                                    else:
                                        print('El precio debe ser mayor a 0')

                                seguro=input('Seguro que quieres cambiar el precio de prenda, escriba "si" para finalizar la accion: ').lower()
                                if seguro=='si':
                                    precios[prenda]=pr
                                    print(Fore.GREEN+'Precio cambiado con exito'+Fore.RESET)
                                    input()
                        case '3':
                            print('Estas son todas las prendas que estan disponibles en la tienda: ')
                            i=0
                            for j in prendas:
                                i+=1
                                print(f'{i}, {j}')
                            if prendas_espe!=[]:
                                i+=1
                                for j in prendas_espe:
                                    print(f'{i}, {j}')
                            
                            add=input('Quieres modificar la cantidad de alguna de ellas, escriba "si" para hacerlo: ').lower()
                            if add=='si':
                                while True:
                                    elec=input('Introduzca la prenda que quiere modificar, indicando el numero de su derecha: ')
                                    elec=comprueba(elec)
                                    lon=len(prendas_espe)
                                    if elec>0 and elec<=7+lon:
                                        if elec<=7:
                                            prenda=prendas[elec-1]
                                            break
                                        else:
                                            prenda=prendas_espe[elec-8]
                                            break
                                while True:
                                    pr=input('Que cantidad habra: ')
                                    pr=comprueba(pr)
                                    if pr>0:
                                        break
                                    else:
                                        print('El precio debe ser mayor a 0')
                                seguro=input('Seguro que quieres cambiar la cantidad de la prenda, escriba "si" para finalizar la accion: ').lower()
                                if seguro=='si':
                                    cantidades[prenda]=pr
                                    print(Fore.GREEN+'Cantidad cambiada con exito'+Fore.RESET)
                                    input()
                        case _:
                            break   
            else:
                print('No tienes acceso a esta seccion, para acceder ve a usuarios, modo gestor y introduzca la contraseña y usuario correcto')
                input()
        case '6':
            os.system('cls')
            nom_m='    PEDIDOS     '
            print(inter,nom_m,inter_c,nom,inter_ped)
            if usuario==True:
                lon=len(user[nom])
                if lon>0:
                    print('Estos son tus pedidos realizados hasta la fecha')
                    lon=len(user[nom])
                    for pedido,j in zip(enumerate(user[nom],start=1),pedidos_pr[nom]):
                        print(f'{pedido} su importe fue {j}€\n')
                   
                else:
                    print('No has realizado ningun pedido')
            elif gestor==True:
                os.system('cls')
                print('Estos son todos los usuario hasta la fecha con todos sus pedidos')
                for pedido in (user):
                        print(f'{pedido}, sus pedidos son: ')
                        for i,k in zip(user[pedido], pedidos_pr[pedido]):
                             print(f'{i} su importe fue {k}€\n ')    
            else:
                print('Inicia sesion primero')
                
            input()
        case '7':
            while True:
                os.system('cls')
                nom_m='    RESEÑAS     '
                print(inter,nom_m,inter_c,nom,inter_res)
                acc_obj=input('Que quieres hacer: ')
                if acc_obj=='2':
                    print('Reseñas: ')
                    for j in reseñas:
                        print(j)
                    input()   
                elif acc_obj=='1':
                    print('Añade una reseña')
                    res=input(': ')
                    reseñas.append(res)
                else:
                    break
        case '0':
            os.system('cls')
            print('Gracias por usar MiShapp')
            break    
input()