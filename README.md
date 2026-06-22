# Airline Reservation System

## Overview

The Airline Reservation System is a Python-based desktop application developed using CustomTkinter. It allows users to manage airline routes, book and cancel tickets, allocate seats, search booking records, generate reports, and perform data backup and restoration.

The project demonstrates the implementation of Data Structures and File Handling concepts in a real-world application.


## Features

### Route Management

* Add new airline routes
* Store Route ID, Source, Destination, Distance, and Travel Time
* Display routes in a tabular format

### Ticket Booking

* Book tickets for passengers
* Generate unique Ticket IDs
* Allocate seats automatically

### Ticket Cancellation

* Cancel booked tickets
* Update seat availability automatically
* Maintain cancellation history

### Search Booking

* Search booking details using Ticket ID
* Display passenger and route information

### Seating Arrangement

* View seat allocation visually
* Differentiate booked and available seats

### Reports

* Total Routes
* Total Bookings
* Total Cancellations
* Available Seats
* Booked Seats

### Backup & Restore

* Create backup copies of all data files
* Restore previously saved records
  

## Data Structures Used

### Graph

Used for storing and managing airline routes and connections.

### Priority Queue

Used for processing booking requests based on booking priority.

### Array (Python List)

Used for seat allocation and seat status management.

### File Handling

Used for permanent storage of:

* Routes
* Bookings
* Seat Information
* Cancellation History


## Technologies Used

* Python
* CustomTkinter
* JSON File Storage
* Object-Oriented Programming (OOP)


## Project Structure

Airline_Reservation_System/

├── main.py

├── route_manager.py

├── booking_manager.py

├── seat_manager.py

├── report_manager.py

├── backup_manager.py

├── file_manager.py

├── routes.json

├── bookings.json

├── seats.json

├── cancellations.json

├── backups/

└── README.md


## How to Run

### Install Dependencies

```bash
pip install customtkinter
```

### Run the Application

```bash
python main.py
```


## Functional Requirements Implemented

* Add Route Details
* Manage Seat Allocation
* Book Tickets
* Cancel Tickets
* Process Booking Requests
* Display Seating Arrangement
* Search Booking Details
* Generate Booking Reports
* File Handling
* Backup & Restore

---

## Developed By

Riddhima

Academic Project – Airline Reservation System
