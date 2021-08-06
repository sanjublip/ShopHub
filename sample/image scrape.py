import requests
from bs4 import BeautifulSoup
import os.path

url = 'https://www.amazon.in/poco-x2/s?k=poco+x2'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

images = soup.select('.s-image')

for image in images:
    name = 'img'
    link = image['src']
    print(link)
    with open(f"C:/Users/MY/projects/shophub/assets/assets/img/{name}.jpg".format(name), "wb") as f:
        im = requests.get(link)
        f.write(im.content)