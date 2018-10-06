class ParkingSlot:
    def __init__(self, slot_number, is_empty=True, car=None):
        self.slot_number = slot_number
        self.is_empty = is_empty
        self.car = car

    def park_car(self, car):
        self.is_empty = False
        self.car = car
        self.car.update_parking_slot_number(self.slot_number)

    def remove_car(self):
        self.is_empty = True
        self.car = None

    def does_car_with_color_exists(self, color):
        if not self.is_empty:
            if self.car.color == color:
                return True
            else:
                return False
        else:
            return False

    def get_car(self):
        return self.car

    def does_car_wit_registration_number_exists(self, registration_number):
        if not self.is_empty:
            if self.car.registration_number == registration_number:
                return True
        else:
            return False


