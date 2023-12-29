
class MyConnectException(Exception):
    code = 1
    info = "[My connect exception]"

    def __init__(self, msg: object="") -> None:
        self.msg = msg

    def __str__(self):
        return f"{self.info}{str(self.msg)}"

class YourConnectException(MyConnectException):
    code = 2
    info = "[Your connect exception]"

class HisConnectException(MyConnectException):
    code = 3
    info = "[His connect exception]"

class SomeParams:
    def __init__(self) -> None:
        self.data = 123456

def foo1():
    print("Go foo1.")
    raise MyConnectException("DB connect failed")

def foo2():
    print("Go foo2.")
    raise MyConnectException({
        'a': 123,
        'b': "asdf",
        'c': {
            'd': 456
        }
    })

def foo3():
    print("Go foo3.")
    raise YourConnectException("DB connect failed")

def foo4():
    print("Go foo4.")
    raise YourConnectException({
        'a': 321,
        'b': "fdsa",
        'c': {
            'd': 654
        }
    })

def foo5():
    print("Go foo5.")
    sp = SomeParams()
    raise YourConnectException(sp)

if __name__ == "__main__":
    try:
        foo1()
    except MyConnectException as exc:
        print("Catch foo1: exc.code = ", exc.code)
        print("Catch foo1: exc.info = ", exc.info)
        print("Catch foo1: str(exc) = ", str(exc))
        print("Catch foo1: exc = ", exc)

    try:
        foo2()
    except MyConnectException as exc:
        print("Catch foo2: exc.code = ", exc.code)
        print("Catch foo2: exc.info = ", exc.info)
        print("Catch foo2: str(exc) = ", str(exc))
        print("Catch foo2: exc = ", exc)

    try:
        foo3()
    except YourConnectException as exc:
        print("Catch foo3: exc.code = ", exc.code)
        print("Catch foo3: exc.info = ", exc.info)
        print("Catch foo3: str(exc) = ", str(exc))
        print("Catch foo3: exc = ", exc)
        print(exc)

    try:
        foo4()
    except YourConnectException as exc:
        print("Catch foo4: exc.code = ", exc.code)
        print("Catch foo4: exc.info = ", exc.info)
        print("Catch foo4: str(exc) = ", str(exc))
        print("Catch foo4: exc = ", exc)
        print("Catch foo4: exc.msg['a'] = ", exc.msg['a'])
        print(exc)

    try:
        foo5()
    except YourConnectException as exc:
        print("Catch foo5: exc.code = ", exc.code)
        print("Catch foo5: exc.info = ", exc.info)
        print("Catch foo5: str(exc) = ", str(exc))
        print("Catch foo5: exc = ", exc)
        if isinstance(exc.msg, SomeParams):
            print("Msg is SomeParams.")
        else:
            print("Msg is NOT SomeParams.")
        if isinstance(exc, YourConnectException):
            print("exc is YourConnectException.")
        else:
            print("exc is NOT YourConnectException.")

        if isinstance(exc, HisConnectException):
            print("exc is HisConnectException.")
        else:
            print("exc is NOT HisConnectException.")
    finally:
        print("In finally, exc = ", exc)
