import random

class RailwaySystem:
    def __init__(self, total_seats=50):
        # Using a dictionary to store bookings: {booking_id: {"name": name, "age": age, "seat": seat_no}}
        self.total_seats = total_seats [cite: 4]
        self.available_seats = list(range(1, total_seats + 1)) [cite: 5]
        self.bookings = {} [cite: 4]

    def check_availability(self):
        print(f"\n--- Seat Availability ---")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {len(self.available_seats)}")
        print(f"Seats vacant: {self.available_seats}") [cite: 4]

    

    def view_ticket(self):
        print("\n--- View Ticket ---")
        try:
            bid = int(input("Enter your Booking ID: ")) [cite: 4]
            if bid in self.bookings:
                details = self.bookings[bid]
                print(f"\nTicket Found:")
                print(f"Booking ID: {bid}")
                print(f"Name: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Seat Number: {details['seat']}") [cite: 4]
            else:
                print("No ticket found with that ID.")
        except ValueError:
            print("Invalid ID format.")

    def cancel_ticket(self):
        print("\n--- Cancel Ticket ---")
        try:
            bid = int(input("Enter Booking ID to cancel: "))
            if bid in self.bookings:
                # Remove booking and add the seat back to available list
                cancelled_seat = self.bookings[bid]['seat']
                del self.bookings[bid] [cite: 5]
                self.available_seats.append(cancelled_seat)
                self.available_seats.sort() [cite: 5]
                print(f"Ticket ID {bid} cancelled successfully. Seat {cancelled_seat} is now free.")
            else:
                print("Booking ID not found.")
        except ValueError:
            print("Invalid ID format.")

def main():
    system = RailwaySystem()
    
    while True:
        print("\n--- RAILWAY RESERVATION SYSTEM ---") [cite: 4]
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit") [cite: 4]
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            system.check_availability()
        elif choice == '2':
            system.book_ticket()
        elif choice == '3':
            system.view_ticket()
        elif choice == '4':
            system.cancel_ticket()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()