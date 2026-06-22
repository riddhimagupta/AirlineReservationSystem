from file_manager import FileManager

class SeatManager:

    def __init__(self):
        self.seats = FileManager.load_data("seats.json")

        if not self.seats:
            self.seats = ["Available"] * 30
            FileManager.save_data("seats.json", self.seats)

    def display_seats(self):
        return self.seats

    def book_seat(self):
        for i in range(len(self.seats)):
            if self.seats[i] == "Available":
                self.seats[i] = "Booked"

                #self.seats = FileManager.load_data("seats.json")

                FileManager.save_data(
                    "seats.json",
                    self.seats
                )

                return i + 1

        return None

    def cancel_seat(self, seat_no):
        self.seats[seat_no - 1] = "Available"

        FileManager.save_data(
            "seats.json",
            self.seats
        )
