class MinMaxWordFinder:
    def __init__(self):
        self.word_list = []

    def add_sentence(self, value):
        self.word_list.extend(value.split())

    def shortest_words(self):
        len_list, check_len_word, answer = [len(i) for i in
                                            self.word_list], 0, []
        if len_list:
            check_len_word = min(len_list)
        for i in self.word_list:
            if len(i) == check_len_word:
                answer.append(i)
        return sorted(answer)

    def longest_words(self):
        len_list, check_len_word, answer = [len(i) for i in
                                            self.word_list], 0, []
        if len_list:
            check_len_word = max(len_list)
        for i in self.word_list:
            if len(i) == check_len_word:
                answer.append(i)
        return sorted(set(answer))


finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
