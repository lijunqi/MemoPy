import importlib

def main():
    print("=== Begin main")
    m = importlib.import_module("myModule")
    print("=== After import.")
    print("=== double_it(1) = ", m.double_it(1))
    print("=== a = ", m.a)

if __name__ == "__main__":
    main()
