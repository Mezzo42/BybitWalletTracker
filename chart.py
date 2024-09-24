import matplotlib.pyplot as plt

def update_chart(ax, prices, symbol):
    """Aktualisiert den Preis-Chart basierend auf den übergebenen Preisen."""
    ax.clear()
    ax.plot(prices, label=f'{symbol} Preis', color='blue')
    ax.set_title(f'Tick-Chart für {symbol}')
    ax.set_xlabel('Ticks')
    ax.set_ylabel('Preis (USD)')
    ax.legend()
