###IMPORTS###
from fpdf import FPDF

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
        
        # Formating PDF
        pdf.set_font(family="Times", size =24, style="B")
        pdf.cell(w = 0, h = 80, txt = "Flatmates Bill", border=1, align= "C", ln = 1)
        
        # Insert period
        pdf.cell(w=100,h=40, txt = "Period:", border=1)
        pdf.cell(w=150,h=40, txt = bill.period, border=1, ln=1)
        
        # Insert name and due amount of th first flatmate
        pdf.cell(w=100,h=40, txt = flatmate2.name, border=1)
        pdf.cell(w=150,h=40, txt =  str(flatmate2.pays(bill, flatmate)), border=1, ln=1)
            
        # naming a file and save it as a pdf
        pdf.output(self.filename + "_" + bill.period + ".pdf")

    
    
the_bill = Bill(amount=50, period="January 2021")
lennart = Flatmate(name ="Lennart", days_in_house = 30)
adele = Flatmate(name ="Adele", days_in_house = 23)

#print("lennart pays:",lennart.pays(bill = the_bill, flatmate2 = adele))
#print("Adele pays:", adele.pays(bill = the_bill, flatmate2 = lennart))


pdf_generator = PdfGenerator(filename = "report") #Write only filename(Do not write filename.filetype)
pdf_generator.generate(flatmate = lennart, flatmate2 = adele, bill = the_bill)
