
import sys

from namely import print_user_name

my_name = "Jacky"
print("my_name id in main:", id(my_name))


def main():
    try:
        print_user_name()
    except ValueError as ve:
        return str(ve)


if __name__ == "__main__":
    print("This is start.")
    sys.exit(main())