from parsers import WordParser
from randomwords import RandomWord


class PasswordGenerator(object):
    def __init__(self, config):
        self.config = config

        parser = WordParser()
        wordlist = parser.parse('./' + self.config.language + '/' + self.config.language + '_words.txt')
        self.randomwords = RandomWord(wordlist)

        adjectives_list = parser.parse('./' + self.config.language + '/' + self.config.language + '_adjectives.txt')
        self.random_adjectives = RandomWord(adjectives_list)

        nouns_list = parser.parse('./' + self.config.language + '/' + self.config.language + '_nouns.txt')
        self.random_nouns = RandomWord(nouns_list)

        verb_list = parser.parse('./' + self.config.language + '/' + self.config.language + '_verbs.txt')
        self.random_verbs = RandomWord(verb_list)

    def generate_password(self):
        for i in range(30, 0, -1):
            if self.config.prefix:
                password = self.generate_shortcut_password(self.config.prefix, self.config.separator)
            elif self.config.chain:
                password = self.generate_end_begin_password(self.config.words, self.config.separator)
            elif self.config.sentence:
                password = self.generate_pass_sentence(self.config.separator)
            else:
                password = self.generate_simple_password(self.config.separator, self.config.words)

            if 12 <= len(password) <= self.config.length:
                return password
        raise ValueError('Please, try again with a different password length, or change a number of words.')

    def generate_simple_password(self, separator, n):
        password = self.randomwords.randwords(n)
        return separator.join(password)

    def generate_shortcut_password(self, prefix, separator):
        password = self.randomwords.randwords_prefix(prefix)
        return separator.join(password)

    def generate_end_begin_password(self, n, separator):
        password = self.randomwords.randwords_endbegin(n)
        return separator.join(password)

    def generate_pass_sentence(self, separator='.'):
        return separator.join(
            [self.random_adjectives.randword(), self.random_nouns.randword(), self.random_verbs.randword()])
