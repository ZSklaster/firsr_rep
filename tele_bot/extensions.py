import requests
import json
from config import keys


class API_exeption(Exception):
    pass


class Skillf_mein:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if base == quote:
            raise API_exeption(f'Невозможно меревести {base} в {quote}')

        try:
            f_tiker = keys[base]
        except KeyError:
            raise API_exeption(f'Неудалось обработать валюту {base}')

        try:
            t_tiker = keys[quote]
        except KeyError:
            raise API_exeption(f'Неудалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise API_exeption(f'Неудалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={f_tiker}&tsyms={t_tiker}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base * amount
