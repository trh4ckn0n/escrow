import requests
from bs4 import BeautifulSoup

def get_suspected_scammers():
    url = "https://info.signal-arnaques.com/tous-les-articles"  # Nouvelle URL
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return ["Erreur de connexion au site"]

    soup = BeautifulSoup(response.text, "html.parser")
    escrocs = []

    # On suppose que les noms d'escrocs sont dans des balises <h2> ou similaires
    for article in soup.find_all("h2"):  # Adapté à la structure de la page
        name = article.text.strip()
        escrocs.append(name)

    return escrocs[:10]  # On récupère les 10 premiers titres d'articles

# Test de la fonction
print(get_suspected_scammers())
