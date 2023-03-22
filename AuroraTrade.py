import os
import ccxt
import time
import numpy as np
import talib


def initialize_kraken(api_key, api_secret):
    exchange = ccxt.kraken({
        'apiKey': api_key,
        'secret': api_secret,
    })
    return exchange


def get_ohlcv(exchange, symbol, timeframe):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    return ohlcv


def moving_average_crossover(api_key, api_secret, symbol, short_window, long_window, trade_amount_nok):
    exchange = initialize_kraken(api_key, api_secret)

    position = None

    while True:
        ohlcv = get_ohlcv(exchange, symbol, '5m')
        closes = np.array([x[4] for x in ohlcv])

        short_ma = talib.SMA(closes, short_window)
        long_ma = talib.SMA(closes, long_window)

        btc_nok_ticker = exchange.fetch_ticker('BTC/NOK')
        btc_nok_price = btc_nok_ticker['last']
        trade_amount_btc = trade_amount_nok / btc_nok_price

        if short_ma[-1] is not None and long_ma[-1] is not None:
            if short_ma[-1] > long_ma[-1] and position != 'long':
                exchange.create_market_buy_order(symbol, trade_amount_btc)
                position = 'long'
                print('Bought at:', closes[-1])

            elif short_ma[-1] < long_ma[-1] and position != 'short':
                exchange.create_market_sell_order(symbol, trade_amount_btc)
                position = 'short'
                print('Sold at:', closes[-1])

        time.sleep(60 * 5)  # Check every 5 minutes


if __name__ == "__main__":
    API_KEY = os.environ.get('KRAKEN_API_KEY') or 'your_api_key_here'
    API_SECRET = os.environ.get('KRAKEN_API_SECRET') or 'your_api_secret_here'
    SYMBOL = 'BTC/NOK'  # Trading pair you want to trade
    SHORT_WINDOW = 12
    LONG_WINDOW = 26
    TRADE_AMOUNT_NOK = 100  # Replace with the amount you want to trade in NOK

    moving_average_crossover(API_KEY, API_SECRET, SYMBOL, SHORT_WINDOW, LONG_WINDOW, TRADE_AMOUNT_NOK)
