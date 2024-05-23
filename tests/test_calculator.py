import unittest
from rpn_calculator import RPNCalculator
from stack import Stack
from gui import GUI
from unittest.mock import MagicMock, patch

from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.

class TestRPNCalculator(unittest.TestCase):
    def test_performa_addition(self):
        stack = Stack()
        calculator = RPNCalculator(stack)
        stack.push(2)
        stack.push(3)
        calculator.performa()
        self.assertEqual(stack[0], 5)

    # Другие тесты для методов RPNCalculator

class TestGUI(unittest.TestCase):
    @patch('calculator.Button', MagicMock)
    def test_setup_ui(self):
        root = MagicMock()
        calculator = MagicMock()
        stack = MagicMock()
        gui = GUI(root, calculator, stack)
        gui.setup_ui()
        root.grid.assert_called_once()
