"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as file:
        secuencia = sorted([(codigo.split(":")[0], 1) for linea in file for codigo in linea.split('\t')[4].split(',')])
    resultados = []
    for key, group in groupby(secuencia, lambda x: x[0]):
        resultados.append((key, sum(value for _, value in group)))
    return dict(resultados)
