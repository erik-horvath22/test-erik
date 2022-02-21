

class TestHandler:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


def test_module(a, b):
    return a + b