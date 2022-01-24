### IMPORTS ###
from cgitb import text
import justpy as jp


class Home:
    """Home page created by Quasars' layouts
    """
    path = "/"

    @classmethod
    def serve(cls, req):
       wp = jp.QuasarPage(tailwind=True)
       
       layout = jp.QLayout(a=wp ,view="hHh lpR fFf")
       header = jp.QHeader(a=layout)
       toolbar = jp.QToolbar(a=header)
       jp.QHeader(a=layout)
       
       # drawer represen menubar
       drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode = "left",
                           bordered = True)
       
       scroller = jp.QScrollArea(a=drawer, classes = "fit")
       qlist = jp.QList(a = scroller)
       a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
       jp.A(a= qlist, text = "Home", href = "/", classes = a_classes)
       jp.Br(a= qlist)
       jp.A(a= qlist, text = "Dictionary", href = "/dictionary", classes = a_classes)
       jp.Br(a= qlist)
       jp.A(a= qlist, text = "About", href = "/about", classes = a_classes)
       
       
       
       jp.QBtn(a= toolbar,dense=True, flat=True, icon="menu", click= cls.move_drawer,
              drawer = drawer)
       
       jp.QToolbarTitle(a=toolbar , text= "Instant Dictionary")
       
       container = jp.QPageContainer(a=layout)
       
       div = jp.Div(a=container, classes = "bg-gray-200 h-screen p-2")
       jp.Div(a=div, text = "This is the about page!", 
              classes = "text-4xl m-2")
       jp.Div(a=div, text = """ text text text text text text text text text
               text HomePage
               text
              """, classes="text-lg")
       return wp

    @staticmethod
    def move_drawer(widget, msg):
       if widget.drawer.value:
              widget.drawer.value = False
       else:
              widget.drawer.value = True
    
