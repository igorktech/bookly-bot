from logger import configure_logger

logger = configure_logger()

class IntentCatcher:
    def __init__(self, model: str):
        self.model = model

    def predict(self, text: str) -> str:
        raise NotImplementedError


prompt = """Based on the user's message, identify the intent of the message. The possible intents are "Greeting", "Booking", "Cancel", "Confirmation", "Show", "Bye", "Thank You". Use the information in the message to accurately classify the intent. If the intent is not clear from the message, you may classify it as "Unclear".

User's message: "{user_message}"

Identify the intent:"""


class IntentCatcherOpenAI(IntentCatcher):
    def __init__(self, client):
        super().__init__(model="gpt-3.5-turbo")
        self.client = client
        self.prompt = prompt

    def predict(self, message: str) -> str: # TODO: use llm.py to generate the intent
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt.format(user_message=message)}
            ],
            max_tokens=20
        )
        intent = completion.choices[0].message.content.strip()

        logger.info(f"Predicted intent: {intent}")

        return intent
