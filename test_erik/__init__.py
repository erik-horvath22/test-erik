from .module1 import hello as hello1
from .module2 import hello as hello2
def hello(target="World"):
    print("Hello {}!".format(target))