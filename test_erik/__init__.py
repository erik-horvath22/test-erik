from .module1 import hello as hello1
from .module2 import hello as hello2
from .helpers.module3 import hello as hello3
def hello(target="World"):
    print("Hello {}!".format(target))