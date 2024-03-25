import json
from datetime import datetime

from openai import BadRequestError

from logger import configure_logger
from engine.builder import Builder
from nlp_tools.prompt import prompt_template
from services.db_manager import write_messages, get_messages
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

        messages = get_messages(chat_id, user_id)
        messages.append({"role": "user", "content": text if text else "empty message"})
        response = self.handle_dialogue(user_id, messages, intent)

        write_messages(chat_id, user_id, messages)
        response = f"INTENT: {intent}\n{response}"
        return response

    def handle_dialogue(self, user_id, messages, intent=None):

        system = [
            {"role": "system",
             "content": self.system_prompt}
        ]

        try:
            response = self.builder.get_chat_completion(system + messages)
            logger.info(f"Assistant response: {response}")
        except BadRequestError as e:
            logger.error(f"Failed to get chat completion: {e}")
            return str(e)

        if response.choices:
            assistant_message = response.choices[0].message
            logger.info(f"Assistant message: {assistant_message}")
        else:
            return "No response"

        if assistant_message.tool_calls:
            result = self.execute_function_call(user_id, assistant_message)
            logger.info(f"Function call result: {result}")

            d = {"role": "function",
                 # "tool_call_id": assistant_message.tool_calls[0].id,
                 "name": assistant_message.tool_calls[0].function.name,
                 "content": str(result) if result else "No result"}
            messages.append(d)

            response = self.builder.get_chat_completion(system + messages)
            logger.info(f"Assistant response: {response}")
            if response.choices:
                assistant_message = response.choices[0].message
            else:
                return "No response"

        messages.append({"role": "assistant", "content": assistant_message.content if assistant_message.content else "No message"})
        return assistant_message.content

    def execute_function_call(self, user_id, message):
        function_name = message.tool_calls[0].function.name
        logger.info(f"Executing function call: {function_name}")

        if function_name == "book_appointment":
            args = json.loads(message.tool_calls[0].function.arguments)
            date = args["date"]
            time = args["time"]
            result = "N/A"

            appointment_datetime_str = f"{date} {time}"
            appointment_datetime = self.builder.tools.date_extractor.extract(appointment_datetime_str)

            if appointment_datetime and self.appointment_manager.check_availability(appointment_datetime):
                self.appointment_manager.book_appointment(user_id, appointment_datetime.strftime("%Y-%m-%d %H:%M"))
                result = f"Booking reserved successfully for {appointment_datetime.strftime('%Y-%m-%d %H:%M')}."

            logger.info(f"Appointment {appointment_datetime} is {result}")

        elif function_name == "cancel_appointment":
            args = json.loads(message.tool_calls[0].function.arguments)
            date = args["date"]
            time = args["time"]

            appointment_datetime_str = f"{date} {time}"
            appointment_datetime = self.builder.tools.date_extractor.extract(appointment_datetime_str)

            if appointment_datetime:
                cancellation_result = self.appointment_manager.cancel_appointment(user_id,
                                                                                  appointment_datetime.strftime(
                                                                                      "%Y-%m-%d %H:%M"))
                if cancellation_result:
                    result = f"Appointment for {appointment_datetime.strftime('%Y-%m-%d %H:%M')} cancelled successfully."
                else:
                    result = "Could not find an appointment to cancel."
            else:
                result = "Invalid date or time format."

        elif function_name == "show_appointment":
            appointments = self.appointment_manager.get_appointment(user_id)
            if appointments:
                result = "You have the following appointments:\n"
                for appointment in appointments:
                    result += f"{appointment}\n"
                result = appointments
            else:
                result = "You have no appointments"

        else:
            result = f"Error: function {function_name} does not exist"

        return result
