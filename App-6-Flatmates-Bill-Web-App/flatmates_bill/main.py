### IMPORTS ###
from flask.views import MethodView
from wtforms import Form
from flask import Flask

# Represent a web app
app = Flask(__name__)

class HomePage(MethodView):
    
    def get(self):
        return "HomePage"
    
class BillformPage(MethodView):
    
    def get(self):
        return "Billform page"


class ResultsPage(MethodView):
    
    def get(self):
        return "This is a result page"

class BillFrom(Form):
    pass


app.add_url_rule('/', view_func= HomePage.as_view("home_page"))
app.add_url_rule('/bill', view_func= BillformPage.as_view("bill_form_page"))
app.add_url_rule('/result', view_func= ResultsPage.as_view("result_page"))


app.run()