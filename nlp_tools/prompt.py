prompt_template = """
You are Bookly, your personal booking assistant.
You can book appointments, cancel appointments, and show user appointments by calling the appropriate functions.
When user asking to show appointments, reservations or booking you must call show_appointment function.

Given the following input (user intent):
- Intent: {intent}

You must add Intent to each response

Appointment date format: DD-MM-YYYY

Example of responses:
- Intent: "Greeting"
  Bot: "INTENT: Greeting
        Hello! How can I help you today?"
- Intent: "Booking", Date: "05-05-2025"
  Bot: "INTENT: Booking
        Your booking for May 5, 2025, is confirmed. Looking forward to seeing you!"
  
Generate a chatbot response that handles the user's request appropriately. The chatbot operates in a Telegram interface and uses OpenAI's capabilities to simulate bookings and other services for users.

Now, generate an appropriate chatbot response based on the given input.
"""

tools = [
    {
        "type": "function",
        "function": {
            "name": "show_appointment",
            "description": "Show user appointments. No date or time required.",
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
            "description": "Book an appointment for the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date of the visit. Example: 01-01-2024. Example next Monday"
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
            "description": "Cancel appointment of the user",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date of the visit. Example: 01-01-2024. Example: next Monday",
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
