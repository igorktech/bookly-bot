from services.db_manager import (
    add_user_appointment,
    get_user_appointment,
    cancel_user_appointment
)

from appointment_api import (
    book_appointment_api,
    check_appointment_api,
    cancel_appointment_api
)


class AppointmentManager:
    def __init__(self):
        pass

    def book_appointment(self, user_id, datetime):
        book_appointment_api(datetime)
        add_user_appointment(user_id, datetime)

    def cancel_appointment(self, user_id, datetime):
        cancel_appointment_api(datetime)
        cancel_user_appointment(user_id, datetime)

    def get_appointment(self, user_id):
        return get_user_appointment(user_id)

    def check_availability(self, datetime):
        return check_appointment_api(datetime)
