import random


# dummy api that returns a random number
# if reservation is available
def check_appointment_api(datetime):
    return random.choice(["Avaliable", "N/A"])


def book_appointment_api(datetime):
    pass


def cancel_appointment_api(datetime):
    pass
