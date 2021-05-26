import json
import requests
from models.coin import Coin

API_URL = 'https://api.coincap.io/v2/assets/'

def get_token(token):
    response = requests.get(API_URL+token)
    json = response.json()['data']
    return Coin(**json)
 