from ParkingSlot import ParkingSlot


class TicketKiosk:
    def __init__(self, number_of_parking_slots):
        self.number_of_parking_slots = number_of_parking_slots
        self.parking_slots = self.init_parking_slots()

    def init_parking_slots(self):
        parking_slots = list()
        for i in range(self.number_of_parking_slots):
            parking_slots.append(ParkingSlot(slot_number=i+1))
        print "Created a parking lot with " + str(self.number_of_parking_slots) + " slots."
        return parking_slots

    def get_nearest_slot_index_and_number(self):
        for index, parking_slot in enumerate(self.parking_slots):
            if parking_slot.is_empty:
                return index, parking_slot.slot_number

    def assign_parking_slot_to_car(self, car, slot_index):
        self.parking_slots[slot_index].park_car(car)

    def get_slot_number_for_registration_number(self, registration_number):
        for parking_slot in self.parking_slots:
            if not parking_slot.is_empty:
                if parking_slot.does_car_wit_registration_number_exists(registration_number):
                    return True, parking_slot.slot_number
        return False, -1

    def get_slot_numbers_for_cars_with_color(self, color):
        slot_numbers_for_cars_with_color = []
        for parking_slot in self.parking_slots:
            if not parking_slot.is_empty:
                if parking_slot.does_car_with_color_exists(color):
                    slot_numbers_for_cars_with_color.append(parking_slot.slot_number)
        if len(slot_numbers_for_cars_with_color) > 0:
            return True, slot_numbers_for_cars_with_color
        else:
            return False, slot_numbers_for_cars_with_color

    def leave_parking_slot(self, parking_slot_number):
        self.parking_slots[parking_slot_number-1].remove_car()

    def status(self):
        print "No" + '\t' + "Registration" + '\t' + "Slot No." + '\t' + "Color" + '\n'
        for i, parking_slot in enumerate(self.parking_slots):
            if not parking_slot.is_empty:
                print str(i+1) + '\t' + parking_slot.get_car().registration_number + '\t' + parking_slot.slot_number + '\t' + parking_slot.get_car().color + '\n'
