from commons.utils import *
from commons.menus import *
from businnes.actoresPeliculas import *
from businnes.informes import *
from businnes.generosPeliculas import *
from businnes.formatosPeliculas import *
from businnes.mainPeliculas import *

def actoresPeliculas():      
    limpiar_pantalla()
    op=gestorActores()
    if op==1:
      limpiar_pantalla()
      crearActor()
      input("Clic cualquier teclas [continuar]: ")
    if op==2:
      limpiar_pantalla()
      listarActores()
      input("Clic cualquier teclas [continuar]: ")
       
def formatosPeliculas():
    limpiar_pantalla()
    op=gestorFormatos()
    if op == 1:
        limpiar_pantalla()
        crearFormato()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        limpiar_pantalla()
        listaFormatos()
        input("Clic cualquier teclas [continuar]: ")
        
def mainPeliculas():
    limpiar_pantalla()
    op=gestorPeliculas()
    if op == 1:
        limpiar_pantalla()
        crearPelicula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        limpiar_pantalla()
        modificarPeliculas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        limpiar_pantalla()
        # eliminarPeliculas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 4:
        limpiar_pantalla()
        # eliminarActor()
        input("Clic cualquier teclas [continuar]: ")
    if op == 5:
        limpiar_pantalla()
        buscarPelicula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 6:
        limpiar_pantalla()
        listarPeliculas()
        input("Clic cualquier teclas [continuar]: ") 
      
        
def generosPeliculas():
    limpiar_pantalla()
    op=gestorGeneros()
    if op == 1:
        limpiar_pantalla()
        crearGeneros()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        limpiar_pantalla()
        listarGeneros()
        input("Clic cualquier teclas [continuar]: ")
        
def informesPeliculas():
    limpiar_pantalla()
    op=gestorInformes()
    if op ==1:
        limpiar_pantalla()
        infoSpecGen()#No Funciona
        input("Clic cualquier teclas [continuar]: ")
    elif op==2:
        limpiar_pantalla()
        infoSpecName()#No Funciona
        input("Clic cualquier teclas [continuar]: ")
    elif op==3:
        limpiar_pantalla()
        infoSpecMov()#No Funciona
        input("Clic cualquier teclas [continuar]: ")

#start
while True: 
   limpiar_pantalla()
   op=gestorBlockbusters()
   if  op==1:
       gestorGeneros()
   elif op==2:
       gestorActores()
   elif op==3:
       gestorFormatos()
   elif op==4:
      gestorInformes()
   elif op==5:
       gestorPeliculas()
   elif op==6:
       print("Saliendo")
       break     