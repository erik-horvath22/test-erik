from .helpers import module3


def hello():
    print("This is the module 4 importing module1 saying hello")
    module3.hello()