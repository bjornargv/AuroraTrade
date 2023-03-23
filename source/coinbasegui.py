import ccxt
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        master.title("AuroraTrade")
        master.configure(bg="white")
        master.geometry("700x700")

        # Initialize Coinbase API
        self.exchange = ccxt.coinbasepro()

        # Get ticker information for BTC/USD
        self.ticker = self.exchange.fetch_ticker('BTC/USD')

        # Center the app on the screen
        window_width = master.winfo_reqwidth()
        window_height = master.winfo_reqheight()
        position_right = int(master.winfo_screenwidth() / 2 - window_width / 2) - 250
        position_down = int(master.winfo_screenheight() / 2 - window_height / 2) - 300
        master.geometry("+{}+{}".format(position_right, position_down))

        # Create Header Frame
        self.header_frame = tk.Frame(master, bg="white")
        self.header_frame.pack(fill=tk.X, padx=10, pady=10)

        # Load logo image
        self.logo = tk.PhotoImage(file="assets/aurora.png").subsample(2)

        # Create Labels
        self.logo_label = tk.Label(master, image=self.logo, bg="white")
        self.btc_usd_price_label = tk.Label(master, text="BTC/USD Price: $0.00", bg="white", fg="black",
                                            font=("Arial", 16))
        self.btc_nok_price_label = tk.Label(master, text="BTC/NOK Price: 0.00 NOK", bg="white", fg="black",
                                            font=("Arial", 16))
        self.btc_amount_label = tk.Label(master, text="Bitcoin Amount:", bg="white", fg="black", font=("Arial", 16))
        self.btc_value_nok_label = tk.Label(master, text="Your assets: 0.00 NOK", bg="white", fg="black",
                                            font=("Arial", 16))

        # Create Entry
        self.btc_amount_entry = tk.Entry(master, bg="white", fg="black", font=("Arial", 16))

        # Add widgets to the window
        self.logo_label.pack(padx=10, pady=10)
        self.btc_usd_price_label.pack(padx=10, pady=10)
        self.btc_nok_price_label.pack(padx=10, pady=10)
        self.btc_amount_label.pack(padx=10, pady=10)
        self.btc_amount_entry.pack(padx=10, pady=10)
        self.load_amount()
        self.btc_value_nok_label.pack(padx=10, pady=10)

        # Initialize Coinbase API
        self.exchange = ccxt.coinbasepro()

        # Get ticker information for BTC/USD
        self.ticker = self.exchange.fetch_ticker('BTC/USD')

        # Call update_values to display initial values
        self.update_values()

        # Bind the <Return> key to the btc_amount_entry widget
        self.btc_amount_entry.bind('<Return>', self.update_values)
        self.btc_amount_entry.bind('<KeyRelease>', self.update_values)
        # Update the prices
        self.update_price()

        # Call update_price every second
        self.master.after(1000, self.update_price)

    def update_price(self):
        # Get ticker information for BTC/USD
        self.ticker = self.exchange.fetch_ticker('BTC/USD')

        # Update the USD and NOK price labels
        usd_price = self.ticker['last']
        nok_price = usd_price * 10.38
        self.btc_usd_price_label.config(text=f"BTC/USD Price: ${usd_price:.2f}")
        self.btc_nok_price_label.config(text=f"BTC/NOK Price: {nok_price:.2f} NOK")

        # Call update_price again in one second
        self.master.after(1000, self.update_price)

    def update_values(self, event=None):
        # Get the bitcoin amount from the user
        try:
            bitcoin_amount = float(self.btc_amount_entry.get())
        except ValueError:
            bitcoin_amount = 0

        # Calculate the value in NOK
        usd_price = self.ticker['last']
        nok_rate = 10.38
        usd_value = bitcoin_amount * usd_price
        nok_value = usd_value * nok_rate

        # Display the value in the GUI
        self.btc_value_nok_label.config(text=f"Your assets: {nok_value:.2f} NOK")

        # Call update_value function again after 1 second
        self.master.after(1000, self.update_values)

    def load_amount(self):
        try:
            with open("amount.txt", "r") as file:
                amount = file.read()
                self.btc_amount_entry.delete(0, tk.END)
                self.btc_amount_entry.insert(0, amount)
        except FileNotFoundError:
            pass

    def save_amount(self):
        with open("amount.txt", "w") as file:
            file.write(self.btc_amount_entry.get())
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.save_amount)
    root.mainloop()
