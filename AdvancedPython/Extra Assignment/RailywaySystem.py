import csv

# Define the fare rules based on distance, class, etc.
# For simplicity, let's assume a fixed fare per seat.
def calculate_fare(train_id, num_tickets):
    # Replace this with actual fare calculation logic based on train_id and distance if needed.
    # For now, we assume a fixed fare of 1000 per seat.
    fixed_fare = 1000
    return fixed_fare * num_tickets

def load_train_data(filename):
    trains = {}
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            train_id = row["Train ID"]
            train_name = row["TrainName"]
            source_station = row["SourceStation"]
            destination_station = row["DestinationStation"]
            total_seats = int(row["TotalSeats"])
            fare_per_seat = float(row["fareperseat"])

            trains[train_id] = {
                "TrainName": train_name,
                "SourceStation": source_station,
                "DestinationStation": destination_station,
                "TotalSeats": total_seats,
                "FarePerSeat": fare_per_seat
            }
    return trains

def load_passenger_data(filename):
    passengers = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            passenger_name = row["Passenger Name"]
            train_id = row["TrainID"]
            num_tickets = int(row["Number of Tickets"])

            passengers.append({
                "PassengerName": passenger_name,
                "TrainID": train_id,
                "NumTickets": num_tickets
            })
    return passengers

def check_seat_availability(train_id, num_tickets, trains):
    if train_id not in trains:
        return False, "Invalid Train ID"

    available_seats = trains[train_id]["TotalSeats"]
    if num_tickets > available_seats:
        return False, "Insufficient Seats"

    return True, "Seats Available"

def update_seat_availability(train_id, num_tickets, trains):
    trains[train_id]["TotalSeats"] -= num_tickets

def generate_report_1(trains):
    print("Report 1 - Details of all Trains:")
    for train_id, train_info in trains.items():
        print(f"Train ID: {train_id}")
        print(f"Train Name: {train_info['TrainName']}")
        print(f"Source Station: {train_info['SourceStation']}")
        print(f"Destination Station: {train_info['DestinationStation']}")
        print(f"Total Seats Available: {train_info['TotalSeats']}")
        print("")

def generate_report_2(trains):
    print("Report 2 - Revenue earned from each Train:")
    for train_id, train_info in trains.items():
        total_seats = train_info['TotalSeats']
        seats_booked = total_seats - train_info['TotalSeats']
        fare_per_seat = train_info['FarePerSeat']
        total_fare = seats_booked * fare_per_seat

        print(f"Train ID: {train_id}")
        print(f"Train Name: {train_info['TrainName']}")
        print(f"Total Seats Booked: {seats_booked}")
        print(f"Total Fare Earned: {total_fare}")
        print("")

def main():
    # Load train data from "trains.csv"
    trains = load_train_data("trains.csv")

    # Load passenger data from "passengers.csv"
    passengers = load_passenger_data("passengers.csv")

    # Process passenger bookings
    for passenger in passengers:
        passenger_name = passenger["PassengerName"]
        train_id = passenger["TrainID"]
        num_tickets = passenger["NumTickets"]

        # Check seat availability
        is_available, message = check_seat_availability(train_id, num_tickets, trains)

        if is_available:
            # Calculate fare for the booking
            fare = calculate_fare(train_id, num_tickets)

            # Confirm booking and update seat availability
            update_seat_availability(train_id, num_tickets, trains)

            print(f"Booking confirmed for {passenger_name} on Train ID {train_id} for {num_tickets} tickets.")
            print(f"Total Fare: {fare}")
            print("")

        else:
            print(f"Booking not confirmed for {passenger_name} on Train ID {train_id}: {message}")
            print("")

    # Generate reports
    generate_report_1(trains)
    generate_report_2(trains)

if __name__ == "__main__":
    main()
