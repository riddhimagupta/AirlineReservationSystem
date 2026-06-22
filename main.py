import customtkinter as ctk
from tkinter import ttk
from route_manager import RouteManager
from booking_manager import BookingManager
from report_manager import ReportManager
from backup_manager import BackupManager
import os

print("Current Folder:", os.getcwd())

class AirlineGUI:

    def __init__(self):

        self.app = ctk.CTk()

        self.route_manager = RouteManager()
        self.booking_manager = BookingManager()
        self.report_manager = ReportManager()
        self.backup_manager = BackupManager()

        self.app.title("Airline Reservation System")
        self.app.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self.app,
            text="✈ Airline Reservation System",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=20)

        self.sidebar = ctk.CTkFrame(
         self.app,
         width=200
        )

        self.sidebar.pack(
          side="left",
          fill="y"
        )

        self.content = ctk.CTkFrame(
           self.app
        )

        self.content.pack(
         side="right",
         fill="both",
         expand=True
        )

        self.content.pack(
    side="right",
    fill="both",
    expand=True
)

# Navigation Buttons

        self.route_btn = ctk.CTkButton(
            self.sidebar,
            text="Routes",
            command=self.show_routes
        )
        self.route_btn.pack(pady=10, padx=10)

        self.booking_btn = ctk.CTkButton(
            self.sidebar,
            text="Book Ticket",
            command=self.show_booking
        )
        self.booking_btn.pack(pady=10, padx=10)

        self.cancel_btn = ctk.CTkButton(
            self.sidebar,
            text="Cancel Ticket",
            command=self.show_cancel
        )
        self.cancel_btn.pack(pady=10, padx=10)

        self.report_btn = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            command=self.show_report
        )
        self.report_btn.pack(pady=10, padx=10)

        self.search_btn = ctk.CTkButton(
        self.sidebar,
        text="Search Booking",
        command=self.show_search
        )

        self.search_btn.pack(pady=10, padx=10)

        self.seat_btn = ctk.CTkButton(
        self.sidebar,
        text="Seating Arrangement",
        command=self.show_seats
        )
        
        self.seat_btn.pack(pady=10, padx=10)

        self.backup_btn = ctk.CTkButton(
        self.sidebar,
        text="Backup Data",
        command=self.create_backup
        )
        
        self.backup_btn.pack(
            pady=10,
            padx=10
        )

        self.restore_btn = ctk.CTkButton(
        self.sidebar,
        text="Restore Data",
        command=self.restore_data
        )
        
        self.restore_btn.pack(
            pady=10,
            padx=10
        )

    def clear_content(self):

      for widget in self.content.winfo_children():
         widget.destroy()

    def show_routes(self):

      self.clear_content()

      title = ctk.CTkLabel(
        self.content,
        text="Route Management",
        font=("Arial", 24, "bold")
      )

      title.pack(pady=20)

    # Route ID

      self.route_id_entry = ctk.CTkEntry(
        self.content,
        placeholder_text="Route ID"
      )

      self.route_id_entry.pack(pady=10)

    # Source

      self.source_entry = ctk.CTkEntry(
        self.content,
        placeholder_text="Source"
      )

      self.source_entry.pack(pady=10)

    # Destination

      self.destination_entry = ctk.CTkEntry(
        self.content,
        placeholder_text="Destination"
      )

      self.destination_entry.pack(pady=10)

    # Distance

      self.distance_entry = ctk.CTkEntry(
        self.content,
        placeholder_text="Distance"
      )

      self.distance_entry.pack(pady=10)

    # Travel Time

      self.time_entry = ctk.CTkEntry(
        self.content,
        placeholder_text="Travel Time"
      )

      self.time_entry.pack(pady=10)

    # Add Route Button

      add_btn = ctk.CTkButton(
        self.content,
        text="Add Route",
        command=self.add_route
      )

      add_btn.pack(pady=20)

      self.routes_table = ttk.Treeview(
    self.content,
    columns=(
        "Route ID",
        "Source",
        "Destination",
        "Distance",
        "Travel Time"
    ),
    show="headings",
    height=10
)

      self.routes_table.heading(
          "Route ID",
          text="Route ID"
      )

      self.routes_table.heading(
          "Source",
          text="Source"
      )

      self.routes_table.heading(
          "Destination",
          text="Destination"
      )

      self.routes_table.heading(
          "Distance",
          text="Distance"
      )

      self.routes_table.heading(
          "Travel Time",
          text="Travel Time"
      )

      self.routes_table.pack(
          pady=20,
          fill="x"
      )

      self.load_routes()

    def add_route(self):

      #print("Button Clicked")

      route_id = int(
        self.route_id_entry.get()
      )

      source = self.source_entry.get()

      destination = self.destination_entry.get()

      distance = int(
        self.distance_entry.get()
      )

      travel_time = self.time_entry.get()

      self.route_manager.add_route(
        route_id,
        source,
        destination,
        distance,
        travel_time
      )

      print("Route Added")

      self.load_routes()

      self.route_id_entry.delete(0, "end")
      self.source_entry.delete(0, "end")
      self.destination_entry.delete(0, "end")
      self.distance_entry.delete(0, "end")
      self.time_entry.delete(0, "end")

    def load_routes(self):

        for row in self.routes_table.get_children():
            self.routes_table.delete(row)

        routes = self.route_manager.display_routes()

        for route in routes:

            self.routes_table.insert(
                "",
                "end",
                values=(
                    route["route_id"],
                    route["source"],
                    route["destination"],
                    route["distance"],
                    route["travel_time"]
                )
            )

    def show_booking(self):

        self.clear_content()

        title = ctk.CTkLabel(
            self.content,
            text="Book Ticket",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

    # Passenger Name

        self.passenger_entry = ctk.CTkEntry(
            self.content,
            placeholder_text="Passenger Name"
        )

        self.passenger_entry.pack(pady=10)

    # Priority

        self.priority_entry = ctk.CTkEntry(
            self.content,
            placeholder_text="Priority (1 = Highest)"
        )

        self.priority_entry.pack(pady=10)

    # Route Selection

        routes = self.route_manager.display_routes()

        route_list = []

        for route in routes:

            route_list.append(
                f"{route['route_id']} | "
                f"{route['source']} -> "
                f"{route['destination']}"
            )

        self.route_menu = ctk.CTkOptionMenu(
            self.content,
            values=route_list
        )

        self.route_menu.pack(pady=10)

    # Book Button

        book_btn = ctk.CTkButton(
            self.content,
            text="Book Ticket",
            command=self.book_ticket
        )

        book_btn.pack(pady=20)

    # Result

        self.booking_result = ctk.CTkLabel(
            self.content,
            text=""
        )

        self.booking_result.pack(pady=10)

    def show_search(self):

        self.clear_content()
    
        title = ctk.CTkLabel(
            self.content,
            text="Search Booking",
            font=("Arial", 24, "bold")
        )
    
        title.pack(pady=20)
    
        self.ticket_search_entry = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Ticket ID"
        )
    
        self.ticket_search_entry.pack(pady=10)
    
        search_btn = ctk.CTkButton(
            self.content,
            text="Search",
            command=self.search_booking
        )
    
        search_btn.pack(pady=10)
    
        self.search_result = ctk.CTkTextbox(
            self.content,
            width=500,
            height=150
        )
    
        self.search_result.pack(pady=20)

    def book_ticket(self):

        passenger = self.passenger_entry.get()

        priority = int(
            self.priority_entry.get()
        )

        selected_route = self.route_menu.get()
    
        route_id = int(
            selected_route.split("|")[0].strip()
        )
    
        routes = self.route_manager.display_routes()
    
        route_found = None
    
        for route in routes:

            if route["route_id"] == route_id:
                route_found = route
                break

        self.booking_manager.add_booking_request(
            priority,
            passenger
        )
    
        booking = self.booking_manager.process_booking(
            route_found["route_id"],
            route_found["source"],
            route_found["destination"]
        )
    
        self.booking_result.configure(
            text=f"Ticket Booked: "
                 f"{booking['ticket_id']} | "
                 f"Seat {booking['seat_no']}"
        )

    def show_cancel(self):

        self.clear_content()
    
        title = ctk.CTkLabel(
            self.content,
            text="Cancel Ticket",
            font=("Arial", 24, "bold")
        )
    
        title.pack(pady=20)
    
        self.cancel_ticket_entry = ctk.CTkEntry(
            self.content,
            placeholder_text="Enter Ticket ID"
        )
    
        self.cancel_ticket_entry.pack(pady=10)
    
        cancel_btn = ctk.CTkButton(
            self.content,
            text="Cancel Ticket",
            command=self.cancel_ticket
        )
    
        cancel_btn.pack(pady=20)
    
        self.cancel_result = ctk.CTkLabel(
            self.content,
            text=""
        )
    
        self.cancel_result.pack(pady=10)

    def cancel_ticket(self):

        ticket_id = self.cancel_ticket_entry.get()
    
        success = self.booking_manager.cancel_booking(
            ticket_id
        )
    
        if success:
    
            self.cancel_result.configure(
                text="Ticket Cancelled Successfully"
            )
    
        else:
    
            self.cancel_result.configure(
                text="Ticket Not Found"
            )

    def show_report(self):

        self.clear_content()
    
        title = ctk.CTkLabel(
            self.content,
            text="Booking Report",
            font=("Arial", 24, "bold")
        )
    
        title.pack(pady=20)
    
        report = self.report_manager.generate_report()
    
        report_text = f"""
    Total Routes: {report['total_routes']}
    
    Total Bookings: {report['total_bookings']}
    
    Total Cancellations: {report['total_cancellations']}
    
    Available Seats: {report['available_seats']}
    
    Booked Seats: {report['booked_seats']}
    """
    
        report_label = ctk.CTkLabel(
            self.content,
            text=report_text,
            justify="left",
            font=("Arial", 18)
        )
    
        report_label.pack(pady=20)

    def search_booking(self):

        ticket_id = self.ticket_search_entry.get()
    
        booking = self.booking_manager.search_booking(
            ticket_id
        )
    
        self.search_result.delete(
            "1.0",
            "end"
        )
    
        if booking:
    
            self.search_result.insert(
                "end",
                f"Ticket ID: {booking['ticket_id']}\n\n"
                f"Passenger: {booking['passenger_name']}\n\n"
                f"Seat No: {booking['seat_no']}\n\n"
                f"Route: {booking['source']} -> "
                f"{booking['destination']}"
            )
    
        else:
    
            self.search_result.insert(
                "end",
                "Booking Not Found"
            )

    def show_seats(self):
        self.clear_content()
    
        title = ctk.CTkLabel(
            self.content,
            text="Seating Arrangement",
            font=("Arial", 24, "bold")
        )
    
        title.pack(pady=20)

        legend_frame = ctk.CTkFrame(self.content)
        legend_frame.pack(pady=10)
        
        green_label = ctk.CTkLabel(
            legend_frame,
            text="Available",
            fg_color="green",
            corner_radius=5
        )
        
        green_label.pack(
            side="left",
            padx=10
        )
        
        red_label = ctk.CTkLabel(
            legend_frame,
            text="Booked",
            fg_color="red",
            corner_radius=5
        )
        
        red_label.pack(
            side="left",
            padx=10
        )

        # green_label = ctk.CTkLabel(
        # self.content,
        # text="Available",
        # fg_color="green",
        # corner_radius=5
        # )
        
        # green_label.pack(pady=5)
        
        # red_label = ctk.CTkLabel(
        #     self.content,
        #     text="Booked",
        #     fg_color="red",
        #     corner_radius=5
        # )
        
        # red_label.pack(pady=5)
            
        seats = self.booking_manager.seat_manager.display_seats()
    
        seats_frame = ctk.CTkFrame(self.content)
        seats_frame.pack(pady=20)
    
        for i, seat in enumerate(seats):
    
            if seat == "Booked":
                color = "red"
            else:
                color = "green"
    
            seat_btn = ctk.CTkButton(
                seats_frame,
                text=f"{i+1}",
                width=50,
                fg_color=color
            )
    
            row = i // 5
            col = i % 5
    
            seat_btn.grid(
                row=row,
                column=col,
                padx=5,
                pady=5
            )

    def create_backup(self):
        self.backup_manager.create_backup()
    
        self.clear_content()
    
        label = ctk.CTkLabel(
            self.content,
            text="Backup Created Successfully",
            font=("Arial",20)
        )
    
        label.pack(pady=50)

    def restore_data(self):

        self.backup_manager.restore_backup()
    
        self.clear_content()
    
        label = ctk.CTkLabel(
            self.content,
            text="Data Restored Successfully",
            font=("Arial",20)
        )
    
        label.pack(pady=50)

    def run(self):
                self.app.mainloop()


gui = AirlineGUI()
gui.run()

# import customtkinter as ctk

# # App Settings
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# # Main Window
# app = ctk.CTk()
# app.title("Airline Reservation System")
# app.geometry("1000x600")

# # Title
# title_label = ctk.CTkLabel(
#     app,
#     text="✈ Airline Reservation System",
#     font=("Arial", 28, "bold")
# )
# title_label.pack(pady=20)

# # Button Frame
# button_frame = ctk.CTkFrame(app)
# button_frame.pack(pady=20)

# # Buttons
# route_btn = ctk.CTkButton(
#     button_frame,
#     text="Add Route",
#     width=200
# )
# route_btn.pack(pady=10)

# book_btn = ctk.CTkButton(
#     button_frame,
#     text="Book Ticket",
#     width=200
# )
# book_btn.pack(pady=10)

# cancel_btn = ctk.CTkButton(
#     button_frame,
#     text="Cancel Ticket",
#     width=200
# )
# cancel_btn.pack(pady=10)

# search_btn = ctk.CTkButton(
#     button_frame,
#     text="Search Booking",
#     width=200
# )
# search_btn.pack(pady=10)

# report_btn = ctk.CTkButton(
#     button_frame,
#     text="Generate Report",
#     width=200
# )
# report_btn.pack(pady=10)

# backup_btn = ctk.CTkButton(
#     button_frame,
#     text="Backup Data",
#     width=200
# )
# backup_btn.pack(pady=10)

# restore_btn = ctk.CTkButton(
#     button_frame,
#     text="Restore Data",
#     width=200
# )
# restore_btn.pack(pady=10)

# app.mainloop()
