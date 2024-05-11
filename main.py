from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager


datamanager = DataManager()
city_list = datamanager.get_city()
price_list = DataManager().get_price()
iata_code = DataManager().get_iata()

datamanager.start()

flyfrom= input("enter iata code : ")
flyprice = int(input("enter max price : "))
message = "Low price alert!!\n\n"
for index in range(0, len(city_list)):
    flight = FlightSearch(flyfrom=flyfrom, flyto=iata_code[index], price=flyprice)
    flight_datah = flight.search_flight()

    message += f"{index}) ${flight_datah[0].get('price')} to fly from {flight_datah[0].get('flyfrom')} to {flight_datah[0].get('flyto')} from {flight_datah[0].get('dateFrom')} to {flight_datah[0].get('dateTo')}.\n"

NotificationManager().send_mail(message=message)
