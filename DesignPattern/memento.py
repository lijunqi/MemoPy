# Memento Pattern with Python Code
from abc import abstractmethod,ABCMeta

class Memento():
    _state = ""
    def __init__(self,strState):
        self._state = strState
    def getState(self):
        return self._state

class Originator():
    _state = ""
    def setState(self,strState):
        self._state = strState
    def getState(self):
        return self._state
    def saveStateToMemento(self):
        return Memento(self._state)
    def getStateFromMemento(self,inMemento):
        self._state = inMemento.getState()

class CareTaker():
    _mementoList = []
    def add(self,inMemento):
        self._mementoList.append(inMemento)
    def get(self,inIndex):
        return self._mementoList[inIndex]

if __name__ == '__main__':
    originator = Originator()
    careTaker = CareTaker()
    originator.setState("State #1")
    originator.setState("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #4")

    print("Current State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State: " +  originator.getState())
    originator.getStateFromMemento(careTaker.get(1))
    print("Second saved State: " +  originator.getState())
