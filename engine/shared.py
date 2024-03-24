from nlp_tools.intent_catcher import IntentCatcher, IntentCatcherOpenAI
from nlp_tools.date_extractor import DateExtractor
from nlp_tools.prompt import tools
import openai

class Tools():
    def __init__(self, api_key, openai_tools=tools):
        openai.api_key = api_key
        self.client = openai.OpenAI()
        self.model = "gpt-3.5-turbo"
        self.openai_tools = openai_tools
        self.intent_catcher: IntentCatcher = IntentCatcherOpenAI(self.client)
        self.date_extractor: DateExtractor = DateExtractor()