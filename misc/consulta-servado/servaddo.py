#!/usr/bin/env python3
# coding: utf-8

import requests
import json
import csv

# Modificar este número para incrementar la cantidad de entradas a descargar
maxRows = str(2000)

print("Busque y descargue sus datos del listado oficial")
print("Codigos de los distados disponibles: 108b, fl2")
codListado = input("Ingrese el codigo del listado y presione enter: ")

SERVER_URL = 'http://server35.abc.gov.ar/lof.mc/'+ codListado +'/'
jQueryId = 'jQuery172015617992574835882_1520259126988'

paramList = list()
param = input('Ingrese un parámetro de búsqueda y presione enter: ')
while (param):
    paramList.append('&fq=busqueda%3A' + param)
    param = input('Ingrese otro parámetro de búsqueda, o presione enter para realizar la búsqueda: ')

print(paramList)

if (len(paramList) == 0):
    print("No ingresó ningún parámetro, saliendo")
    exit(-1)

paramBusqueda = ''.join(paramList)
start = str(0)

params = 'select?q=*%3A*%20AND%20aniolistado%3A%5B2016%20TO%202018%5D&fl=apto_fisico%2Capellido%2Cpun_titu%2Cpun_reside%2Cnombre%2Cdocumento%2Cdistrito%2Crama%2Ccargo_area%2Cpro_tit%2Cpuntaje%2Corden%2Ccargo_area_id%2Ctimestamp%2Caniolistado%2Crecalificacionlaboral&start=' + start + '&rows=' + maxRows + '&sort=orden%20asc' + paramBusqueda + '&facet=true&facet.field=distrito&facet.field=rama&facet.field=cargo_area&facet.field=aniolistado&facet.mincount=1&json.nl=map&wt=json&json.wrf=' + jQueryId + '&_=1520259139516'
referer = 'http://servicios.abc.gov.ar/servaddo/listado.oficial/?s=' + codListado
headers = {
    'Host': 'server35.abc.gov.ar',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': referer,
    'Cookie': '_ga=GA1.3.1049753468.1510787586; _gid=GA1.3.1881545445.1520221751; _gat=1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


url = SERVER_URL + params
response = requests.get(url, headers=headers)

offset = len(jQueryId) + 1
dataRaw = response.content[offset : -1]
data = json.loads(dataRaw.decode('utf-8'))

materias = data['facet_counts']['facet_fields']

if (len(data['response']['docs']) == 0):
    print ("No se encontraron registros para el criterio buscado")
    exit(0)

headersCsv = data['response']['docs'][0]

if (data['response']['numFound'] > int(maxRows)):
    print ("ATENCION: el número de registros encontrados es mayor al descargado, ajuste la variable 'maxRows' de este script")

filename = input('Nombre el archivo de salida: ', "salida")
with open(filename + '.csv','w') as f:
    w = csv.DictWriter(f,headersCsv.keys())
    w.writeheader()
    w.writerows(data['response']['docs'])

print("Se generó el archivo " + filename + ".csv, que puede ser utilizado en procesadores de hojas cálculo")