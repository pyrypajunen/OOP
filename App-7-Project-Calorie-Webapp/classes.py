### IMPORTS ###
import requests
from pprint import pprint
from selectorlib import Extractor



class Calorie:
    """ 
    Represent amount of the calories in calcuated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
    
    def calculate(self):
        result = 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*self.temperature
        return result
    

class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/wather webpage.
    """
    
    yaml_file = r'App-7-Project-Calorie-Webapp/temperature.yaml'
    web_url = r"https://www.timeanddate.com/weather/"
    
    def __init__(self, country, city):
        self.country = country
        self.city = city
        
    def _build_url(self):
        
        web_url = self.web_url + self.country + "/" + self.city
        return web_url
        
    def _scrape(self):
        """
        Web scraping part
        """
        url = self._build_url()
        re = requests.get(url)
        con = re.text # This is a source code of the webpage
        
        extractor = Extractor.from_yaml_file(self.yaml_file)
        raw_result = extractor.extract(con)
        return raw_result
        
    def get(self):
        """
        Cleans the output of _scrape
        """
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("\xa0°C", ""))
    
    
### User inputs ###

    
if __name__ == '__main__':   
    country = input("Which country? ")
    city = input("Which city? ")
    weight = float(input("Weight? "))
    height = float(input("Height? "))
    age = int(input("Age? "))


            
    temperature = Temperature(city=city, country=country).get()
    calorie = Calorie(weight=weight, height=height, age=age, temperature=temperature)
    print("Total calorie:", calorie.calculate())
