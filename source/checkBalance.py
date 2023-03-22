import os
import ccxt

def get_kraken_balance(api_key, api_secret):
    exchange = ccxt.kraken({
        'apiKey': api_key,
        'secret': api_secret,
    })

    balance = exchange.fetch_balance()

    # Print the balance for all currencies
    for currency, amount in balance['total'].items():
        print(f'{currency}: {amount}')

if __name__ == "__main__":
    API_KEY = os.environ.get('KRAKEN_API_KEY') or 'your_api_key_here'
    API_SECRET = os.environ.get('KRAKEN_API_SECRET') or 'your_api_secret_here'

    get_kraken_balance(API_KEY, API_SECRET)
