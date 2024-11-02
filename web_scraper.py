import requests
from bs4 import BeautifulSoup
import csv






with open ("urls_to_scrap",'r',encoding= 'utf-8') as file:
    for url in file.readline():
        url = url.strip()
        pass
