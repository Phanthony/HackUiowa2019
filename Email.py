from bs4 import BeautifulSoup
import requests


def email():
    result = requests.get("https://10minemail.com/en/change")
    print(result)

