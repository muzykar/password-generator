class PasswordGeneratorConfiguration(object):
    def __init__(self, words, separator, prefix, chain, length, sentence, language):

        self.prefix = prefix
        self.chain = chain

        if words is None:
            self.words = 4
        elif words < 2 or words > 19:
            raise ValueError("Number of words must be between 2 and 19, but was %d." % words)
        else:
            self.words = words

        if separator is None:
            self.separator = '/'
        else:
            self.separator = separator

        if length is None:
            self.length = 50
        elif 12 > length or length > 127:
            raise ValueError("Length must be between 12 and 127, but was %d." % length)
        else:
            self.length = length

        self.sentence = sentence

        if language is None:
            self.language = 'en'
        else:
            self.language = language