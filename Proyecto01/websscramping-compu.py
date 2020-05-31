from bs4 import BeautifulSoup
import requests
import pandas as pd

url ='https://www.computrabajo.com.pe/empleos-en-lima'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

empleos =soup.find_all("a", {"class": "js-o-link"})
fechas =soup.find_all('span',  class_="dO")

listEmpleos= list()
for i in empleos:
    listEmpleos.append(i.get('title'))
#corregir fechas
listFechas =list()
for j in fechas:
    listFechas.append((j.text).strip())

#print(listFechas)

df = pd.DataFrame({"Empleo": listEmpleos, "Fecha": listFechas})
print(df)

#df.to_csv('Clasificacion.csv', encoding = 'ISO-8859-1')