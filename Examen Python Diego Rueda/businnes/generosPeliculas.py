import json
import os

def guardarGeneros_json():
    try:
      with open(os.path.join("data","generosPeliculas.json"), 'w') as archivo_json:
        json.dump(listaGeneros, archivo_json, indent=2)
        print("La lista de Generos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Generos guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
        
def listarGeneros():
  print("Listado de generos: ")
  for genero in listaGeneros:
    print(genero)
        
def cargarGenerosjson():
    try:
        with open(os.path.join("data","generosPeliculas.json"), 'r') as archivo_json:        
            listaGeneros = json.load(archivo_json)
            print("La lista de Generos ha sido cargada")
            return listaGeneros
    except FileNotFoundError:
        print("El archivo 'generosPeliculas.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []
  
listaGeneros = cargarGenerosjson()

def crearGeneros():
    print("Ingrese los datos del nuevo Formato")
    idn = input("Ingrese el identificador del Genero: ")
    gen = input("Ingrese el Genero: ")
    
    genero = { 
              idn:{
        'ID':idn,
        'Genero': gen
        }
    }

    listaGeneros.append(genero)
    print("Se creó el Genero con éxito")
    guardarGeneros_json()

def modificarGeneros():
    if not listaGeneros:
        print("No hay Generos registrados.")
        return

    genName = input("Ingrese el nombre del Genero que desea modificar: ")

    for genero in listaGeneros:
        if genero['Aula'] == genName:
            print(f"Datos actuales del Genero {genName}:")
            print(genero)
            dato_a_modificar = input("¿Qué dato desea modificar? (ID/Genero): ").lower()

            if dato_a_modificar == "id":
                nuevo_valor = input("Nuevo ID: ")
                if nuevo_valor:
                    genero['ID'] = nuevo_valor
            elif dato_a_modificar == "Genero":
                nuevo_valor = input("Nuevo Genero : ")
                if nuevo_valor:
                    genero['Genero'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Genero modificado con éxito.")
      
            guardarGeneros_json()
            return

    print(f"No se encontró un genero con el nombre {genName}.")