import socket #biblioteca que dá acesso ao ip interno da máquina
from requests import get #biblioteca que permite acessar a API ipify para conseguir o ip externo

class BuscaIP:
    def __init__(self):
        self.ipInterno = None
        self.ipExterno = None
        self.hostname = None

    def buscaIpInterno(self) -> None:
        self.hostname = socket.gethostname()
        self.ipInterno = socket.gethostbyname(self.hostname)
        print(f"Hostname: {self.hostname}")
        print(f"IP Interno: {self.ipInterno}")

    def buscaIpExterno(self) -> None:
        self.ipExterno = get('https://api.ipify.org').text
        print(f"IP Externo: {self.ipExterno}")
