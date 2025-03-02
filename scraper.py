import requests
from bs4 import BeautifulSoup

def get_suspected_scammers():
    url = "https://info.signal-arnaques.com/tous-les-articles"  # Nouvelle URL
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Si le status code n'est pas 200, une exception sera levée

        soup = BeautifulSoup(response.text, "html.parser")
        escrocs = []

        # On suppose que les titres des escrocs sont dans des balises <h2> ou similaires
        for article in soup.find_all("h2"):  # Adapté à la structure de la page
            name = article.text.strip()
            escrocs.append(name)

        return escrocs[:10]  # On récupère les 10 premiers titres d'articles

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion ou problème avec la requête: {e}")
        return ["Erreur de connexion au site"]
    except Exception as e:
        print(f"Une erreur est survenue: {e}")
        return ["Erreur inconnue"]

# Test de la fonction
print(get_suspected_scammers())
