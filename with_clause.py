
# a good doc: https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/

# Format:
# with context_expression [as target(s)]:
#     with-body

# Context Management Protocol supported
class DummyResource:
    def __init__(self):
        print("Resource init.")

    def __enter__(self):
        print("[Enter]: Allocate resource.")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("[Exit]: Free resource.")
        if exc_tb is None:
            print("[Exit]: Exited without exception.")
        else:
            print("[Exit]: Exited with exception.")


def main():
    with DummyResource() as dummy_resource:
        print("Do somthing with resource.")

if __name__ == "__main__":
    main()