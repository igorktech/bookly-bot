from logger import configure_logger

logger = configure_logger()

class IntentCatcher:
    def __init__(self, model: str):
        self.model = model

    def predict(self, text: str) -> str:
        raise NotImplementedError


prompt = """Based on the user's message, your task is to identify the primary intent expressed. The user's messages can encompass various intents, each representing a specific type of request or response within a booking system. Below are the potential intents you should identify:

- Greeting: Any form of salutation or introductory message.
- Booking: Requests to make a new appointment or reservation.
- Cancel: Inquiries or requests to cancel an existing appointment or reservation.
- Confirmation: Messages seeking verification or acknowledgment of a booking or cancellation.
- Show: Requests to display or list details about appointments or reservations.
- Bye: Farewell or ending conversations.
- Thank You: Expressions of gratitude.
- Unclear: If the intent cannot be determined from the message.

Your goal is to read the user's message and accurately classify it into one of the above intents. Consider the context and keywords within the message to make your decision. If the message's intent is ambiguous or not directly related to the predefined intents, classify it as "Unclear".

Here are some examples to guide you:

1. User's message: "Hello, I'd like to check your availability for tomorrow."
   Identify the intent: Booking

2. User's message: "Can you confirm my appointment for next Wednesday?"
   Identify the intent: Confirmation

3. User's message: "Thanks for your help today."
   Identify the intent: Thank You

Remember, the clarity of your intent classification directly impacts the effectiveness of the booking bot's ability to respond appropriately to user inquiries. Approach each message with careful consideration to identify the most accurate intent.

User's message**: "{user_message}"

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
