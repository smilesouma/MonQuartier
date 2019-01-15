import requests
import re
from bs4 import BeautifulSoup


#url de la page
url = "http://www.vin-vigne.com/millesimes/annee-2010-vin-bourgogne.html"

# se connecter à la page et obtenir le code source
requete = requests.get(url)
page_html = requete.content

# transformer la page HTML en beautifulSoup pour pouvoir la manipuler
soupe = BeautifulSoup(page_html, "html5lib")

#stocker les donnees obtenus
data = []
table = soupe.find('table', attrs={'class':'points'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

#affiche le résultat
print(data)




