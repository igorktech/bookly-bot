prompt_template = """
You are Bookly, your personal booking assistant.
You can book appointments, cancel appointments, and show user appointments by calling the appropriate functions.
Booking date doe not have strict format.

# Function Calls:
* When user asking to show appointments, reservations or booking you must call show_appointment function.
* When user want to cancel it reservation you must call cancel_appointment function.
* When user want to book it you must call book_appointment function.

Generate a chatbot response that handles the user's request appropriately. The chatbot operates in a Telegram interface and uses OpenAI's capabilities to simulate bookings and other services for users using Functions Calling.

Now, generate an appropriate chatbot response based on the given input.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "show_appointment",
            "description": "Show user appointments. No date or time required. "
                           "Example: Show. "
                           "Example: Show my appointments.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "book_appointment",
            "description": "Book an appointment for the user"
                           "Example: Book. "
                           "Example: Book an appointment next Monday"
                           "Example: reserve at 10:00. "
                           "Example: book on 01-01-2024 at 10 AM.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date of the visit. "
                                       "Example: 01-01-2024. "
                                       "Example: next Monday"
                    },
                    "time": {
                        "type": "string",
                        "description": "The time of the visit. Example: 10:00",
                    }
                },
                "required": ["date", "time"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancel_appointment",
            "description": "Cancel user appointment. "
                           "Example: Cancel. "
                           "Example: Cancel my appointment on 01-01-2024 at 10:00. "
                           "Example: cancel next Monday at 10:00."
                            "Example: delete my appointment.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date of the visit. "
                                       "Example: 01-01-2024. "
                                       "Example: next Monday",
                    },
                    "time": {
                        "type": "string",
                        "description": "The time of the visit. Example: 10:00",
                    }
                },
                "required": ["date", "time"]
            },
        }
    },
]
