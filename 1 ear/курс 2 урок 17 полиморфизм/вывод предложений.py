class LeftParagraph():
    def __init__(self, length):
        self.length = length
        self.array = ['']
        self.k = 0

    def add_word(self, world):
        if len(self.array[-1]) + len(world) <= self.length - 1:
            if self.k != 0:
                self.array[-1] += ' ' + world
            elif self.array[-1] == '':
                self.array[-1] += world
                self.k = 1
        else:
            self.array[-1].ljust(self.length)
            self.array.append(world)

    def end(self):
        if self.array[0] == "":
            del self.array[0]
        for i in self.array:
            print('{0:<{1}}'.format(i, self.length))
        self.array = ['']


class RightParagraph():
    def __init__(self, length):
        self.length = length
        self.array = ['']
        self.k = 0

    def add_word(self, world):
        if len(self.array[-1]) + len(world) <= self.length - 1:
            if self.k != 0:
                self.array[-1] += ' ' + world
            else:
                self.array[-1] += world
                self.k = 1
        else:
            self.array[-1].ljust(self.length)
            self.array.append(world)

    def end(self):
        if self.array[0] == "":
            del self.array[0]

        for i in self.array:
            print('{0:>{1}}'.format(i, self.length))

        self.array = ['']



lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()