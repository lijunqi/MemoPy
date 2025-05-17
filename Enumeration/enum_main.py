from enum import Enum


class Color(Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'

class Constants(Enum):
    ONE = 1
    TWO = 2
    THREE = 3



if __name__ == "__main__":
    print(f"{type(Color.RED) = }")
    print(f"{Color['RED'] is Color.RED = }")
    print(f"{Color.RED.name = }")
    print(f"{Color.RED.value = }")
    #print(f"{Color.get('red') == Color.RED = }")

    try:
        # ! Error: '<' not supported between instances of 'Constants' and 'Constants'
        Constants.ONE < Constants.TWO
    except TypeError as exc:
        print(exc)

    print(f"{Color('red') = }")

    print(f"{' Check attr ':=^30}")
    print(f"{getattr(Color, 'red', None) = }")
    print(f"{getattr(Color, 'RED', None) = }")
    print(f"{getattr(Color, 'invalid', None) = }")
    print(f"{getattr(Color, 'invalid', Color.RED) = }")

    print(f"{' enum is iterable ':=^30}")
    for member in Color:
        print(repr(member))

    print(f"{' Check attr ':=^30}")
    print(f"{'RED' in Color.__members__ = }") # check key 'RED' exist or not
    print(f"{'red' in Color.__members__ = }")
    print(f"{'invalid' in Color.__members__ = }")
    print(f"{'RED' in Color = }")
    print(f"{'red' in Color = }") # check value 'red' exist or not
