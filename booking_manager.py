import heapq
import random
from datetime import datetime

from file_manager import FileManager
from seat_manager import SeatManager


class BookingManager:

    def __init__(self):

        self.bookings = FileManager.load_data(
            "bookings.json"
        )

        self.booking_queue = []

        self.seat_manager = SeatManager()

    # Add booking request to priority queue
    def add_booking_request(self,
                            priority,
                            passenger_name):

        heapq.heappush(
            self.booking_queue,
            (priority, passenger_name)
        )

    # Process next request
    def process_booking(
        self,
        route_id,
        source,
        destination):

        if not self.booking_queue:
            return "No Booking Requests"

        priority, passenger_name = heapq.heappop(
            self.booking_queue
        )

        seat_no = self.seat_manager.book_seat()

        if seat_no is None:
            return "No Seats Available"

        ticket_id = "T" + str(
            random.randint(1000, 9999)
        )

        booking = {
    "ticket_id": ticket_id,
    "passenger_name": passenger_name,
    "seat_no": seat_no,
    "priority": priority,
    "route_id": route_id,
    "source": source,
    "destination": destination,
    "booking_time":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
}

        self.bookings.append(booking)

        FileManager.save_data(
            "bookings.json",
            self.bookings
        )

        return booking

    # Display all bookings
    def display_bookings(self):
        return self.bookings

    # Search booking
    def search_booking(self, ticket_id):

        for booking in self.bookings:

            if booking["ticket_id"] == ticket_id:
                return booking

        return None

    # Cancel booking
    def cancel_booking(self, ticket_id):

        bookings = FileManager.load_data(
            "bookings.json"
        )
    
        cancellations = FileManager.load_data(
            "cancellations.json"
        )
    
        for booking in bookings:
    
            if booking["ticket_id"] == ticket_id:
    
                self.seat_manager.cancel_seat(
                    booking["seat_no"]
                )
    
                cancellations.append(booking)
    
                bookings.remove(booking)
    
                FileManager.save_data(
                    "bookings.json",
                    bookings
                )
    
                FileManager.save_data(
                    "cancellations.json",
                    cancellations
                )
    
                return True
    
        return False

    # Generate report
    def generate_report(self):

        total_bookings = len(self.bookings)

        cancellations = FileManager.load_data(
            "cancellations.json"
        )

        total_cancellations = len(
            cancellations
        )

        seats = self.seat_manager.display_seats()

        available = seats.count("Available")

        booked = seats.count("Booked")

        cancelled = seats.count("Cancelled")

        return {
            "total_bookings": total_bookings,
            "total_cancellations": total_cancellations,
            "available_seats": available,
            "booked_seats": booked,
            "cancelled_seats": cancelled
        }

    def search_booking(self, ticket_id):

        bookings = FileManager.load_data(
            "bookings.json"
        )
    
        for booking in bookings:
    
            if booking["ticket_id"] == ticket_id:
                return booking
    
        return None