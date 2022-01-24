### IMPORTS ###
import justpy as jp
from webapp.layout import Layout
from webapp.page import Page

class Home(Page):
    """Home page created by Quasars' layouts
    """
    path = "/"

    @classmethod
    def serve(cls, req):
       wp = jp.QuasarPage(tailwind=True)
       
       lay = Layout(a=wp)
       
       container = jp.QPageContainer(a=lay)
       
       div = jp.Div(a=container, classes = "bg-gray-200 h-screen p-2")
       jp.Div(a=div, text = "Welcome to the Instant Dictionary!", 
              classes = "text-4xl m-2")
       jp.Div(a=div, text = """Get any definition of the word! Just type it!! 
              """, classes="text-lg")
       return wp
    
