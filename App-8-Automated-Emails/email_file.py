### IMPORTS ###
import yagmail
import getpass

user = "kurssipyyttoni@gmail.com"
password = 'Sanako996!"'

email = yagmail.SMTP(user=user, password=password)
email.send(to="ewzbhmknzsfr@dropmail.me",
           subject="Hi there",
           contents="Hi, this is the body",)
