class Queue:
    def __init__(self, *values):
        self.data = list(values)

    def append(self, *values):
        self.data += list(values)

    def __str__(self):
        return '[' + ' -> '.join(map(str, self.data)) + ']'

    def copy(self):
        return Queue(*self.data)

    def pop(self):
        return self.data.pop(0)

    def extend(self, queue):
        self.data.extend(queue.data)

    def __next__(self):
        n = self.data[1:]
        return Queue(*n)

    def next(self):
        n = self.data[1:]
        return Queue(*n)

    def __add__(self, other):
        return Queue(*(self.data + other.data))

    def __iadd__(self, other):
        return Queue(*(self.data + other.data))

    def __eq__(self, other):
        return self.data[:] == other.data[:]

    def __rshift__(self, other):
        n = self.data[other:]
        return Queue(*n)

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
print()
print()
