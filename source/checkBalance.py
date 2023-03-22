import ccxt
import tkinter as tk


class KrakenBalanceGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kraken Balance Checker")

        # API key entry
        tk.Label(self.root, text="API Key:").grid(row=0, column=0)
        self.api_key_entry = tk.Entry(self.root, width=50)
        self.api_key_entry.grid(row=0, column=1)

        # API secret entry
        tk.Label(self.root, text="API Secret:").grid(row=1, column=0)
        self.api_secret_entry = tk.Entry(self.root, width=50)
        self.api_secret_entry.grid(row=1, column=1)

        # Balance display
        tk.Label(self.root, text="Balance:").grid(row=2, column=0)
        self.balance_var = tk.StringVar()
        self.balance_var.set("")
        tk.Label(self.root, textvariable=self.balance_var).grid(row=2, column=1)

        # Check balance button
        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=3, column=0, columnspan=2)

    def check_balance(self):
        api_key = self.api_key_entry.get()
        api_secret = self.api_secret_entry.get()

        exchange = ccxt.kraken({
            'apiKey': api_key,
            'secret': api_secret,
        })

        balance = exchange.fetch_balance()['total']
        self.balance_var.set(f"{balance['ZUSD']} USD | {balance['XXBT']} BTC | {balance['ETH']} ETH")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = KrakenBalanceGUI()
    gui.run()
