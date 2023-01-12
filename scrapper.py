from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page= requests.get(START_URL)

Soup=BeautifulSoup(page.text,"html.parser")
star_table=Soup.find_all("table")
table_rows=star_table[7].find_all('tr')

templist=[]

for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    templist.append(row)

star_name=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(templist)):
    star_name.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])

df2=pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
df2.to_csv("dwraf_stars.csv")