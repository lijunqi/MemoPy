
import __main__


def did_user_define_their_name():
    return 'my_name' in dir(__main__)


# ! Error: print("my_name id in namely 1:", id(__main__.my_name))


def print_user_name():
    if not did_user_define_their_name():
        raise ValueError('Define the variable `my_name`!')

    if '__file__' in dir(__main__):
        print(__main__.my_name, "found in file", __main__.__file__)
        print("my_name id in namely:", id(__main__.my_name))
    else:
        print(__main__.my_name)