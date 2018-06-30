import unittest


class Stack():

    def __init__(self):
        self.stk = []

    def pop(self):
        return self.stk.pop()

    def push(self, elt):
        self.stk.append(elt)

    def is_empty(self):
        return len(self.stk) == 0

    def peek(self):
        if not self.stk.is_empty():
            return self.stk[-1]


class Queue():

    def __init__(self):
        self.q = Stack()  
        self.b = Stack()  
        self.front = None

    def is_empty(self):
        return self.q.is_empty()

    def peek(self):
        if self.q.is_empty():
            return None
        else:
            return self.front

    def enqueue(self, elt):
        self.front = elt
        self.q.push(elt)

    def dequeue(self):
        while not self.q.is_empty() > 0:
            elt = self.q.pop()
            self.b.push(elt)
        val = self.b.pop()
        elt = None
        while not self.b.is_empty() > 0:
            elt = self.b.pop()
            self.q.push(elt)
        self.front = elt
        return val
# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)