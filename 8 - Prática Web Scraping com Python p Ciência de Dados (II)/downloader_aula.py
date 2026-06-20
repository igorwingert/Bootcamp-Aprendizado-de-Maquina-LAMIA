import requests
from bs4 import BeautifulSoup as bs

# carrega a pagina principal
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")

# transforma o conteudo em beautifulsoup
webpage = bs(r.content)

# seleciona as imagens da pagina
images = webpage.select("div.row div.column img")
image_url = images[0]['src']
full_url = url + image_url

# baixa a imagem e salva em um arquivo local
img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)
