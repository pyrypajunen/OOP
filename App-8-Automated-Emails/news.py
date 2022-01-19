### import ###
import requests
from pprint import pprint
# API Key: 9a551ad259da4b8daff3011be7314353

        
class NewsFeed:
    """Representing multiple news title and links as a single string
    """
    base_url = 'http://https://newsapi.org/v2/everything?'
    api_key = '9a551ad259da4b8daff3011be7314353'
    
    def __init__(self, interest,from_date, to_date, language = 'en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        
    def get(self):
        url = self._build_url()
        
        articles = self._get_articles(url)
        
        the_new = self._email_body(articles)
        
        return the_new
    
    def _build_url(self):
        """Build url for requesting news from API
        """
        url = f"https://newsapi.org/v2/everything?" \
            f"qInTitle={self.interest}&" \
            f"from={self.from_date}&" \
            f"to={self.to_date}&" \
            f"language={self.language}&" \
            f"apiKey={self.api_key}"  
        return url  
    
    def _get_articles(self, url):
        """Request article from news API
        """
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles
    
    def _email_body(self,articles):
        """Creating email body
        """
        email_body = ""
        for article in articles: # -> list of dicts
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
    
        return email_body
        
    

if __name__ == '__main__':
    news_feed = NewsFeed(interest="nasa", from_date="2022-11-1", to_date="2022-11-1", language="en")
    print(news_feed.get())