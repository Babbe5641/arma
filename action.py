import time

import a2s
import requests

tg = '8249005370:AAEpc0Tm9MnbAT1v9aCTlDUkZr9X1Qreeq4'
tg_id = '5633643414'


def query():
    try:
        if a2s.info(("165.217.129.29", 9121)).player_count < 20:
            return True
    except Exception as e:
        print(e)
        return False


def send(text):
    url = f"https://api.telegram.org/bot{tg}/sendMessage"
    msg = {
        "chat_id": tg_id,

    }
    msg["text"] = text
    r = requests.post(url, json=msg)
    # print(r.status_code)
    # print(r.text)
if __name__ == "__main__":
    send("Online")
    if query():
        send("LOW POP")


