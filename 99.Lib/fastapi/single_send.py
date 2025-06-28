from utils import URL, send_get, send_post

if __name__ == "__main__":
    send_get(f"{URL}/items/")
    send_get(f"{URL}/items?q=hello world&skip=123&limit=456")
    send_get(f"{URL}/items?skip=123&limit=456")

    send_get(f"{URL}/users/1")
    send_get(f"{URL}/users/123")

    send_get(f"{URL}/elements/")
    send_get(f"{URL}/elements/?q=qwer")
    send_get(f"{URL}/elements/?q=asdf&skip=123&limit=456")
    send_get(f"{URL}/elements/?q=ab")

    item1 = {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5,
    }
    send_post(f"{URL}/items/", item1)

    item2 = {
        "name": "Foo",
        "price": 45.2,
    }
    send_post(f"{URL}/items/", item2)

    send_get(f"{URL}/items/123")
    send_get(f"{URL}/items/0")
    send_get(f"{URL}/items/abc")
