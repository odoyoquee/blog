import urllib.request,json
from . import create_app
import requests


def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json (Links to an external site.)')
    if response.status_code == 200:
        quote = response.json()
        return quote
