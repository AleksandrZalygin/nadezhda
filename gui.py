import tkinter as tk
from tkinter import ttk, messagebox

class GUI:
    def __init__(self, root, calculator, stack):
        self.root = root
        self.calculator = calculator
        self.stack = stack
        self.argument = tk.StringVar()
        self.stacklist = tk.StringVar()
        self.num = ''

        self.setup_ui()

    def setup_ui(self):
        self.root.title("RPN Calc 1.1 by Shino")
        self.root.resizable(0, 0)
        mf = ttk.Frame(self.root)
        mf.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        label0 = tk.Label(mf, textvariable=self.stacklist)
        label0.grid(row=0, columnspan=3)
        label1 = tk.Label(mf, textvariable=self.argument, background="white")
        label1.grid(row=0, column=3)

        buttons = [
            ('7', self.construct_digit('7'), 0, 2),
            ('8', self.construct_digit('8'), 1, 2),
            ('9', self.construct_digit('9'), 2, 2),
            ('+', self.calculator.performa, 3, 2),
            ('4', self.construct_digit('4'), 0, 3),
            ('5', self.construct_digit('5'), 1, 3),
            ('6', self.construct_digit('6'), 2, 3),
            ('-', self.calculator.performs, 3, 3),
            ('1', self.construct_digit('1'), 0, 4),
            ('2', self.construct_digit('2'), 1, 4),
            ('3', self.construct_digit('3'), 2, 4),
            ('*', self.calculator.performm, 3, 4),
            ('0', self.construct_digit('0'), 0, 5),
            ('.', self.construct_dot, 1, 5),
            ('!', self.calculator.performf, 2, 5),
            ('/', self.calculator.performd, 3, 5),
            ('Push!', self.push, 3, 1),
            ('neg', self.construct_minus, 2, 1),
            ('<-', self.go_back, 1, 1),
            ('<- (st)', self.delete_from_stack, 0, 1)
        ]

        for (text, command, col, row) in buttons:
            button = tk.Button(mf, text=text, command=command, width=5, height=2)
            button.grid(column=col, row=row)

        self.root.mainloop()

    def construct_digit(self, digit):
        def wrapper():
            if self.num == '0' and digit == '0':
                messagebox.showinfo("The error", "Can't begin with a zero.")
            else:
                self.num += digit
                self.argument.set(self.num)
        return wrapper

    def construct_dot(self):
        if '.' in self.num:
            messagebox.showinfo("The error", "A dot is used already.")
        elif self.num == '':
            self.num += "0."
            self.argument.set(self.num)
        else:
            self.num += '.'
            self.argument.set(self.num)

    def construct_minus(self):
        if self.num == '':
            self.num += '-'
            self.argument.set(self.num)
        else:
            messagebox.showinfo("The error", "A minus can be put only in the beginning.")

    def go_back(self):
        if self.num == '':
            messagebox.showinfo("The error", "It's empty already.")
        else:
            self.num = self.num[:-1]
            self.argument.set(self.num)

    def delete_from_stack(self):
        self.stack.delete_last()
        self.stacklist.set(str(self.stack))

    def push(self):
        if self.num == '' or self.num == '-':
            messagebox.showinfo("The error", "The number is not complete.")
        elif self.num == '-0' or self.num == '-0.0':
            self.stack.push(0)
            self.stacklist.set(str(self.stack))
            self.argument.set('')
            self.num = ''
        else:
            try:
                value = float(self.num)
                if value % 1 == 0.0:
                    self.stack.push(int(value))
                else:
                    self.stack.push(value)
                self.stacklist.set(str(self.stack))
                self.argument.set('')
                self.num = ''
            except ValueError:
                messagebox.showinfo("The error", "Invalid number")
