'''
class Train

methods:
book a ticket
show status(no of seats)
show fare
cancel Ticket

5 seats 
[1, 2, 3, 4, 5]
'''

class Train:

    def __init__(self, name, noOfSeats, fare):
        self.name = name
        self.noOfSeats = noOfSeats
        self.fare = fare
        self.nSeats = list(range(1, noOfSeats + 1))

    def showDetails(self):
        print(f"Train Name: {self.name}")
        print(f"Train fare is: {self.fare}")
        print(f"Total seats is train :{self.noOfSeats}")
        print(f"Seats available: {len(self.nSeats)}")

    def showSeatsAvailable(self):
        print(f"Total no of seats available: {len(self.nSeats)}")
        print(f"Seat nos available: {self.nSeats}")

    def bookTicket(self, noOfTickets):
        if noOfTickets <= len(self.nSeats):
            for _ in range(noOfTickets):
                print(f"seat no booked: {self.nSeats.pop()}")
            print(f"Please pay: {noOfTickets * self.fare}")
        else:
            print(f"{noOfTickets} seats are not available")
            print(f"available seats: {len(self.nSeats)}")

    def cancelTicket(self, ticketNum):
        if ticketNum < 0 or ticketNum > self.noOfSeats:
            print("Please enter valid ticket number")
        else:
            if ticketNum not in self.nSeats:
                self.nSeats.append(ticketNum)
                print(f"{ticketNum} is cancelled")
            else:
                print("enter correct ticket num")

obj = Train("Rajdhani Express", 5 , 50)

# obj.showDetails()
# obj.showSeatsAvailable()
obj.bookTicket(3)
# obj.showDetails()
obj.cancelTicket(5)
obj.showSeatsAvailable()

