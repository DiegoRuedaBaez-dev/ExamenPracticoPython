import json
import os
from commons.utils import validar_opcion

def guardarActores():
    try:
      with open(os.path.join("data","actoresPeliculas.json"), 'w') as archivo_json:
        json.dump(listaActores, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
        
def listarActores():
    print("Listado de Actores: ")
    for actores in listaActores:
        print(actores)

def cargarActores():
    try:
        with open(os.path.join("data","actoresPeliculas.json"), 'r') as archivo_json:        
            listaActores = json.load(archivo_json)
            print("La lista de campers ha sido cargada")
            return listaActores
    except FileNotFoundError:
        print("El archivo 'actoresPeliculas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
listaActores = cargarActores()

def crearActor():
    print("Ingrese los datos del nuevo Formato")
    Idn = input("Ingrese el ID del Actor: ")
    actorName = input("Ingrese el apellido del nombre")
    
    actor = { 
             Idn: {
        'ID': actorName,
        'Nombre': actorName,
        }
    }

    listaActores.append(actor)
    print("Se creó el camper con éxito")
    guardarActores()

def modificarActores():
    if not listaActores:
        print("No hay campers registrados.")
        return

    idn_temp = input("Ingrese el identificador del Actor: ")

    for actor in listaActores:
        if actor['ID'] == idn_temp:
            print(f"Datos actuales del campers con identificacion {idn_temp}:")
            print(actor)
            print("1. Modificar ID")
            print("2. Modificar Nombre")
            op = int(input("Ingrese que opcion desea utilizar:"))
            if op == 1:
                nuevo_valor = input("ID: ")
                if nuevo_valor:
                    actor['ID'] = nuevo_valor
            elif op == 2:
                nuevo_valor = input("Nombre: ")
                if nuevo_valor:
                    actor['Nombre'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Camper modificado con éxito.")
      
            guardarActores()
            return

    print(f"No se encontró un campers con el nombre {idn_temp}.")