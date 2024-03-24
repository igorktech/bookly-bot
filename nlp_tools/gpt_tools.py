tools = tools = [
    {
        "type": "function",
        "function": {
            "name": "show_appointments",
            "description": "Show user booked appointments",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
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
                        "description": "The date of the visit. Example: 01-01-2024",
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
                        "description": "The date of the visit. Example: 01-01-2024",
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