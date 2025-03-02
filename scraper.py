import requests
from bs4 import BeautifulSoup

def get_suspected_scammers():
    url = "https://www.signal-arnaques.com/"  # Exemple de site qui liste les arnaques
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return ["Erreur de connexion au site"]

    soup = BeautifulSoup(response.text, "html.parser")
    escrocs = []

    # Supposons que les noms d'escrocs sont dans des balises <h3>
    for scammer in soup.find_all("h3"):
        name = scammer.text.strip()
        escrocs.append(name)

    return escrocs[:10]  # On récupère les 10 premiers noms
