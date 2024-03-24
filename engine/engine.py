from logger import configure_logger
from engine.builder import Builder
from nlp_tools.llm import generate_openai
from nlp_tools.prompt import prompt_template
from services.db_manager import add_message, get_messages
from services.appointment_manager import AppointmentManager

logger = configure_logger()

class Engine():
    def __init__(self, builder: Builder, appointment_manager: AppointmentManager):
        self.builder = builder
        self.appointment_manager = appointment_manager
        self.system_prompt = prompt_template

    def run_dm(self, chat_id, user_id, text: str):
        message_data = self.builder.process_input(text)
        intent = message_data["intent"]
        date = message_data["date"]
        if date:
            date = date[0]  # Get the first date

        state = self.get_state(user_id, intent, date)
        logger.info(f"State: {state}")
        messages = self.update_messages(chat_id, user_id, text)

        response = self.handle_dialogue(messages, state)
        add_message(chat_id, user_id, "assistant", response)
        return response

    def get_state(self, user_id, intent, date):

        result = {"availability": "N/A",
                  "action": None,
                  "date": date,
                  "intent": intent}

        if "Booking" in intent:
            self.appointment_manager.book_appointment(user_id, date)
        elif "Cancel" in intent:
            self.appointment_manager.cancel_appointment(user_id)
        elif "Confirmation" in intent:
            result["availability"] = self.appointment_manager.check_availability(date)
        elif "Show" in intent:
            date = self.appointment_manager.get_appointment(user_id)
            result["date"] = date

        return result

    def update_messages(self, chat_id, user_id, text: str):
        add_message(chat_id, user_id, "user", text)
        return get_messages(chat_id, user_id)

    def handle_dialogue(self, messages, state):

        system = [
            {"role": "system",
             "content": self.system_prompt.format(intent=state["intent"], date=state["date"],
                                                  availability=state["availability"])}
        ]
        if isinstance(messages, str):
            messages = [messages]
        messages = system + messages

        response = generate_openai(self.builder.tools.client,"gpt-3.5-turbo", messages)
        return response

chat_response = chat_completion_request(messages, tools)
assistant_message = chat_response.choices[0].message
assistant_message.content = str(assistant_message.tool_calls[0].function)
messages.append({"role": assistant_message.role, "content": assistant_message.content})
if assistant_message.tool_calls:
    results = execute_function_call(assistant_message)
def execute_function_call(message):
    if message.tool_calls[0].function.name == "ask_database":
        query = json.loads(message.tool_calls[0].function.arguments)["query"]
        results = ask_database(conn, query)
    else:
        results = f"Error: function {message.tool_calls[0].function.name} does not exist"
    return results