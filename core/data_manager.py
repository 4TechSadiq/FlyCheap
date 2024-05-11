import requests
import json

SHEETY_GET_API = ""SHEETY API TO GET""
SHEETY_POST_API = ""SHEETY API TO POST""
SHEETY_PUT_API = ""SHEETY API TO PUT""
SHEET2_POST_API = ""SHEETY API TO POST""
SHEET2_POST_KEY = ""SHEETY API KEY ""

class DataManager:
    def __init__(self):
        self.data = None
        self.post = None
        self.params = None
        self.add = None
        self.header = {
            "Authorization": SHEET2_POST_KEY
        }
        self.response = requests.get(url=SHEETY_GET_API, headers=self.header)

    def get_city(self):
        """Get the city name from the response json."""
        data_dict = self.response.json()
        price_list = data_dict['prices']
        city_list = [price_list[citi]['city'] for citi in range(0, len(price_list))]
        return city_list

    def get_price(self):
        """Get the expected price from the response json."""
        data_dict = self.response.json()
        price_list = data_dict.get('prices', [])
        low_price = []
        for price_info in price_list:
            lowest_price = price_info.get('lowestPrice')  # Use .get() to handle missing 'lowestPrice' key
            if lowest_price is not None:
                low_price.append(lowest_price)
        return low_price

    def get_iata(self):
        """Get the city IATA code from the response json."""
        data_dict = self.response.json()
        price_list = data_dict['prices']
        iata_list =[]
        for index in range(0, len(price_list)):
            iata = price_list[index].get('iataCode')
            iata_list.append(iata)

        return iata_list

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
        print(self.add.status_code)
        return self.add.status_code

    def insert_userinfo(self,f_name, l_name, email):
        self.data = {
            "user": {
                "first": f_name,
                "last": l_name,
                "email": email
                }

        }
        self.post = requests.post(url=SHEET2_POST_API, json=self.data, headers=self.header)
        return self.post.status_code

    def start(self):
        print("Welcome to FlyCheap.\nWe find the best flight deals and emails you.")
        fname = input("What is your first name?\n")
        lname = input("What is your last name?\n")
        email = input("What is your email?\n")
        e2mail = input("Enter email again.\n")
        if email == e2mail:
            status_code = self.insert_userinfo(f_name=fname, l_name=lname, email=email)
            if status_code == 200:
                print("You're in")


