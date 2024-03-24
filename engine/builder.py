# builder.py

from engine.shared import Tools
from nlp_tools.llm import generate_openai

class Builder:
    def __init__(self, tools: Tools):
        self.tools = tools

    def process_input(self, text: str):
        message_data = {"intent": self.tools.intent_catcher.predict(text),
                        "date": self.tools.date_extractor.extract(text)}
        return message_data

    def generate_message(self, messages: list[str]):
        return generate_openai(self.tools.client, self.tools.model, messages)