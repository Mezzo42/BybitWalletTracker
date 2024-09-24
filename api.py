from pybit.unified_trading import HTTP

# Deine API-Schlüssel
API_KEY = "XXX"  # Ersetze mit deinem API-Schlüssel
API_SECRET = "XXX"  # Ersetze mit deinem API-Geheimnis

session = HTTP(
    testnet=False,  # Setze auf True, wenn du im Testnetz arbeiten möchtest
    api_key=API_KEY,
    api_secret=API_SECRET,
)

def get_wallet_balance(coin="BTC"):
    output = "Wallet-Balance Informationen:\n"
    try:
        response = session.get_wallet_balance(accountType="UNIFIED", coin=coin)

        if response['retCode'] == 0:
            total_balance = response['result']['list'][0]
            output += f"Gesamt Eigenkapital: {total_balance['totalEquity']}\n"
            output += f"Verfügbares Guthaben: {total_balance['totalAvailableBalance']}\n"
            output += f"Gesamt Wallet-Balance: {total_balance['totalWalletBalance']}\n"
        else:
            output += f"Fehler: {response['retMsg']}\n"
    except Exception as e:
        output += f"Ein Fehler ist aufgetreten: {str(e)}\n"
    
    return output

def get_position_data():
    output = "\nPositionsinformationen:\n"
    positions = []
    try:
        # Abfrage für USDT Perpetual
        response_usdt = session.get_positions(category="linear", settleCoin="USDT")
        # Abfrage für Inverse Perpetual
        response_inverse = session.get_positions(category="inverse")
        
        if response_usdt['retCode'] == 0 and response_inverse['retCode'] == 0:
            positions = response_usdt['result']['list'] + response_inverse['result']['list']
            if positions:
                for position in positions:
                    if float(position['size']) != 0:
                        output += f"Symbol: {position['symbol']}\n"
                        output += f"Seite: {position['side']}\n"
                        output += f"Größe: {position['size']}\n"
                        output += f"Durchschnittspreis: {position['avgPrice']}\n"
                        output += f"Unrealisierter PnL: {position['unrealisedPnl']}\n"
                        output += f"Realisierter PnL: {position['cumRealisedPnl']}\n"
                        output += f"Stop-Loss: {position['stopLoss']}\n"  # Stop-Loss hinzufügen
                        output += f"Take-Profit: {position['takeProfit']}\n"  # Take-Profit hinzufügen
                        output += "-----------------------\n"
            else:
                output += "Keine offenen Positionen gefunden.\n"
        else:
            output += "Fehler beim Abrufen der Positionsdaten.\n"
    except Exception as e:
        output += f"Ein Fehler ist beim Abrufen der Positionsdaten aufgetreten: {str(e)}\n"
    
    return output, positions
