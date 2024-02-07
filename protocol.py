from typing import Protocol
import os

class object(Protocol):
    def update():
        ...
    def print():
        ...
class person:
    def __init__(self, name):
        self.name = name

    def update(self,name):
        self.name = name
    
    def print(self):
        print(self.name)


class object:
    def __init__(self, data):
        self.data = data

    def update(self, data):
        self.data = data
    
    def print(self):
        print(self.data)

def demo():
    print("Hello World")
    faculty = person("John Doe")
    faculty.print()

if __name__ == "__main__":
    demo()