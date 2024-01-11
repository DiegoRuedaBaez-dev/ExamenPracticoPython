import json
import os
from commons.utils import *

def guardarPeliculas():
    try:
      with open(os.path.join("data", "mainPeliculas.json"), 'w') as archivo_json:
        json.dump(listaPeliculas, archivo_json, indent=2)
        print("La lista de Peliculas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Peliculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
        
def listarPeliculas():
  print("Listado de generos: ")
  for Pelicula in listaPeliculas:
    print(Pelicula)
        
def cargarPeliculas():
    try:
        with open(os.path.join("data", "mainPeliculas.json"), 'r') as archivo_json:        
            listaPeliculas = json.load(archivo_json)
            print("La lista de Trainers ha sido cargada")
            return listaPeliculas
    except FileNotFoundError:
        print("El archivo 'Trainers.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
listaPeliculas = cargarPeliculas()

def crearPelicula():
    print("Ingrese los datos de la nueva Pelicula")
    idn = input("Ingrese el identificador de la pelicula")
    Nombre= input("Ingrese el nombre de la Pelicula: ")
    Duracion= input("Ingres la duracion de la Pelicula")
    Sinopsis= input("Ingrese la Sinopsis/Resumen de la pelicula")
    Generos= input("Ingrese el horario del Trainer")
    
   
    Pelicula = { "Peliculas": {
         idn:{
          'ID':idn,
          'Nombre': Nombre,
          'Duracion': Duracion,
          'Sinopsis': Sinopsis,
          'Generos': Generos,
        }
      }
    }

    listaPeliculas.append(Pelicula)
    print("Se creó la Pelicula con éxito")
    guardarPeliculas()

def modificarPeliculas():
    if not listaPeliculas:
        print("No hay trainers registrados.")
        return

    idn_temp = input("Ingrese el nombre del trainer que desea modificar: ")

    for Pelicula in listaPeliculas:
        if Pelicula['Nombre'] == idn_temp:
            print(f"Datos actuales del trainer {idn_temp}:")
            print(idn_temp)
            sett = input("¿Qué dato desea modificar? ").lower()
            print("1. Modificar Identificador (ID)")
            print("2. Modificar Nombre (Nombre)")
            print("3. Modificar Duracion (Duracion)")
            print("4. Modificar Sinopsis (Sinopsis)")
            print("5. Modificar Generos (Generos)")
            print("6. Modificar Actores (Actores)")
            print("7. Modificar Formatos (Formatos)")
            
            if sett == "id":
                nuevo_valor = input("Nuevo identificador de la Pelicula ")
                if nuevo_valor:
                    Pelicula['ID'] = nuevo_valor
                    
            elif sett == "nombre":
                nuevo_valor = input("Nuevo nombre de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Nombre'] = nuevo_valor
                    
            elif sett == "duracion":
                nuevo_valor = input("Nueva duracion de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Ruta'] = nuevo_valor
                    
            elif sett == "sinopsis":
                nuevo_valor = input("Nueva sinopsis de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Sinopsis'] = nuevo_valor
                    
            elif sett == "generos":
                nuevo_valor = input("Nuevos generos de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Generos'] = nuevo_valor
                    
            elif sett == "actores":
                nuevo_valor = input("Nuevos actores de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Actores'] = nuevo_valor
                    
            elif sett == "formatos":
                nuevo_valor = input("Nuevos formatos de la pelicula: ")
                if nuevo_valor:
                    Pelicula['Formatos'] = nuevo_valor
      
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Pelicula modificada con éxito.")
      
            guardarPeliculas()
            return

    print(f"No se encontró un trainer con el nombre {idn_temp}.")


def buscarPelicula():
    def buscar_por_id(json_path, palabra_ingresada):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)
                identificacion_coincidente = [entry for entry in data if entry.get('ID') == palabra_ingresada]

                if identificacion_coincidente:
                    print(f"El Trainer con nombre '{palabra_ingresada}' existe. Datos de la Pelicula:")
                    for entry in identificacion_coincidente:
                      
                        print(f"ID: {entry['ID']}, Nombre: {entry['Nombre']}")
                        print(f"Duracion: {entry['Duracion']}")
                        print(f"Sinopsis: {entry['Sinopsis']}")
                        print(f"Generos: {entry['Generos']}")
                        print(f"Actores: {entry['Actores']}")
                        print(f"Formatos: {entry['Formatos']}")
                else:
                    print(f"No hay coincidencias para el numero de identifiacion '{palabra_ingresada}'.")

        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("data", "mainPeliculas.json")
    palabra_ingresada = input("Ingrese el numero de identificador de la Pelicula: ")
    buscar_por_id(json_path, palabra_ingresada)