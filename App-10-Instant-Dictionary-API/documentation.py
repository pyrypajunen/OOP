### IMPORTS ###
import justpy as jp

class Documentation:
    """Documentation page.
    """
    
    def serve(self):
       wp = jp.WebPage()
       
       div = jp.Div(a=wp, classes = "bg-gray-200 h-screen")
       jp.Div(a=div, text = "Instant Dictionary API Documentation", 
              classes = "text-4xl m-2")
       jp.Div(a=div, text = """
              Get definitions of words:
              """, classes="text-lg")
       jp.Hr(a=div)
       jp.Div(a = div, text = "www.example.com/api?w=word")
       jp.Hr(a=div)
       jp.Div(a=div, text = """
        {"word": "acid", "definition": ["A compound capable of transferring a hydrogen ion in solution.", 
        "Being harsh or corrosive in tone.", "Having an acid, sharp or tangy taste.", 
        "A powerful hallucinogenic drug manufactured from lysergic acid.",
        "Having a pH less than 7, or being sour, or having the strength to neutralize alkalis, 
        or turning a litmus paper red."]}  
        """)

       return wp

    