# builder.py

from engine.shared import Tools
from nlp_tools.llm import chat_completion_request


class Builder:
    def __init__(self, tools: Tools):
        self.tools = tools

    def process_input(self, text: str):
        message_data = {"intent": self.tools.intent_catcher.predict(text)}
        return message_data

    def get_chat_completion(self, messages, tool_choice="auto"):
        return chat_completion_request(self.tools.client, messages, tools=self.tools.openai_tools,
                                       tool_choice=tool_choice, model=self.tools.model)
