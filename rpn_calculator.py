from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.

class RPNCalculator:
    def __init__(self, stack):
        self.stack = stack

    def performa(self):  # Addition
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            self.stack[-2] = self.stack[-2] + self.stack[-1]
            del self.stack[-1]
            if self.stack[-1] % 1 == 0.0:
                self.stack[-1] = int(self.stack[-1])

    def performs(self):  # Subtraction
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            self.stack[-2] = self.stack[-2] - self.stack[-1]
            del self.stack[-1]
            if self.stack[-1] % 1 == 0.0:
                self.stack[-1] = int(self.stack[-1])

    def performm(self):  # Multiplication
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            self.stack[-2] = self.stack[-2] * self.stack[-1]
            del self.stack[-1]
            if self.stack[-1] % 1 == 0.0:
                self.stack[-1] = int(self.stack[-1])

    def performd(self):  # Division
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            if self.stack[-1] == 0:
                tkinter.messagebox.showinfo("The error", "The divisor is 0, can't perform the division.")
            else:
                self.stack[-2] = int((self.stack[-2] / self.stack[-1]) * 1000000 + 0.5) / 1000000.0
                del self.stack[-1]
                if self.stack[-1] % 1 == 0.0:
                    self.stack[-1] = int(self.stack[-1])

    def performf(self):  # Factorial
        if len(self.stack) < 1:
            tkinter.messagebox.showinfo("The error", "At least 1 element in the stack is required.")
        elif type(self.stack[-1]) != int:
            tkinter.messagebox.showinfo("The error", "The type of the argument is not an integer.")
        elif self.stack[-1] < 0:
            tkinter.messagebox.showinfo("The error", "Unable to factor a negative number.")
        elif self.stack[-1] > 25:
            tkinter.messagebox.showinfo("The error", "The number is too large.")
        else:
            self.stack[-1] = self.factorial(self.stack[-1])

    def performp(self):  # Power
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            self.stack[-2] = self.stack[-2] ** self.stack[-1]
            del self.stack[-1]

    def performr(self):  # Root
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        else:
            self.stack[-2] = self.stack[-2] ** self.stack[-1]
            del self.stack[-1]

    def performmd(self):  # Modulo
        if len(self.stack) < 2:
            tkinter.messagebox.showinfo("The error", "At least 2 elements in the stack are required.")
        elif self.stack[-1] >= 0:
            self.stack[-2] = self.stack[-2] % self.stack[-1]
            del self.stack[-1]
        else:
            self.stack[-1] = -self.stack[-1]
            self.stack[-2] = self.stack[-2] % self.stack[-1]
            del self.stack[-1]

    def factorial(self, number):  # Factorial helper method
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)
