import unittest
from TicketKioskHandler import TicketKioskHandler


class TicketKioskHandlerTest(unittest.TestCase):
    def setUp(self):
        self.ticket_kiosk_handler = TicketKioskHandler(6)

    def test_should_assign_correct_slot_number(self):
        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg1", "White")
        assert slot_number == 1

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg2", "White")
        assert slot_number == 2

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg3", "White")
        assert slot_number == 3

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg4", "White")
        assert slot_number == 4

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg5", "White")
        assert slot_number == 5

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg6", "White")
        assert slot_number == 6

        success = self.ticket_kiosk_handler.leave(1)
        assert success

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg7", "White")
        assert slot_number == 1

        success = self.ticket_kiosk_handler.leave(3)
        assert success

        success = self.ticket_kiosk_handler.leave(4)
        assert success

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg8", "White")
        assert slot_number == 3

        success = self.ticket_kiosk_handler.leave(2)
        assert success

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg9", "White")
        assert slot_number == 2

        slot_number = self.ticket_kiosk_handler.park_car_with_details("Reg10", "White")
        assert slot_number == 4

    def test_should_output_the_correct_slot_numbers(self):
        self.ticket_kiosk_handler.park_car_with_details("Reg1", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg2", "Black")
        self.ticket_kiosk_handler.park_car_with_details("Reg3", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg4", "Red")
        self.ticket_kiosk_handler.park_car_with_details("Reg5", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg6", "Red")

        self.ticket_kiosk_handler





if __name__ == "__main__":
    unittest.main()