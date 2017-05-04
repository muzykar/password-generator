import os


class WordParser(object):
    def __init__(self):
        self.parsers = [TextParser()]

    def supports(self, file):
        for parser in self.parsers:
            if parser.supports(file):
                return True
        return False

    def parse(self, file):
        for parser in self.parsers:
            if parser.supports(file):
                return parser.parse(file)


class TextParser(object):
    def __init__(self):
        pass

    def supports(self, file):
        file_extension = os.path.splitext(file)[1][1:]
        return file_extension == 'txt'

    def parse(self, file):
        with open(file, 'r') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        return content
