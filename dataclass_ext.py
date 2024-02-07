## dataclass_extfile

from dataclasses import dataclass

@dataclass
class Person:
    firstName: str
    lastName: str
    age: int

    def print(self):
        print(f"User: {self.firstName} {self.lastName},\nAge: {self.age}")


def demo():
    user = Person("John", "Doe", 37)

    print(user)
    user.print()
    print(user.firstName)


if __name__ == "__main__":
    demo()