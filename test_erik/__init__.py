from .module1 import hello as hello1
from .module2 import hello as hello2
from .module4 import hello as hello4
def hello(target="World"):
    print("Hello {}!".format(target))