from parsers import WordParser
from randomwords import RandomWord


class PasswordGenerator(object):
    def __init__(self, words_file):
        parser = WordParser()
        wordlist = parser.parse(words_file)
        self.randomwords = RandomWord(wordlist)

    def generate_simple_password(self, n=4, separator='/'):
        password = self.randomwords.randwords(n)
        return separator.join(password)

    def generate_shortcut_password(self, prefix, separator='/'):
        password = self.randomwords.randwords_prefix(prefix)
        return prefix, separator.join(password)

    def generate_end_begin_password(self, n, separator='/'):
        password = self.randomwords.randwords_endbegin(n)
        return separator.join(password)
