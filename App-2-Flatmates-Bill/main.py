###IMPORTS###
from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about a bill.
    """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatemate who lives in the same flat and pays share of the bill.
    """
    
    def __init__(self, name, days_in_house):
        self.name = name,
        self.days_in_house = days_in_house
        
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        total = bill.amount * weight
        return total

class PdfGenerator:
    
    """
    Generating pdf each month of the bill. Includes the amount of the bill and flatmates names.
    """
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        
        # Add Image
        pdf.image("App-2-Flatmates-Bill\house.png", w=30, h=30)
        
        # Formating PDF
        pdf.set_font(family="Times", size =24, style="B")
        pdf.cell(w = 0, h = 80, txt = "Flatmates Bill", border=0, align= "C", ln = 1)
        
        # Insert period
        pdf.set_font(family="Times", size =20, style="B")
        pdf.cell(w=100,h=40, txt = "Period:", border=0)
        pdf.cell(w=150,h=40, txt = bill.period, border=0, ln=1)
        
        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size =14)
        pdf.cell(w=100,h=25, txt =  "".join(flatmate2.name), border=0)
        pdf.cell(w=150,h=25, txt =  str(round(flatmate2.pays(bill, flatmate),2)), border=0, ln=1)
        pdf.cell(w=100,h=25, txt =  "".join(flatmate.name), border=0)
        pdf.cell(w=150,h=25, txt =  str(round(flatmate.pays(bill, flatmate2),2)), border=0, ln=1)
            
        # Naming a file and save it as a pdf
        pdf.output(self.filename + "_" + bill.period + ".pdf")
        
        # Open PDF file automatically
        webbrowser.open(self.filename  + "_" + bill.period + ".pdf")
    
#Inputs    
bill_amount = int(input("Hello user, enter the bill amount: "))
user_period = input("What is the bill period? E.g. January 2021 ")
person = input("What is your name? ")
person2 = input("What is your flatmate's name? ")
stay_in_house1 = int(input(f"How many days did {person} stay in the house during the bill period? "))
stay_in_house2 = int(input(f"How many days did {person2} stay in the house during the bill period? "))
gived_filename = input("Give a filename: ")

the_bill = Bill(amount= bill_amount, period= user_period)
flat_mate = Flatmate(name = person, days_in_house = stay_in_house1)
flat_mate2 = Flatmate(name = person2, days_in_house = stay_in_house2)

print("flat_mate pays:",flat_mate.pays(bill = the_bill, flatmate2 = flat_mate2))
print("flat_mate2 pays:", flat_mate2.pays(bill = the_bill, flatmate2 = flat_mate))


pdf_generator = PdfGenerator(filename = gived_filename)
pdf_generator.generate(flatmate = flat_mate, flatmate2 = flat_mate2, bill = the_bill)
