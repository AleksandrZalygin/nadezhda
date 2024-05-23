from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.

from calculator_factory import CalculatorFactory
from stack import Stack
from rpn_calculator import RPNCalculator
from gui import GUI

if __name__ == '__main__':
    root = Tk()
    factory = CalculatorFactory()
    stack = factory.create_stack()
    calculator = factory.create_calculator(stack)
    gui = factory.create_gui(root, calculator, stack)
    root.mainloop()
