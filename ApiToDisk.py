"""
concept: code python pour récuperer automatiquement des fichiers csv sur data.gouv
         API JSON => python => écriture automatique sur disque


auteur: Eddie Rajaonarivelo, pour CBDATA 7 FITEC

"""
import json
import requests
import csv


id =[]

# boucle sur une colonne "id", dans un fichier .csv externe
with open('list_id.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # ignorer la première ligne (nom des colonnes)
    next(csvfile)
    for ligne in readCSV:
        id.append(ligne[0])

#boucle pour récuperer et stocker une liste d'url, avec comme variale "id"
for i in id:
    response = requests.get("https://www.data.gouv.fr/api/1/datasets/{}/".format(i))
    data = json.loads(response.text)
    
    titre = data['title']
    resources = data['resources']
    csv_url = requests.get(resources[0]['url'])

    # écriture sur disque
    with open('{}.csv'.format(titre), 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(csv_url.text.splitlines())

        for row in reader:
            writer.writerow(row)


