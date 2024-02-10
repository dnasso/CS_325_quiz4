class Person:
    name: str

    def __init__(self, text=''):
        self.name = text

    ### Am I misunderstanding this? Because this seems really simple.

def demo():
    faculty = Person('Greg')
    print("Name is " + faculty.name)
    faculty.name = 'Dave'
    print("Name is " + faculty.name)
    

if __name__ == "__main__":
    demo()