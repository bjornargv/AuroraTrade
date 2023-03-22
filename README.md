# AuroraTrade
AuroraTrade is an elegant day trading bot designed to navigate the captivating world of cryptocurrency. Focusing on the BTC/NOK trading pair on Kraken, the bot employs a simple yet effective Moving Average Crossover strategy. AuroraTrade aims to provide users with a delightful trading experience that resonates with the mesmerizing beauty of the Nordic skies.

### Technical stuff

This Kraken day trading bot is designed to trade the BTC/NOK (Bitcoin to Norwegian Krone) pair using a simple Moving Average Crossover strategy. The bot is implemented in Python and uses ccxt, numpy, and ta-lib libraries.

In practice, the bot works by monitoring the BTC/NOK trading pair on the Kraken exchange and executing buy and sell orders based on the Moving Average Crossover strategy. It compares a short-term moving average (by default, 12 periods) with a long-term moving average (by default, 26 periods) to determine the optimal points to enter or exit a trade.

The frequency of buy and sell orders depends on the market conditions and the chosen moving average windows. If the market is volatile and the moving averages frequently cross each other, the bot will execute more buy and sell orders. In a less volatile market, the bot might execute fewer orders.

<em>Please note that trading cryptocurrencies carries risks, and using a simple trading bot like this one may not guarantee profits. This example is for educational purposes and should be used as a starting point to build more sophisticated trading strategies.</em>

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Strategy](#strategy)
- [Customization](#customization)
- [License](#license)

## Prerequisites

Before using the bot, you need to have the following:

- Python 3.6 or higher installed, 3.10 at the highest due to support of technical analysis library wheels not being updated for 3.11
- Kraken account with API key and secret
- `ccxt`, `numpy`, and `ta-lib` libraries installed

## Installation

1. Clone the repository or download the Python script:


```
git clone https://github.com/yourusername/kraken-btc-nok-bot.git](https://github.com/bjornargv/AuroraTrade
cd AuroraTrade
```


2. Install the required Python libraries:


```
pip install ccxt numpy TA-Lib
```


### Usage

Open the Python script with your preferred text editor and replace 'your_api_key_here' and 'your_api_secret_here' with your actual Kraken API key and secret.

Set the TRADE_AMOUNT_NOK variable to the amount you want to trade in NOK.

Run the script:

```
python AuroraTrade.py
```


The bot will start trading and print the buy/sell actions to the console.


### Strategy

The trading bot uses the Moving Average Crossover strategy with two simple moving averages: a short-term moving average and a long-term moving average. The bot checks the moving averages every 5 minutes and takes the following actions:

- If the short-term moving average crosses above the long-term moving average and the current position is not long, the bot places a market buy order.


- If the short-term moving average crosses below the long-term moving average and the current position is not short, the bot places a market sell order.

### Customization

You can customize the bot by modifying the following parameters in the script:

- <strong>SHORT_WINDOW<strong>: The number of periods for the short-term moving average (default: 12)

- <strong>LONG_WINDOW<strong>: The number of periods for the long-term moving average (default: 26)

- <strong>TRADE_AMOUNT_NOK<strong>: The amount you want to trade in NOK (default: 100)

You can also modify the moving_average_crossover function to implement more sophisticated trading strategies or use other technical indicators from the ta-lib library.

### License
  
This project is licensed under the MIT License. Use it however you want, forks are received with open arms.
