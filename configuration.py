class PasswordGeneratorConfiguration(object):
    def __init__(self, words, separator, prefix, chain, length, sentence, language):

        self.prefix = prefix
        self.chain = chain
        self.min_length = 12

        if words is None:
            self.words = 5
        elif words < 2 or words > 24:
            raise ValueError("Number of words must be between 2 and 19, but was %d." % words)
        else:
            self.words = words

        if separator is None:
            if sentence:
                self.separator = '.'
            else:
                self.separator = '/'
        else:
            self.separator = separator

        if length is None:
            self.length = 7 * self.words
        elif self.min_length > length or length > 127:
            raise ValueError("Length must be between 12 and 127, but was %d." % length)
        else:
            self.length = length

        self.sentence = sentence

        if language is None:
            self.language = 'en'
        else:
            self.language = language
