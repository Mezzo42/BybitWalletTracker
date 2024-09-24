# BybitWalletTracker
Bybit Wallet Tracker
Übersicht
Der Bybit Wallet Tracker ist eine Desktop-Anwendung zur Überwachung von Wallet-Bilanzen und offenen Positionen auf der Bybit-Krypto-Börse. Die Anwendung ermöglicht es Benutzern, Echtzeitdaten zu ihrem Portfolio abzurufen und anzuzeigen, einschließlich Wallet-Bilanzen und Positionsinformationen für verschiedene Kryptowährungen.

Funktionen
Echtzeit Wallet-Balance: Zeigt die aktuellen Wallet-Bilanzen für ausgewählte Kryptowährungen an.
Positionsinformationen: Zeigt Informationen über offene Positionen auf Bybit an.
Einfache Benutzeroberfläche: Intuitive GUI zur Auswahl von Coins und zum Abrufen von Daten.
Visualisierung: Diagramm zur Anzeige von Preistrends in Echtzeit.
Voraussetzungen
Python 3.7 oder höher
Die folgenden Python-Pakete:
tkinter (in der Regel vorinstalliert)
matplotlib
pybit (Python-Bibliothek zur Interaktion mit der Bybit API)
Installation
Repository klonen:

cd BybitWalletTracker
Abhängigkeiten installieren:

bash
Code kopieren
pip install matplotlib pybit
API-Schlüssel hinzufügen: Erstelle eine Datei api.py im Projektordner und füge deine Bybit API-Schlüssel wie folgt hinzu:

python
Code kopieren
from pybit.unified_trading import HTTP

# Deine API-Schlüssel
API_KEY = "dein_api_schluessel"
API_SECRET = "dein_api_geheimnis"

session = HTTP(
    testnet=False,  # Setze auf True für Testnet
    api_key=API_KEY,
    api_secret=API_SECRET,
)
Verwendung
Anwendung starten:

bash
Code kopieren
python gui.py
Coin auswählen: Wähle die gewünschte Kryptowährung aus der Dropdown-Liste aus.

Positionsinformationen abrufen: Klicke auf den Button "Positionsinformationen abrufen", um die aktuellen Positionen und Wallet-Bilanzen anzuzeigen.

Beitrag
Beiträge sind willkommen! Bitte erstelle einen Pull-Request oder öffne ein Issue, um Vorschläge oder Fehlerberichte zu teilen.

Lizenz
Dieses Projekt ist lizenziert und darf nur zum Privatgebrauch genutzt werden.

Kontakt
Für Fragen oder Anfragen kannst du mich über GitHub kontaktieren.

