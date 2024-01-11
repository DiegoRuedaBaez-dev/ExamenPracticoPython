from commons.utils import validar_opcion

def gestorBlockbusters():
    print("----------- Sistema Gestor de  Peliculas Blockbuster v0.1-----------")
    print("1. Administrador de Generos")
    print("2. Administrador de Actores")
    print("3. Administrador de Formatos")
    print("4. Gestor de Informes")
    print("5. Gestor de Peliculas")
    print("6. Salir")
    op=validar_opcion("Opcion: ",1,6)
    return op

def gestorGeneros():
    print("----------- Gestor de Generos-----------")
    print("1. Crear genero")
    print("2. Listar generos")
    print("3. Ir al Menu Principal")
    op=validar_opcion("Opcion: ",1,3)
    return op
    
    
def gestorActores():
    print("----------- Gestor de Actores-----------")
    print("1. Crear actor")
    print("2. Buscar actor")
    print("3. Ir al Menu Principal")
    op=validar_opcion("Opcion: ",1,3)
    return op
  
def gestorFormatos():
    print("----------- Gestor de Formatos-----------")
    print("1. Crear formato")
    print("2. Listar formatos")
    print("3. Ir al Menu Principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def gestorPeliculas():
    print("----------- Gestor de Peliculas-----------")
    print("1. Agregar pelicula")
    print("2. Editar pelicula")
    print("3. Eliminar pelicula")
    print("4. Eliminar actor")
    print("5. Buscar pelicula")
    print("6. Listar todas las peliculas")
    print("7. Ir al Menu principal")
    op=validar_opcion("Opcion: ",1,7)
    return op

def gestorInformes():
    print("----------- Gestor de Informes-----------")
    print("1. Listar las peliculas de un genero especifico")
    print("2. Listar las peliculas donde el protagonista sea Silvester Stallone")
    print("3. Buscar pelicula y mostrar la sinopsis y los actores")
    print("4. Ir al Menu Principal")
    op=validar_opcion("Opcion: ",1,4)
    return op