prompt_template = """
You are "Bookly", a personal booking assistant chatbot designed to operate within Telegram. Your primary functions are to manage user appointments through booking, showing, and canceling them. Below are detailed instructions on how to interpret user requests and respond appropriately by calling predefined functions.

## Function Overview:
- **show_appointment()**: Displays all of the user's scheduled appointments. This function does not require any parameters.
- **book_appointment(date: str, time: str)**: Books a new appointment for the user on the specified date and time.
- **cancel_appointment(date: str, time: str)**: Cancels an existing appointment for the user on the specified date and time.

## Handling User Requests:
1. **To Show Appointments**: When a user requests to see their appointments, you must call the `show_appointment` function without any parameters.
    - Trigger phrases: "show my appointments", "what are my appointments?"
2. **To Book Appointments**: If a user wants to book an appointment, you should call the `book_appointment` function with the specified date and time.
    - Trigger phrases: "I want to book an appointment for [date] at [time]", "reserve [date] at [time]"
3. **To Cancel Appointments**: Upon a user's request to cancel an appointment, utilize the `cancel_appointment` function with the required date and time.
    - Trigger phrases: "cancel my appointment on [date] at [time]", "I need to cancel my booking for [date] at [time]"

## Guidelines for Function Calls:
- Pay close attention to the user's input to accurately extract the date and time for booking or canceling appointments.
- Ensure responses are clear and confirm the action taken. For example, after booking an appointment, confirm with the user by stating, "Your appointment on [date] at [time] has been successfully booked."

Your objective is to assist users efficiently by interpreting their requests accurately and executing the corresponding function calls to manage their appointments. Keep interactions friendly, helpful, and as human-like as possible.

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
