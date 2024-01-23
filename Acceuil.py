import requests
from bs4 import BeautifulSoup

url = 'https://lenouvelliste.com/'
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")
    all_tag = soup.findAll('div')

    for tag in all_tag:
        # Récupérer le titre
        title_tag = tag.find('h1')
        if title_tag:
            title = title_tag.text.strip()
     # print(f"Titre: {title}")
     link = tag.find('a')['href']

        # Récupérer l'URL de la photo (supposons que l'image soit dans une balise <img>)
        image_url = tag.find('img')['src']

        # Récupérer la description (supposons que la description soit dans une balise <p>)
        description = tag.find('p').text.strip()

        # Afficher les informations de l'article
        print(f"Titre: {title}")
        print(f"Liens: {link}")
        print(f"Image URL: {image_url}")
        print(f"Description: {description}")
        print("\n")
else:
    print(f"Échec de la requête HTTP avec le code d'état {reponse.status_code}")

