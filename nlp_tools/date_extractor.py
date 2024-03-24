from dateparser.search import search_dates


class DateExtractor:
    def __init__(self):
        pass

    def extract(self, text):
        found_dates = search_dates(text)
        extracted_dates = []

        if found_dates is not None:
            for _, date_obj in found_dates:
                formatted_date = date_obj.strftime('%d-%m-%Y')
                extracted_dates.append(formatted_date)

        return extracted_dates
