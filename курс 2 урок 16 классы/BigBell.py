class BigBell:
    def __init__(self):
        self.n = 0

    def sound(self):
        if self.n % 2 == 0 or self.n == 0:
            print("ding")
            self.n += 1
        else:
            print("dong")
            self.n += 1
