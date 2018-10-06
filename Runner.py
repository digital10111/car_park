import traceback
from TicketKioskHandler import TicketKioskHandler


def main():

    valid = set()
    valid.add("park")
    valid.add("leave")
    valid.add("status")
    valid.add("registration_numbers_for_cars_with_color")
    valid.add("slot_numbers_for_cars_with_color")
    valid.add("slot_number_for_registration_number")

    while True:
        create_input = raw_input()
        splits = create_input.split(" ")

        create_command = splits[0]

        if create_command != "create_parking_lot":
            print "First command has to be create_parking_lot. Please Try Again."
            continue
        else:
            if len(splits) != 2:
                print "Specify Number of slot too. Or Wrong number of args."
                continue
            ticket_kiosk_handler = TicketKioskHandler(int(splits[1]))
            break

    while True:
        try:
            inp = raw_input()
            splits = inp.split(" ")

            if splits[0] not in valid:
                print "Not a valid in put."
                if splits[0] == "create_parking_lot":
                    print "Already created."
                    continue
                continue

            if splits[0].lower() == "park":
                if len(splits) != 3:
                    print "Enter Car registration number and color to park. Or Wrong number of args."
                else:
                    ticket_kiosk_handler.park_car_with_details(splits[1], splits[2])

            if splits[0].lower() == "leave":
                if len(splits) != 2:
                    print "Please enter the slot number. Or Wrong Number of args."
                else:
                    ticket_kiosk_handler.leave(int(splits[1]))

            if splits[0].lower() == "status":
                ticket_kiosk_handler.parking_lot_status()

            if splits[0].lower() == "registration_numbers_for_cars_with_color":
                if len(splits) != 2:
                    print "Enter the car color. Or Wrong Number of args."
                ticket_kiosk_handler.get_registration_numbers_for_cars_with_color(splits[1])

            if splits[0].lower() == "slot_numbers_for_cars_with_color":
                if len(splits) != 2:
                    print "Enter the car color. Or Wrong Number of args."
                ticket_kiosk_handler.get_slot_numbers_for_cars_with_color(splits[1])

            if splits[0].lower() == "slot_number_for_registration_number":
                if len(splits) != 2:
                    print "Enter registration number. Or Wrong Number of args."
                ticket_kiosk_handler.get_slot_number_for_registration_number(splits[1])

        except Exception:
            print(traceback.format_exc())
            continue


if __name__ == '__main__':
    main()





