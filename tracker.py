from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json




def read_coins():
    with open("coins.txt", "r") as file:
        lines = file.readlines()
        return lines[0].replace(" ", "").split(',')

def get_crypto_prices():
    coins = read_coins()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
      # 'start':'1',
      # 'limit':'5000',
      # 'id':'9830'
      'symbol':'DEXI'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '2eb82aea-98a7-431d-a186-f793afcb898f',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)

      crypto_data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

    return crypto_data


if __name__ == "__main__":
    print(get_crypto_prices())
