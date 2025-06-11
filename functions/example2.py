import requests


def get_exchange_rate(from_currency, to_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'rates' not in data or to_currency.upper() not in data['rates']:
            return None

        return data['rates'][to_currency.upper()]

    except Exception as e:
        print('Error:', e)
        return None


def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)

    if rate is None:
        return f'Conversion failed: unsupported currency or API error!'
    return f'{amount * rate:.2f}'


amount = 100
from_curr = input()
to_curr = input()
converted = convert_currency(amount, from_curr, to_curr)
print(f'{amount} {from_curr} = {converted} {to_curr}')