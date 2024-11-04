import requests
from bs4 import BeautifulSoup
import csv






with open ("urls_to_scrap",'r',encoding= 'utf-8') as file:
    for url in file.readline():
        url = url.strip()

        pass


def open_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find('strong', class_="projector_prices__price")
    price = products.text.strip()
    print("price: {}".format(price))




    
open_website("XXX")
