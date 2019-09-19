# Importation des librairies
import requests
import csv

# Récupération du fichier officiel des codes postaux s'il n'existe pas
try :
    with open('codes_postaux.csv') :
        pass
except IOError :
    url = 'https://datanova.legroupe.laposte.fr/explore/dataset/laposte_hexasmal/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true'
    mon_fichier = requests.get(url)
    with open('codes_postaux.csv', 'wb') as donnees :
        donnees.write(mon_fichier.content)
        
# Demande à l'utilisateur le nom de la commune
commune = ???????
# Mise en majuscules
commune = commune.upper()
# Affichage du nom de la commune dans la console
print(commune)

# Extraction du code postal dans le fichier CSV
fichier_csv = open("codes_postaux.csv", "r")
try :
    lecteur_csv = csv.reader(fichier_csv, delimiter=";")
    for ligne in lecteur_csv :
        ?????????????
		# Affichage du code postal dans la console
		?????????????
finally :
    fichier_csv.close()

    