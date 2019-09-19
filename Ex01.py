from bs4 import BeautifulSoup
import requests

URL_site = 'https://citations.ouest-france.fr'

# Récupération de la page
contenu_brut = requests.get(URL_site)
# Trie le contenu html pour le stocker
code_html = BeautifulSoup(contenu.text, 'html.parser')
#print(code_html)

# recherche de la balise html qui nous intéresse
information_recherchee = code_html.find('div',attrs={"class":u"citation"}).find('p')

# extraction du texte
citation = information_recherchee.text

print(citation)


