## dataclassfile

from dataclasses import dataclass

@dataclass
class Person:
    firstName: str
    lastName: str
    age: int

def demo():
    user = Person("John", "Doe", 37)

    print(user)
    print(user.firstName)


if __name__ == "__main__":
    demo()