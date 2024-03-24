from nlp_tools.date_extractor import DateExtractor
from nlp_tools.intent_catcher import IntentCatcher, IntentCatcherOpenAI
import openai

class Tools():
    def __init__(self, api_key):
        openai.api_key = api_key
        self.client = openai.OpenAI()
        self.date_extractor: DateExtractor = DateExtractor()
        self.intent_catcher: IntentCatcher = IntentCatcherOpenAI(self.client)