### IMPORTS ###
import random
import string
import sqlite3
from fpdf import FPDF

"""Cinema ticket booker program"""

class User:
    """Handling user data when buying a cinema ticket"""
    def __init__(self, name):
        self.name = name
    
        
    def buy(self, seat, card):
        """Buys a ticket if the card is valid"""
        if seat.is_available():
            if card.validate(price = seat.get_price()):
                seat.occupy()
                ticket = Ticket(user = self,
                                price = seat.get_price(),
                                seat_num = seat_id)
                ticket.to_pdf()
                return "Purchase successful!"
            else:
                return "There was a problem with a card. Please try again."
        else:
            return "Seat is taken!"

class Seat:
    """Handling seat data such as id's and price"""
    # cinema database
    database = r"App-11-Cinema-Ticket-Booking/databases/cinema.db"
    
    def __init__(self, seat_id):
        self.seat_id = seat_id
        
    def get_price(self):
        """Get the price pf a certain seat"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?        
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        
    
        print(price)
        
        return price
    
    def is_available(self):
        """Check in the database if the seat is available or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id]) # <- replace ?
        result = cursor.fetchall()[0][0]
        
        if result == 0:
            return True
        else: 
            return False
    
    def occupy(self):
        """Change value of taken in the database from 0 to 1 if Seat is available"""
        
        if self.is_available():
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute("""
            UPDATE "Seat" SET "Taken"=? WHERE "seat_id" = ?
            """, [0, self.seat_id])
            connection.commit()
            connection.close()
            

class Card:
    """handling credit card and validating the card."""
    
    # banking database
    database = r"App-11-Cinema-Ticket-Booking/databases/banking.db"
    
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price):
        """Checks if card is valid and has balance
        and subtracts price from balance"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [self.number, self.cvc])
        result = cursor.fetchall()
        
        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "Balance" =? WHERE "number"=? and "cvc"=? 
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
        

class Ticket:
    """Represents a cinema ticket purchased by a user"""
    
    def __init__(self, user, price, seat_num):
        self.id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat_num = seat_num
        
        
    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        
   
        # Formating PDF
        pdf.set_font(family="Times", size =24, style="B")
        pdf.cell(w = 0, h = 80, txt = "Digital Cinema Ticket", border=1, align= "C", ln = 1)
        
        # Formating  ticket to purchaser
        pdf.set_font(family="Times", size =14, style="B")
        pdf.cell(w=100,h=25, txt = "Name:", border=1)
        pdf.set_font(family="Times", size = 12, style="")
        pdf.cell(w=0,h=25, txt = self.user.name , border=1, ln=1)
        pdf.cell(w=0,h=5, txt = "", border=0, ln=1)
        
        # Ticekt ID part
        pdf.set_font(family="Times", size =14, style="B")
        pdf.cell(w=100, h=25, txt = "Ticket ID" , border=1)
        pdf.set_font(family="Times", size =14, style="")
        pdf.cell(w=0, h=25, txt= self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)
        
        # Seat number
        pdf.set_font(family="Times", size =14, style="B")
        pdf.cell(w=100, h=25, txt = "Seat Number" , border=1)
        pdf.set_font(family="Times", size =14, style="")
        pdf.cell(w=0, h=25, txt=  str(self.seat_num), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)
        
        # PDF output
        pdf.output("CinemaTicket.pdf", 'f')
        

if __name__ == "__main__":
    # Inputs from user input (CLI)
    name =  "John Smith"   #input("Your full name: ")
    seat_id =   "A1"   #input("Preferred seat number: ")
    card_type = "Visa" #input("Your card type: ")
    card_num = "23456789" #input("Your card number: ")
    card_cvc = "234" #input("Your card cvc: ")     
    card_holder = "John Smith"  #input("Card holder name: ") 
    
    
    # Class instances
    
    user = User(name=name)
    seat = Seat(seat_id = seat_id)
    card = Card(type = card_type, number = card_num, cvc = card_cvc, holder = card_holder)
    print(user.buy(seat = seat, card = card))
    