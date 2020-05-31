from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://www.bumeran.com.pe/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#estructuras
empleos =soup.find_all('h2', class_ ='titulo-aviso')
empresas =soup.findAll("a", {"class" :"empresa_nombre_link"})
region =soup.findAll("a",{"class": "ubicacion_link ellipsis"})
fechas = soup.findAll("span", {"class" :"fecha"})
urls =soup.find_all('div', class_='aviso aviso-home clearfix')

listEmpleos= list()
for i in empleos:
    listEmpleos.append(i.text)

listEmpresas = list()
for j in empresas:
    listEmpresas.append((j.text).strip())

listFechas = list()
for k in fechas:
    listFechas.append((k.text))

listRegion =list()
for l in region:
    listRegion.append((l.text).strip())

listUrls =list()
for m in urls:
    listUrls.append('https://www.bumeran.com.pe' + m.get('id'))

#print(listEmpleos)
#dataframe
#df = pd.DataFrame(listEmpresas)
df1= pd.DataFrame({'Empleos':listEmpleos, 'NomEmpresa': listEmpresas,
                   'Region': listRegion,'Fecha': listFechas,
                   'URLs': listUrls })

#print(df1)
#exportar en csv
#encoding='utf-8'
df1.to_csv('ejemplo5.csv',encoding = 'ISO-8859-1' )
