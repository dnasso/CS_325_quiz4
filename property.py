class Person:
    #name: str

    def __init__(self, text=''):
        self._name = text
    @property

    def name(self):
        return self._name
    
    @name.setter
    def name(self, text):
        self._name = text

    @name.deleter
    def name(self):
       del self._name

def demo():
    faculty = Person('Greg')
    print("Name is " + faculty.name)

if __name__ == "__main__":
    demo()