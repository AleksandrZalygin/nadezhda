from stack import Stack
from rpn_calculator import RPNCalculator
from gui import GUI

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CalculatorFactory(metaclass=SingletonMeta):
    def create_stack(self):
        return Stack()

    def create_calculator(self, stack):
        return RPNCalculator(stack)

    def create_gui(self, root, calculator, stack):
        return GUI(root, calculator, stack)
