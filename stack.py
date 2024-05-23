from tkinter import * # Import the essential modules for the graphical user interface.
from tkinter import ttk
import tkinter.messagebox # For MessageBox widget.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            tkinter.messagebox.showinfo("The error", "There is nothing on the stack.")
        else:
            return self.stack.pop()

    def delete_last(self):
        if len(self.stack) == 0:
            tkinter.messagebox.showinfo("The error", "There is nothing on the stack.")
        else:
            self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, index):
        return self.stack[index]

    def __setitem__(self, index, value):
        self.stack[index] = value

    def __delitem__(self, index):
        del self.stack[index]

    def __str__(self):
        return ', '.join(map(str, self.stack))