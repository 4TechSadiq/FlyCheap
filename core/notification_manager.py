from twilio.rest import Client
import smtplib
import requests

SHEETY2_GET_API = "USER SHEETY API"
SHEETY_KEY = "SHEETY_KEY"

class NotificationManager:
    def __init__(self):
        self.message = None
        self.ssid = "SSID"
        self.auth_token = "AUTH TOKEN"
        self.client = Client(self.ssid, self.auth_token)
        self.mail = "EMAIL"
        self.password = "APP PASSWORD"
        self.header = {
            "Authorization": SHEETY_KEY
        }
        self.response = requests.get(url=SHEETY2_GET_API, headers=self.header)

    def send_message(self,msg):
        self.message = msg
        message = self.client.messages.create(body=self.message, from_="+13344686812", to='+918714094884')
        print(message.sid)

    def send_mail(self, message):
        mail_data = self.response.json()
        mail_list = []
        for i in range(len(mail_data['users'])):
            mail = mail_data['users'][i]['email']
            mail_list.append(mail)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.mail, password=self.password)
            for i in range(len(mail_list)):
                connection.sendmail(from_addr=self.mail,
                                    to_addrs= mail_list[i],
                                    msg=f"Subject:Flycheap!!\n\n{message}"
                                    )

