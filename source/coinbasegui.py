import tkinter as tk
from tkinter import ttk
import ccxt
from ttkthemes import ThemedStyle


class CoinbasePriceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Coinbase Price")
        master.geometry("500x250")
        master.configure(bg="#222222")

        # Set style
        self.style = ThemedStyle(master)
        self.style.set_theme("black")

        # Create a label for displaying the price
        self.price_label = ttk.Label(master, text="", font=("Helvetica", 30), foreground="#ffffff",
                                     background="#222222")
        self.price_label.pack(padx=30, pady=30)

        # Create a label and entry for the bitcoin amount
        self.bitcoin_label = ttk.Label(master, text="Bitcoin Amount:", foreground="#ffffff", background="#222222")
        self.bitcoin_label.pack(padx=10, pady=10)
        self.bitcoin_entry = ttk.Entry(master)
        self.bitcoin_entry.pack(padx=10, pady=10)

        # Create a button to calculate the NOK value
        self.calculate_button = ttk.Button(master, text="Calculate NOK Value", command=self.calculate_nok_value)
        self.calculate_button.pack(padx=10, pady=10)

        # Initialize Coinbase API
        self.exchange = ccxt.coinbasepro()

        # Refresh the price on startup
        self.refresh_price()

    def refresh_price(self):
        # Get ticker information for BTC/USD
        ticker = self.exchange.fetch_ticker('BTC/USD')

        # Calculate the price in USD and NOK
        usd_price = ticker['last']
        nok_price = usd_price * 10.38

        # Display the prices in the label
        self.price_label.config(text=f"BTC/USD Price: ${usd_price:.2f}\nBTC/NOK Price: {nok_price:.2f} NOK")

    def calculate_nok_value(self):
        # Get the bitcoin amount from the entry widget
        bitcoin_amount = float(self.bitcoin_entry.get())

        # Get ticker information for BTC/USD
        ticker = self.exchange.fetch_ticker('BTC/USD')

        # Calculate the value in USD and NOK
        usd_price = ticker['last']
        nok_rate = 10.38
        usd_value = bitcoin_amount * usd_price
        nok_value = usd_value * nok_rate

        # Display the value in the label
        self.price_label.config(text=f"BTC/USD Value: ${usd_value:.2f}\nBTC/NOK Value: {nok_value:.2f} NOK")


if __name__ == "__main__":
    root = tk.Tk()
    CoinbasePriceGUI(root)
    root.mainloop()
