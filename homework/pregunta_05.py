"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        secuencia = sorted([(linea.split('\t')[0], int(linea.split('\t')[1])) for linea in file])
    resultados = []
    for key, group in groupby(secuencia, lambda x: x[0]):
        valores = [value for _, value in group]
        
        resultados.append((key, max(valores), min(valores)))
    return resultados
