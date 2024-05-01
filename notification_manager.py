from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.message = None
        self.ssid = "AC5f11824449fc6d3a719462d3fd22dd84"
        self.auth_token = "6f42c3a1bed99147ae422b0a65c8673d"
        self.client = Client(self.ssid, self.auth_token)

    def send_message(self,msg):
        self.message = msg
        message = self.client.messages.create(body=self.message, from_="+13344686812", to='+918714094884')

        print(message.sid)

