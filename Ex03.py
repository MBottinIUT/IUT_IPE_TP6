# Importation des librairies
# sudo pip3 install feedparser
import feedparser

# Récupération du flux allocine des sorties de la semaine
url = 'http://rss.allocine.fr/ac/cine/cettesemaine'
flux = feedparser.parse(url)
#print(flux)

# Extraction des informations
entrees_flux = flux.entries

for entree in entrees_flux :
    print (entree.title)
    

