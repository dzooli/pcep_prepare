from pprint import pprint

class ExampleClass(object):
    __private_classvar = 1
    __classvar: str = 'hello'
    __attr__ = ['x', 'y']
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.__private_x: int = 1
        __class__.__private_classvar = 2

    @classmethod
    def set_classvar(cls, val: str):
        cls.__classvar = val

if __name__ == "__main__":
    my_example = ExampleClass()
    my_example.z = 3
    my_example.__private_x = 2
    my_example.__private_classvar = 2
    my_example._ExampleClass__private_claasvar = 5
    pprint(vars(my_example))
    my_example.__private_y = 12
    ExampleClass.set_classvar('alma')
    pprint(vars(my_example))
    pprint(vars(ExampleClass))

