prompt_template = """
Given the following inputs:
- User intent: {intent}
- Date provided by the user: {date}
- Availability of the date: {availability}

Generate a chatbot response that handles the user's request appropriately. The chatbot operates in a Telegram interface and uses OpenAI's capabilities to simulate bookings and other services for users.

Rules for Bot Logic Responses:
1. If the intent is "Greeting", the bot should greet the user and ask how it can assist.
2. If the intent is "Booking" and a date is provided and available, confirm the booking for that date.
3. If the intent is "Booking" but no date is provided, ask the user for a specific date.
4. If the intent is "Booking" and the date is not available, inform the user and suggest choosing another date.
5. If the intent is "Show", and date is valid display the user's existing appointment.
6. If the intent is "Show", and date is not valid, ask the user to provide a date.
7. If the intent is "Cancel", confirm the cancellation of the user's appointment.
8. If the intent is "Confirmation", confirm the details of the user's existing appointment.
9. If the intent is "Bye" or "Thank You", end the conversation.
10. For any other intent, indicate confusion and ask the user to clarify their request.

Example Dialogues Based on Intent:
- Intent: "Greeting"
  Bot: "Hello! How can I help you today?"
- Intent: "Booking", Date: "2025-05-05", Availability: "Available"
  Bot: "Your booking for May 5, 2025, is confirmed. Looking forward to seeing you!"
- Intent: "Booking", Date: "None", Availability: "N/A"
  Bot: "Could you please provide a specific date for your booking?"
- Intent: "Booking", Date: "2025-05-05", Availability: "Not Available"
  Bot: "Unfortunately, we're fully booked on May 5, 2025. Could you choose another date?"
- Intent: "Cancel"
  Bot: "Your appointment has been successfully canceled."
- Intent: "Confirmation"
  Bot: "Your appointment is confirmed. We are excited to see you!"

Now, generate an appropriate chatbot response based on the given inputs.
"""