from os import *
from clientes import *
from empleado import *
from registro import *
from zona import *
from animal import *
from entradas import *
from interfaces import *
import pygame
cancion = "zoo_ambiente.mp3"
cancion2 = "sonido_animal.mp3"
pygame.init()
pygame.mixer.init()
while True:
    try:
        pygame.mixer.music.load(cancion)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
    except:
        system('cls')
        print(principio)
        hacer=input(':')
        system('cls')
        match hacer:
            case '1':
                pygame.mixer.music.load(cancion2)
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                print(entradas)
                entrada()
                while True:
                    system('cls')
                    print(mensaje)
                    print(inter,'   Modo visita  ',inter_c,'Menu inicial',inter_zoo)
                    hacer=input('(0 Para salir): ')
                    match hacer:
                        case '1':
                            system('cls')
                            zona=sabana
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '2':
                            system('cls')
                            zona=desierto
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '3':
                            system('cls')
                            zona=taiga
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '4':
                            system('cls')
                            zona=selva
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '5':
                            system('cls')
                            zona=pajarera
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '6':
                            system('cls')
                            zona=acuario
                            zona.ver_zona()
                            zona.ver_animales_exp()
                        case '7':
                            system('cls')
                            todas.ver_animales_expt()
                        case '0':
                            break
            case '2':

                while True:
                    system('cls')
                    print(inter,'   Modo admin   ',inter_c,'menu inicial',inter_admin)
                    hacer=input('(0 Para salir): ')
                    match hacer:

                        case '1':
                            system('cls')
                            print(color1+'Clientes'+Fore.RESET)
                            print(f'\t{color}1.{Fore.RESET}Eliminar clientes\n\t{color}2.{Fore.RESET} Ver clientes')
                            hacer=input(':')
                            match hacer:
                                case '1':
                                    system('cls')
                                    eliminar_usu()
                                case '2':
                                    if registros.nombres!=[]:
                                        system('cls')
                                        print(f'''{color1}
        ░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗███████╗░██████╗
        ██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔════╝
        ██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
        ██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
        ╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░███████╗██████╔╝
        ░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░{Fore.RESET}''')
                                        
                                        ver_t()
                                        input()
                                    else:
                                        input('No hay clientes para mostrar')                 
                        case '2':
                            system('cls')
                            print(color1+'Empleados'+Fore.RESET)
                            print(f'\t{color}1.{Fore.RESET}Contratar empleado\n\t{color}2.{Fore.RESET} Ver empleados\n\t{color}3.{Fore.RESET} Despedir empleados')
                            hacer=input(':')
                            match hacer:
                                case '1':
                                    contratar_empleado(dni=input('DNI del empleado: '), nombre=input('Nombre del empleado: '), tarea=input('Tarea para la que se le contrata: ') )
                                    input()
                                case '2':
                                    mostrar_empleados()
                                    input()
                                case '3':
                                    despedir_empleado()
                        case '3':
                            system('cls')
                            print(color1+'Animales'+Fore.RESET)
                            print(f'\t{color}1.{Fore.RESET} Agregar animal\n\t{color}2.{Fore.RESET} Ver animales')
                            hacer=input(':')
                            match hacer:
                                case '1':
                                    zonas.escoger_zonas()
                                    input()
                                case '2':
                                    todas.ver_animales_expt()
                                
                        case '4':
                            system('cls')
                            print('Estas son todas las ganancias: ')
                            print('--------------------------------')
                            print('Ganancias con entradas para niños: '+str(registros.ganancias_n)+'€')
                            print('Ganancias con entradas para adultos: '+str(registros.ganancias_e)+'€')
                            print('Ganancias con entradas para grupos: '+str(registros.ganancias_g)+'€')
                            print('')
                            print('Total de ganancias: '+str(registros.ganancias)+'€')
                            input()

                        case '5':
                            system('cls')
                            print(color1+'Zonas'+Fore.RESET)
                            print(f'\t{color}1.{Fore.RESET} Agregar zona\n\t{color}2.{Fore.RESET} Mostrar zonas')
                            hacer=input(':')
                            match hacer:
                                case '1':
                                    system('cls')
                                    comodin=zonas.crear_zona(input('Nombre de la zona: '),comprueba(input('¿Cuantos animales caben?: ')),input('Clima: ')) 
                                    input()       
                                case '2': 
                                    system('cls')
                                    zonas.mostrar_zonas()
                                    zonas.escoger_zonas_v()
                                    
                                    
                        case '0':
                            break


