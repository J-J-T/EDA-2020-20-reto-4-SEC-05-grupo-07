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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo
def newAnalyzer():
    try:
        citibike={
            "graph":None

        }
        citibike["graph"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=compareStations)
    
        return citibike
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')

def addTrip(citibike, trip,topd,tops,tot):

    origin = trip['start station id']
    o=trip['start station name']
    destination = trip['end station id']
    d=trip['end station name']
    duration = int(trip['tripduration'])
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)
    if d not in topd:
        topd[d]=1
        tot[d]=1
    else: 
        topd[d]=(topd[d]+1)
        tot[d]=(tot[d]+1)
    if o not in tops:
        tops[o]=1
        tot[o]=1
    else:
        tops[o]=(tops[o]+1)
        tot[o]=(tot[o]+1)
    
    

def addStation(citibike, stationid):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(citibike ["graph"], stationid):
            gr.insertVertex(citibike ["graph"], stationid)
    return citibike

def addConnection(citibike, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(citibike["graph"], origin, destination)
    if edge is None:
        gr.addEdge(citibike["graph"], origin, destination, duration)
    return citibike



# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def compareStations(stop, keyvaluestop):
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1

def totalConnections(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer['graph'])

def totalStops(citibike):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return gr.numVertices(citibike["graph"])

def req4(id,tiempo,citibike):
    total=0
    respuesta=[]
    for i in citibike:
         if total+int(i['tripduration'])<tiempo:
            total=total+int(i['tripduration'])
            respuesta.append({'Nombre de estación inicio': i['start station name'], 'Nombre estación final':i['end station name'], 'Duración estimada del segmento':i['tripduration']})
    return respuesta


def req5(rango1,rango2, citibike):
    dato1=str(2018-rango1)
    dato2=str(2018-rango2)
    tiempo=2000
    estaciones=[]
    dict={'estacioninicial': '','estacionfinal': '','estaciones':[] }
    for citibi in citibike:
        if citibi['birth year']<dato1 and citibi['birth year']>dato2:
            if citibi['start station name'] not in estaciones :
                estaciones.append(citibi['end station name'])
            if int(citibi['tripduration'])<tiempo:
                tiempo= int(citibi['tripduration'])
                dict['estacionfinal']= citibi['end station name']
                dict['estacioninicial']= citibi['start station name']
    dict['estaciones']=list(set(estaciones))

    return dict
