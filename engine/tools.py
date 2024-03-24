from engine.shared import Tools
from engine.builder import Builder

class Tools(Tools):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.builder: Builder = Builder(self)
