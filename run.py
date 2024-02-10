from module_1 import function1 as func1
from module_2 import function2 as func2
from module_3 import function3 as func3

def demo():
    #int data = {}
    data = func1.start()
    func3.end(data)
    for i in range(0,10):
        data = func2.middle(data)
    func3.end(data)
    func3.goodbye()

if __name__ == "__main__":
    demo()