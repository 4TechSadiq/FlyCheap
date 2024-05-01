import requests

SHEETY_GET_API = "SHEETY API TO GET"
SHEETY_POST_API = "SHEETY API TO POST"
SHEETY_PUT_API = "SHEETY API TO PUT/UPDATE"


class DataManager:
    def __init__(self):
        self.params = None
        self.add = None
        self.response = requests.get(url=SHEETY_GET_API)

    def get_city(self):
        """Get the city name from the response json."""
        data_dict = self.response.json()
        price_list = data_dict['prices']
        city_list = [price_list[citi]['city'] for citi in range(0, len(price_list))]
        return city_list

    def get_price(self):
        """Get the expected price from the response json."""
        data_dict = self.response.json()
        price_list = data_dict['prices']
        low_price = [price_list[citi]['lowestPrice'] for citi in range(0, len(price_list))]
        return low_price

    def get_iata(self):
        """Get the city IATA code from the response json."""
        data_dict = self.response.json()
        price_list = data_dict['prices']
        iata_code = [price_list[citi]['iataCode'] for citi in range(0, len(price_list))]
        return iata_code

    def insert(self, city: str, code: str, price: float):
        """Used to add new city to google sheet."""
        self.params = {
            "price": {
                "city": city,
                "iata code": code,
                "lowest price": price
            }
        }
        self.add = requests.post(url=SHEETY_POST_API, json=self.params)
        return self.add.status_code


