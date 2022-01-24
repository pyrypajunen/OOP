### IMPORTS ###
from webapp.layout import Layout
from webapp.page import Page
import justpy as jp

class About(Page):
    """comment here
    """
    path = "/about"
    
    def serve(self):
       wp = jp.QuasarPage(tailwind=True)
       
       lay = Layout(a=wp)
       
       container = jp.QPageContainer(a=lay)
       
       div = jp.Div(a=container, classes = "bg-gray-200 h-screen")
       jp.Div(a=div, text = "This is the about page!", 
              classes = "text-4xl m-2")
       jp.Div(a=div, text = """This page could include information on the page,
              but it is empty..
              """, classes="text-lg")

       return wp

    