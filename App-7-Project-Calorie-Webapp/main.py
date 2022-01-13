from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from classes import Calorie, Temperature

# Represent a web app
app = Flask(__name__)


class HomePage(MethodView):
    """Create the HomePage view."""
    def get(self):
        return render_template("index.html")


class CalculatorPage(MethodView):
    """Create the CalculatorPage view"""
    
    def get(self):
        # Return the HTML template
        calories_form = CalculatorForm()
        return render_template("calories_form_page.html", caloriesform=calories_form)
        
    def post(self):
        """Sending user input data by post method into the form.
        """
        calories_form = CalculatorForm(request.form)
        temperature = Temperature(country = calories_form.country.data,
                                  city = calories_form.city.data).get()
        
        calorie = Calorie(weight = float(calories_form.weight.data),
                            height = float(calories_form.height.data),
                            age = float(calories_form.age.data),
                            temperature= temperature)
        
        calories = calorie.calculate()
        return render_template("calories_form_page.html",
                               caloriesform=calories_form,
                               calories=calories,
                               result = True)
    

class CalculatorForm(Form):
    """These represent the user inputs"""
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")
    city = StringField("City: ")
    country = StringField("Country: ")
    button = SubmitField("Calculate: ")
        

# Adoption of the pages
app.add_url_rule("/",
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form",
                 view_func = CalculatorPage.as_view("calories_form_page"))

app.run(debug=True)