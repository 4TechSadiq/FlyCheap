from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.message = None
        self.ssid = "[YOUR SSID]"
        self.auth_token = "[AUTH_TOKEN]"
        self.client = Client(self.ssid, self.auth_token)

    def send_message(self,msg):
        self.message = msg #Message to be sent
        message = self.client.messages.create(body=self.message, from_="[TWILIO NUMBER]", to='[RECIEVER NUMBER]')

        print(message.sid)

