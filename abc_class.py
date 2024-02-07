from abc import ABC , abstractmethod
import os

## This is bad code. For the assignment atleast. 
## However, it runs. I've been stuck on this all 
## day, and it runs. I'm calling that a victory.

class object(ABC):

    @abstractmethod
    def update(self,data):
        pass
    
    @abstractmethod
    def print(self):
        pass

class person(object):
    def __init__(self, name):
        self.name = name

    def update(self,name):
        self.name = name
    
    def print(self):
        print(self.name)

class number(object):
    def __init__(self, data):
        self.data = data

    def update(self, data):
        self.data = data
    
    def print(self):
        print(self.data)

def demo():
    print("Hello world")
    faculty = person("John Doe")
    faculty.print()

if __name__ == "__main__":
    demo()