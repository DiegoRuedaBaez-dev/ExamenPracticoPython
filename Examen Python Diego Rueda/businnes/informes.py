import json
import os

def infoSpecGen():
    print("Su busqueda especifica por Genero fue:")  
    def nom_ap(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('ID') is not None and entry.get('Genero') is not None for entry in data):
               
                    onlyGen = [(entry['ID'], entry['Genero']) for entry in data]
                    return onlyGen
                else:
                    print("El archivo JSON no tiene la estructura esperada (Genero).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("data","Ingresos.json")

    onlyGens = nom_ap(json_path)

    for Nombre, Apellido in nombres_apellidos:
            print(f"{Nombre} {Apellido}")


def infoSpecName():
    print("Esta es la informacion de la Pelicula por el nombre del actor:")
    def ap(file_path):
        try:
            with open(file_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None and
                       entry.get('NotaT') is not None and entry.get('NotaP') is not None for entry in data):
                   
                    info_campers = [(entry['Nombre'], entry['Apellido'], entry['NotaT'], entry['NotaP']) for entry in data]
                    return info_campers
                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, NotaT, NotaP).")
                    return []
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    json_path = os.path.join("data", "Ingresos.json")

    info_campers = ap(json_path)

    for Nombre, Apellido, NotaT, NotaP in info_campers:
        promedio = (NotaT + NotaP) / 2
        if promedio > 60:
            print(f"{Nombre} {Apellido} - Promedio: {promedio}")

def infoSpecMov():
    print("Toda la informacion sobre esta pelicula es:")
    def nom_ap_p(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None for entry in data):
                  
                    names_and_surnames = [(entry['Nombre'], entry['Apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("data","trainers.json")

    nombres_apellidos = nom_ap_p(json_path)

    for Nombre, Apellido in nombres_apellidos:
            print(f"{Nombre} {Apellido}")