from file_manager import FileManager

class ReportManager:

    def generate_report(self):

        routes = FileManager.load_data(
            "routes.json"
        )

        bookings = FileManager.load_data(
            "bookings.json"
        )

        cancellations = FileManager.load_data(
            "cancellations.json"
        )

        seats = FileManager.load_data(
            "seats.json"
        )

        available_seats = seats.count(
            "Available"
        )

        booked_seats = seats.count(
            "Booked"
        )

        report = {
            "total_routes": len(routes),
            "total_bookings": len(bookings),
            "total_cancellations": len(cancellations),
            "available_seats": available_seats,
            "booked_seats": booked_seats
        }

        return report