### IMPORTS ###
import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time



user = "kurssipyyttoni@gmail.com"
password = 'Sanako996!"' # Test account, so GDPR is not required.


def send_email():
    """Function to send emails for subscribers daily."
    """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            
    news_feed = NewsFeed(interest = row["interest"], 
                        from_date= yesterday.strftime("%Y-%m-%d"), 
                        to_date= today)
                   
    email = yagmail.SMTP(user=user, password=password)
    email.send(to=row["email"],
                    subject= f" Your {row['interest']} news for today!",
                    contents= f"Hi {row['name']} \n\n See what's on about {row['interest']} today. {news_feed.get()}\n Regards, \nPyry")

while True:
    if datetime.datetime.now().hour == 14 and datetime.datetime.now().minute == 33:
        print("Executing!")
        dataframe = pd.read_excel(r"App-8-Automated-Emails/people.xlsx")

        for index, row in dataframe.iterrows():
            send_email()
    time.sleep(60)
          
