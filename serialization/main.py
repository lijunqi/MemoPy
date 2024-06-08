import json
import pickle

class A:
    cnt = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.result = Result(123)

class Result:
    def __init__(self, data) -> None:
        self.data = data

def use_json(raw_data):
    return json.dumps(raw_data)

def use_pickle(raw_data):
    return pickle.dumps(raw_data)

def main():
    a = A("Tom", 11)
    a.result = Result(123)
    a.cnt = 1

    try:
        use_json(a)
    except TypeError as exc:
        print("xxx JSON serial failed: ", str(exc))
    
    p_serial = use_pickle(a)
    print(p_serial)

    a_remote = pickle.loads(p_serial)
    print("Remote: ", a_remote.name, a_remote.age, a_remote.result.data)

if __name__ == "__main__":
    main()