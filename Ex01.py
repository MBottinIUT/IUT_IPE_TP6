from bs4 import BeautifulSoup
import requests

URL_site = 'https://www.lapenseedujour.net'

# Récupération de la page
contenu_brut = requests.get(URL_site)
# Trie le contenu html pour le stocker
code_html = BeautifulSoup(contenu_brut.text, 'html.parser')
#print(code_html)

information_recherchee = code_html.find('table', attrs={"class":u"cadre"}).find('font')

# extraction du texte
pensee = information_recherchee.text

print(pensee)


