from engine.shared import Tools
from engine.builder import Builder
from nlp_tools.prompt import tools

class Tools(Tools):
    def __init__(self, api_key, openai_tools=tools):
        super().__init__(api_key, openai_tools=openai_tools)
        self.builder: Builder = Builder(self)
