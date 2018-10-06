from entities.Car import Car
from entities.TicketKiosk import TicketKiosk


class TicketKioskHandler:
    def __init__(self, number_of_parking_slots):
        self.ticket_kiosk = TicketKiosk(number_of_parking_slots=number_of_parking_slots)
        self.number_of_parking_slots = number_of_parking_slots

    def park_car_with_details(self, registration_number, color):
        if not registration_number:
            raise RuntimeError("No Registration number provided.")
        if len(registration_number) == 0:
            raise RuntimeError("No Registration number provided.")

        if not color:
            raise RuntimeError("No color provided.")
        if len(color) == 0:
            raise RuntimeError("No color provided.")

        car = Car(color=color, registration_number=registration_number)
        slot_index = self.ticket_kiosk.get_nearest_slot_index()
        if not slot_index:
            print "Sorry, Parking Lot is Full."
        else:
            self.ticket_kiosk.assign_parking_slot_to_car(car, slot_index)

    def leave(self, slot_number):
        if slot_number < 1 or slot_number > self.number_of_parking_slots:
            print "No such Parking Lot."
        success = self.ticket_kiosk.leave_parking_slot(parking_slot_number=slot_number)
        if not success:
            print "Parking Slot is already empty."
        else:
            print "Parking Slot " + str(slot_number) + " is empty."

    def parking_lot_status(self):
        self.ticket_kiosk.status()

    def get_slot_number_for_registration_number(self, registration_number):
        is_car_there, parking_slot_number = self.ticket_kiosk.get_slot_number_for_registration_number(registration_number)
        if is_car_there:
            print parking_slot_number
        else:
            print "No such car."

    def get_slot_numbers_for_cars_with_color(self, color):
        are_there_cars, slot_numbers_for_cars_with_color = self.ticket_kiosk.get_slot_numbers_for_cars_with_color(color)
        if are_there_cars:
            print ",".join(slot_numbers_for_cars_with_color)
        else:
            print "No cars with this color."

    def get_registration_numbers_for_cars_with_color(self, color):
        are_there_cars, registration_numbers_for_cars_with_color = self.ticket_kiosk.get_registration_numbers_for_cars_with_color(color)
        if are_there_cars:
            print ",".join(registration_numbers_for_cars_with_color)
        else:
            print "No cars with this color."





