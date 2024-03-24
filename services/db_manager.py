from db.mongo import MongoDBClient

db_client = MongoDBClient()
db = db_client.get_db()
users_collection = db["users"]


def delete_user(user_id):
    """
    Delete a user and all their associated data.
    """
    users_collection.delete_one({"user_id": user_id})

def add_chat(chat_id, user_id):
    """
    Add a new chat to the chats array for a user if it doesn't already exist.
    """
    users_collection.update_one(
        {"user_id": user_id, "chats.chat_id": {"$ne": chat_id}},
        {"$push": {"chats": {"chat_id": chat_id, "messages": []}}}
    )

def add_message(chat_id, user_id, role, content):
    """
    Append a new message to the conversation for a user in a specific chat.
    """
    # Ensure the chat exists before adding a message to it
    add_chat(chat_id, user_id)

    message_doc = {"role": role, "content": content}
    users_collection.update_one(
        {"user_id": user_id, "chats.chat_id": chat_id},
        {"$push": {"chats.$.messages": message_doc}}
    )


def get_messages(chat_id, user_id):
    """
    Get the conversation history as a list of messages for a user in a specific chat.
    """
    user_doc = users_collection.find_one(
        {"user_id": user_id},
        {"_id": 0, "chats": 1}
    )
    if user_doc:
        for chat in user_doc["chats"]:
            if chat["chat_id"] == chat_id:
                return chat["messages"]
    return []


def add_user_appointment(user_id, appointment):
    """
    Add an appointment for a user.
    """
    appointment_doc = {"appointment": appointment}
    users_collection.update_one(
        {"user_id": user_id},
        {"$push": {"appointments": appointment_doc}},
        upsert=True
    )


def get_user_appointment(user_id):
    """
    Get the appointments for a user.
    """
    result = users_collection.find_one(
        {"user_id": user_id},
        {"_id": 0, "appointments": 1}
    )
    appointment = result["appointments"] if result else []
    return appointment


def cancel_user_appointment(user_id, appointment):
    """
    Cancel an appointment for a user.
    """
    users_collection.update_one(
        {"user_id": user_id},
        {"$pull": {"appointments": {"appointment": appointment}}}
    )
