from abc import ABC, abstractmethod

class Fruit(ABC):

    @abstractmethod
    def have_seed(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Apple(Fruit):
    def have_seed(self):
        return True


class Pear(Fruit):
    def have_seed(self):
        return True
    
    def color(self):
        return 'yellow'


if __name__ == "__main__":
    # ! Error: Can't instantiate abstract class Fruit without an implementation
    # !        for abstract methods 'color', 'have_seed'
    #f = Fruit()
    #apple = Apple()
    pear = Pear()
