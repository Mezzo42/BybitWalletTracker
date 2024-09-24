import tkinter as tk
from tkinter import scrolledtext, ttk
from api import get_wallet_balance, get_position_data, session
from chart import update_chart
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BybitWalletTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Bybit Wallet Tracker")
        self.master.configure(bg='black')

        self.frame = tk.Frame(self.master, bg='black')
        self.frame.pack(pady=10)

        # Liste von Coins für die Auswahl
        coins = ['BTC', 'ETH', 'XRP', 'SOL', 'LTC']  # Beispiel-Liste von Coins
        self.coin_selection = ttk.Combobox(self.frame, values=coins)
        self.coin_selection.set('BTC')  # Standardwert
        self.coin_selection.pack(side=tk.LEFT, padx=5)

        self.btn_balance = tk.Button(self.frame, text="Positionsinformationen abrufen", command=self.update_position_data, bg='black', fg='white')
        self.btn_balance.pack(side=tk.LEFT, padx=5)

        # ScrolledText für Wallet-Balance
        self.wallet_output_area = scrolledtext.ScrolledText(self.master, width=40, height=10, bg='black', fg='white', insertbackground='white')
        self.wallet_output_area.pack(side=tk.LEFT, padx=20, pady=20)

        # ScrolledText für Positionsinformationen
        self.position_output_area = scrolledtext.ScrolledText(self.master, width=40, height=10, bg='black', fg='white', insertbackground='white')
        self.position_output_area.pack(side=tk.LEFT, padx=20, pady=20)

        # Frame für den Chart
        self.chart_frame = tk.Frame(self.master, bg='black')
        self.chart_frame.pack(pady=10)

        # Matplotlib Figure und Canvas für den Chart
        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.chart_frame)
        self.canvas.get_tk_widget().pack()

        self.prices = []  # Liste für Preisdaten

        # Nächste Aktualisierung in 1000ms (1 Sekunde)
        self.update_data()

    def update_position_data(self):
        """Wird beim Klick auf den Button aufgerufen, um Positionsinformationen zu aktualisieren."""
        selected_coin = self.coin_selection.get()
        if selected_coin:
            positions, _ = get_position_data()  # Hier müssen die Positionsdaten abgerufen werden
            self.position_output_area.delete(1.0, tk.END)
            if positions:
                self.position_output_area.insert(tk.END, str(positions))
            else:
                self.position_output_area.insert(tk.END, "Keine Positionsdaten verfügbar.")
        else:
            print("Kein Coin ausgewählt")

    def update_data(self):
        """Regelmäßig Wallet-Balance und Chart-Daten aktualisieren."""
        selected_coin = self.coin_selection.get()
        if selected_coin:
            balance_info = get_wallet_balance(selected_coin)
            self.wallet_output_area.delete(1.0, tk.END)
            self.wallet_output_area.insert(tk.END, str(balance_info))
            update_chart(self.ax, self.prices, selected_coin)
            self.canvas.draw()

        self.master.after(1000, self.update_data)

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = BybitWalletTracker(root)
    root.mainloop()
