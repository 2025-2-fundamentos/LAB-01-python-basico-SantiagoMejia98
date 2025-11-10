"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/input/data.csv', 'r') as file:
        secuencia = sorted([(letra, int(linea.split("\t")[1])) for linea in file for letra in linea.strip().split("\t")[3].split(",")])
    resultados = []
    for key, group in groupby(secuencia, lambda x: x[0]):
        resultados.append((key, sum(value for _, value in group)))
    return dict(resultados) 
