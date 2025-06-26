from utils import URL, send_get, send_post

if __name__ == "__main__":
    payload = {
        "name": "Tom",
        #"description": "This is Tom",
        "price": 1.0,
    }
    send_post(f"{URL}/my_item/", payload)
