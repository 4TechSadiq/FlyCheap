import requests
from datetime import datetime, timedelta

API_END = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "IzofUYaxSREl126TSviC_eiVn9Lj6y8E"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, flyfrom: str, flyto: str, price: int):
        self.head = {
            "apikey": API_KEY,
        }
        self.price_dict = {}
        self.datefrom = datetime.today().date().strftime("%d/%m/%Y")
        self.dateto = datetime.now().date() + timedelta(days=30 * 6)
        self.params = {
            "fly_from": flyfrom,
            "fly_to": flyto,
            "date_from": self.datefrom,
            "date_to": self.dateto,
            "price_to": price
        }

    def search_flight(self):
        response = requests.get(url=API_END, headers=self.head, params=self.params)
        dict1 = response.json()
        if response.status_code == 200:
            try:
                if "data" in dict1:
                    data_list = dict1["data"]
                    for flight in range(len(dict1)):
                        self.price_dict[flight] = {
                            "dateFrom": self.datefrom,
                            "dateTo": self.dateto.strftime("%d/%m/%Y"),
                            "price": data_list[flight]["price"],
                            "flyfrom": data_list[flight]["cityFrom"],
                            "flyfromcode": data_list[flight]["cityCodeFrom"],
                            "flyto": data_list[flight]["cityTo"],
                            "flytocode": data_list[flight]["cityCodeTo"],

                        }
                        return self.price_dict
            except IndexError:
                if "data" in dict1:
                    data_list = dict1["data"]
                    if len(data_list) == 0:
                        return "There are no flights available"

