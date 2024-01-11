import json
import os

def guardarFormatos():
    try:
      with open(os.path.join("data", "formatosPeliculas.json"), 'w') as archivo_json:
        json.dump(listaFormatos, archivo_json, indent=2)
        print("La lista de Formatos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya matriculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
        
def listarFormatos():
  print("Listado de generos: ")
  for formato in listaFormatos:
    print(formato)
        
def cargarFormatos():
    try:
        with open(os.path.join("data", "formatosPeliculas.json"), 'r') as archivo_json:        
            listaFormatos = json.load(archivo_json)
            print("La lista de matriculas ha sido cargada")
            return listaFormatos
    except FileNotFoundError:
        print("El archivo 'formatosPeliculas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
listaFormatos = cargarFormatos()

def crearFormato():
    print("Ingrese los datos del nuevo Formato")
    idn= input("Ingrese el identificador del Formato: ")
    Nombre= input("Ingrese el nombre del formato")
   
    formato = {
        idn:{
        'ID':idn,
        'Nombre': Nombre
        }
    }

    listaFormatos.append(formato)
    print("Se creó la matricula con éxito")
    guardarFormatos()

def modificarMatricula():
    if not listaFormatos:
        print("No hay Matriculass registrados.")
        return

    id_temp = input("Ingrese el numero de identificacion del Formato: ")

    for formato in listaFormatos:
        if formato['Identificacion'] == id_temp:
            print(f"Datos actuales del Matriculas {id_temp}:")
            print(id_temp)
            op = int(input("Ingrese la opcion que desea hacer:"))
            print("1. Modificar ID")
            print("2. Modificar Nombre")
            if op== 1:
                nuevo_valor = input("Nueva ID: ")
                if nuevo_valor:
                    formato['ID'] = nuevo_valor
            elif op== 2:
                nuevo_valor = input("Nuevo nombre: ")
                if nuevo_valor:
                    formato['Nombre'] = nuevo_valor

            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Matriculas modificado con éxito.")
      
            guardarFormatos()()
            return

    print(f"No se encontró un Matriculas con la identificacion {id_temp}.")