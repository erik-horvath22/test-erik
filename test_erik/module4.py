from . import module1


def hello():
    print("This is the module 4 importing module1 saying hello")
    module1.hello()