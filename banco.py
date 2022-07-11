import pandas as pd
import numpy as np
import unicodedata
import json


def getEntidadDataRaw():

    table_MN = pd.read_html('https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx', attrs = {'title': 'Resultado de la consulta'}, thousands='.',decimal=',')

    df = table_MN[0]

    df = df.replace('Ãº', 'u', regex=True)
    df = df.replace('Ã©', 'e', regex=True)
    df = df.replace('Â°', '#', regex=True)
    df = df.replace('Ã³', 'o', regex=True)
    df = df.replace('Ã', 'u', regex=True)
    df = df.replace('Â', '', regex=True)

    df.drop(0, inplace=True, axis=1)
    df.drop(37, inplace=True, axis=0)
    df.drop(0, inplace=True, axis=0)

    dflist = df.values.tolist()

    dflist = [[unicodedata.normalize("NFKD", word) for word in ls] for ls in dflist]

    return dflist

def getEntidadInfo(bancoNombre):

    rawLista = getEntidadDataRaw()
    bancoList = []

    for row in rawLista:
        if row[0] == bancoNombre:
            bancoList = row
            break

    return bancoList

#Lista de Bancos

def getEntidadLista():

    rawLista = getEntidadDataRaw()
    bancoList = []

    for row in rawLista:
        bancoList.append(row[0])

    return bancoList
