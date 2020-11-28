"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
import operator

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

recursionLimit = 20000
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información")
    print("3- Estaciones críticas ")
    print('4- Ejecutar requerimiento 4')
    print("5- Ejecutar requerimiento 5 ")

def optionTwo():
    print("\nCargando información ....")
    controller.loadTrips(cont,topd,tops,tot)
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))
    

def optionFour():
    print('Las estaciones de salida más populares son:')
    tops_ord=sorted(tops.items(),key=operator.itemgetter(1), reverse=True)
    topd_ord=sorted(topd.items(),key=operator.itemgetter(1), reverse=True)
    tot_ord=sorted(tot.items(),key=operator.itemgetter(1))
    print('1.'+tops_ord[0][0])
    print('2.'+tops_ord[1][0])
    print('3.'+tops_ord[2][0])
    print('Las estaciones de llegada más populares son:')
    print('1.'+topd_ord[0][0])
    print('2.'+topd_ord[1][0])
    print('3.'+topd_ord[2][0])
    print('Las estaciones menos usadas son:')
    print('1.'+tot_ord[0][0])
    print('2.'+tot_ord[1][0])
    print('3.'+tot_ord[2][0])

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
        topd={}
        tops={}
        tot={}

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0])==4:
        id=input("Ingrese el ID de la estación de inicio: ")
        tiempo=input("Ingrese el tiempo máximo de resistencia: ")
        respuesta=controller.req4(id,tiempo,cont, '201801-1-citibike-tripdata.csv')
        for i in respuesta:
            if i== []:
                print("No hay rutas en tan poco tiempo")
            else:
                print(i)
    elif int(inputs[0]) == 3:
        
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
        
    elif int(inputs[0])==5:
        rango1= int(input("Ingrese el rango inicial: "))
        rango2= int(input("Ingrese el rango inicial: "))
        rta= controller.req5(rango1,rango2, cont, '201801-1-citibike-tripdata.csv')
        print("Nombre de la estación inicial: ",rta['estacioninicial'])
        print("Nombre de la estación final: ",rta['estacionfinal'])
        print("Estaciones: ",rta['estaciones'])
   
    else:
        sys.exit(0)
sys.exit(0)
