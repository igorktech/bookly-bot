from dateparser import parse
from dateparser.search import search_dates

class DateExtractor:
    def __init__(self):
        pass

    def extract(self, text):
        return search_dates(text)[0][1]
        # return parse(text)

# print(DateExtractor().extract("next Monday 10:00"))