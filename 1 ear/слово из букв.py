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
        self.data += other.data
        return self

    def __eq__(self, other):
        return self.data[:] == other.data[:]

    def __rshift__(self, other):
        n = self.data[other:]
        return Queue(*n)


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
        self.data += other.data
        return self

    def __eq__(self, other):
        return self.data[:] == other.data[:]

    def __rshift__(self, other):
        n = self.data[other:]
        return Queue(*n)
