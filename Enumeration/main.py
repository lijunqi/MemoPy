from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


if __name__ == "__main__":
    print("Type of Color.RED: ", type(Color.RED))
    if Color['RED'] is Color.RED:
        print('Yes. RED')
    
    #if Color.get('red') == Color.RED:
    #    print('yes')
    #else:
    #    print('no')
