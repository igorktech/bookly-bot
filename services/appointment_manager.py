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

    def book_appointment(self, user_id, date):
        available = check_appointment_api(date)
        if available:
            book_appointment_api(date)
            add_user_appointment(user_id, date)

    def cancel_appointment(self, user_id):
        appointment = get_user_appointment(user_id)
        if appointment:
            cancel_appointment_api(appointment)
            cancel_user_appointment(user_id)

    def get_appointment(self, user_id):
        return get_user_appointment(user_id)

    def check_availability(self, date):
        return check_appointment_api(date)
