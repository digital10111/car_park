class Car:
    def __init__(self, color, registration_number):
        self.color = color
        self.registration_number = registration_number
        self.parking_slot_number = -1

    def update_parking_slot_number(self, parking_slot_number):
        self.parking_slot_number = parking_slot_number
