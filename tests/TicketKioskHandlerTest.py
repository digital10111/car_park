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

        slot_number = self.ticket_kiosk_handler.get_slot_number_for_registration_number("Reg10")
        assert slot_number == 4

        slot_number = self.ticket_kiosk_handler.get_slot_number_for_registration_number("Reg7")
        assert slot_number == 1

        self.ticket_kiosk_handler.leave(1)

        slot_number = self.ticket_kiosk_handler.get_slot_number_for_registration_number("Reg7")
        self.assertFalse(slot_number)
        self.ticket_kiosk_handler.park_car_with_details("RegLat", "Black")

        slot_number = self.ticket_kiosk_handler.get_slot_number_for_registration_number("RegLat")
        assert slot_number == 1

    def test_should_output_the_correct_slot_numbers(self):
        self.ticket_kiosk_handler.park_car_with_details("Reg1", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg2", "Black")
        self.ticket_kiosk_handler.park_car_with_details("Reg3", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg4", "Red")
        self.ticket_kiosk_handler.park_car_with_details("Reg5", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg6", "Red")

        slot_numbers_for_cars_with_color_white = self.ticket_kiosk_handler.get_slot_numbers_for_cars_with_color("White")
        assert '1' in slot_numbers_for_cars_with_color_white
        assert '3' in slot_numbers_for_cars_with_color_white
        assert '5' in slot_numbers_for_cars_with_color_white
        assert '2' not in slot_numbers_for_cars_with_color_white
        assert '4' not in slot_numbers_for_cars_with_color_white
        assert '6' not in slot_numbers_for_cars_with_color_white

        self.ticket_kiosk_handler.leave(1)

        self.ticket_kiosk_handler.park_car_with_details("Reg1", "Black")

        slot_numbers_for_cars_with_color_white = self.ticket_kiosk_handler.get_slot_numbers_for_cars_with_color("White")

        assert '1' not in slot_numbers_for_cars_with_color_white
        assert '3' in slot_numbers_for_cars_with_color_white
        assert '5' in slot_numbers_for_cars_with_color_white
        assert '2' not in slot_numbers_for_cars_with_color_white
        assert '4' not in slot_numbers_for_cars_with_color_white
        assert '6' not in slot_numbers_for_cars_with_color_white

        slot_numbers_for_cars_with_color_black = self.ticket_kiosk_handler.get_slot_numbers_for_cars_with_color("Black")
        assert '1' in slot_numbers_for_cars_with_color_black
        assert '2' in slot_numbers_for_cars_with_color_black
        assert '3' not in slot_numbers_for_cars_with_color_black

    def test_should_output_correct_registration_number(self):
        self.ticket_kiosk_handler.park_car_with_details("Reg1", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg2", "Black")
        self.ticket_kiosk_handler.park_car_with_details("Reg3", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg4", "Red")
        self.ticket_kiosk_handler.park_car_with_details("Reg5", "White")
        self.ticket_kiosk_handler.park_car_with_details("Reg6", "Red")

        registration_numbers_for_cars_with_color_white = self.ticket_kiosk_handler.get_registration_numbers_for_cars_with_color("White")
        assert "Reg1" in registration_numbers_for_cars_with_color_white
        assert "Reg2" not in registration_numbers_for_cars_with_color_white
        assert "Reg3" in registration_numbers_for_cars_with_color_white
        assert "Reg4" not in registration_numbers_for_cars_with_color_white
        assert "Reg5" in registration_numbers_for_cars_with_color_white
        assert "Reg6" not in registration_numbers_for_cars_with_color_white

        registration_numbers_for_cars_with_color_red = self.ticket_kiosk_handler.get_registration_numbers_for_cars_with_color("Red")
        assert "Reg1" not in registration_numbers_for_cars_with_color_red
        assert "Reg2" not in registration_numbers_for_cars_with_color_red
        assert "Reg3" not in registration_numbers_for_cars_with_color_red
        assert "Reg4" in registration_numbers_for_cars_with_color_red
        assert "Reg5" not in registration_numbers_for_cars_with_color_red
        assert "Reg6" in registration_numbers_for_cars_with_color_red

        self.ticket_kiosk_handler.leave(1)
        self.ticket_kiosk_handler.leave(3)

        self.ticket_kiosk_handler.park_car_with_details("RegLat", "White")
        registration_numbers_for_cars_with_color_white = self.ticket_kiosk_handler.get_registration_numbers_for_cars_with_color("White")
        assert "Reg1" not in registration_numbers_for_cars_with_color_white
        assert "Reg2" not in registration_numbers_for_cars_with_color_white
        assert "Reg3" not in registration_numbers_for_cars_with_color_white
        assert "Reg4" not in registration_numbers_for_cars_with_color_white
        assert "Reg5" in registration_numbers_for_cars_with_color_white
        assert "Reg6" not in registration_numbers_for_cars_with_color_white
        assert "RegLat" in registration_numbers_for_cars_with_color_white


if __name__ == "__main__":
    unittest.main()
