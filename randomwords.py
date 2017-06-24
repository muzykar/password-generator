import random


class RandomWord(object):
    def __init__(self, words):
        self.words = words

    def randword(self, blacklist=[]):
        rand_word = random.choice(self.words)
        while rand_word in blacklist:
            rand_word = rand_word.choice(self.words)
        return rand_word

    def randword_prefix(self, prefix):
        while True:
            randword = self.randword()
            if randword.startswith(prefix.lower()):
                return randword

    def randwords(self, n):
        return random.sample(self.words, n)

    def randwords_prefix(self, prefix):
        prefix_list = list(prefix)
        word_list = []
        for letter in prefix_list:
            random_word = self.randword_prefix(letter)
            while random_word in word_list:
                random_word = self.randword_prefix(letter)
            word_list.append(random_word)
        return word_list

    def randwords_endbegin(self, n):
        word = self.randword()
        word_list = [word]

        while len(word_list) < n:
            last = word[-1]
            word = self.randword_prefix(last)
            while word in word_list:
                word = self.randword_prefix(last)
            word_list.append(word)
        return word_list
