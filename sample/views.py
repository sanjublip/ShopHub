from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse, request
import requests
from bs4 import BeautifulSoup
import os




# Create your views here.

def login(request):
    return render(request, "userregistration.html")

def index(request):
    return render(request, "index.html")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def search(request):

    name = request.GET['name']
    try:
        global flipkart
        name1 = name.replace(" ","+")   #iphone x  -> iphone+x
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()  ### New Class For Product Name
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()  ### New Class For Product Price

        else:
            flipkart_price = '0'

    except:
        flipkart_price = '0'

    try:
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0, amazon_page_length):
            name = name.upper()
            amazon_nam = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            images = soup.select('.s-image')
            downloads = 0
            for image in images:
                name4 = 'img'
                link = image['src']
                with open(f"C:/Users/lenovo/Desktop/shophub/static/assets/img/img{name4}.jpg".format(name4), "wb") as f:
                    im = requests.get(link)
                    f.write(im.content)
                if downloads == 2:
                    break
            if name in amazon_nam[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_name = amazon_nam.split()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                return render(request, 'destination.html', {'amazon_price': amazon_price, 'amazon_name': flipkart_name, 'amazon_link': amazon, 'name': name,
                                                            'flipkart_price': flipkart_price, 'flipkart_link': flipkart, 'image_link': link})
            else:
                    amazon_price = "product not found in amazon"
    except:
        amazon_price = "product not found in amazon"











