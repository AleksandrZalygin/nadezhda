from stack import Stack

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack[0], 1)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        popped_value = self.stack.pop()
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(popped_value, 2)

    def test_delete_last(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.delete_last()
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack[0], 1)

if __name__ == '__main__':
    unittest.main()
