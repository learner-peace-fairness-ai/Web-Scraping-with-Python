import requests
import socks
import socket

URL = "https://icanhazip.com/"

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

res = requests.get(URL)
print(res.text)
