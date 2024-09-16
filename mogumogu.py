import requests
import time

while True:
    requests.get("http://0.0.0.0:3534/open")
    time.sleep(0.5)
    requests.get("http://0.0.0.0:3534/close")
    time.sleep(0.5)
