class Queue:
    def __init__(self, *values):
        self.nums = []
        self.data = " "
        for i in values:
            self.nums.append(i)

    def append(self, *values):
        for i in values:
            self.nums.append(i)

    def copy(self):
        new = Queue()
        new.nums += self.nums
        return new

    def pop(self):
        if self.nums:
            first = self.nums[0]
            del self.nums[0]
            return first

    def extend(self, queue):
        self.nums += queue.nums

    def next(self):
        new = self.copy()
        new.nums = new.nums[1:]
        return new

    def __rshift__(self, n):
        if len(self.nums) > n:
            new = Queue()
            new.nums += self.nums[n:]
            return new
        return Queue()

    def __add__(self, other):
        new = self.copy()
        new.nums += other.nums
        return new

    def __iadd__(self, other):
        self.data += other.data
        return self

    def __eq__(self, other):
        if self.nums == other.nums:
            return True
        return False

    def __str__(self):
        if self.nums:
            self.nums = list(map(str, self.nums))
            nums = ' -> '.join(self.nums)
            return f'[{nums}]'
        return '[]'

    def __next__(self):
        n = self.data[1:]
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

