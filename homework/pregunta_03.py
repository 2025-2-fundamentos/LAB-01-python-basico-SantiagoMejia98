"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv', 'r') as file:
        secuencia = sorted([(linea.split('\t')[0], int(linea.split('\t')[1])) for linea in file])
    resultados = []
    for key, group in groupby(secuencia, lambda x: x[0]):
        resultados.append((key, sum(value for _, value in group)))
    return resultados
