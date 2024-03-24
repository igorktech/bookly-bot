from dateparser import parse


class DateExtractor:
    def __init__(self):
        pass

    def extract(self, text):
        return parse(text)