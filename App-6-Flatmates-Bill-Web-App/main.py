### IMPORTS ###
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat


# Represent a web app
app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')
    
class BillformPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform= bill_form)
    



class ResultsPage(MethodView):
    
    def post(self):
        billform = BillForm(request.form) # object instance for billform
        amount = float(billform.amount.data) # data is the user input
        period = billform.period.data 
        
        the_bill = flat.Bill(amount=amount, period=period)
        
        # Person1 name and days_in_house
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        # Person2 name and days_in_house
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))
        
        return render_template('results.html', 
                               name1 = flatmate1.name,
                               amount1 = round(flatmate1.pays(the_bill, flatmate2)),
                               name2 = flatmate2.name,
                               amount2 = round(flatmate2.pays(the_bill,flatmate1)))

class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    
    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")
    
    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house")
    
    button = SubmitField("Calculate:")
    


app.add_url_rule('/', 
                 view_func= HomePage.as_view("home_page"))
app.add_url_rule('/bill_form', 
                 view_func= BillformPage.as_view("bill_form_page"))
app.add_url_rule('/results', 
                 view_func= ResultsPage.as_view("result_page"))


app.run(debug=True)