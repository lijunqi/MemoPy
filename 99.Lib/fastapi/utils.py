import requests

URL = "http://127.0.0.1:8000"

def send_get(url):
    with requests.session() as sess:
        res = sess.get(url)
        if res.status_code == 200:
            print(f"[Success-GET]{url}",'\n', res.json(), '\n')
        else:
            print(f"[{res.status_code}-GET]{url}",'\n', res.json(), '\n')


def send_post(url, payload):
    with requests.session() as sess:
        res = sess.post(url, json=payload) # Request Body
        if res.status_code == 200:
            print(f"[Success-POST]{url}",'\n', res.json(), '\n')
        else:
            print(f"[{res.status_code}-POST]{url}",'\n', res.json(), '\n')
