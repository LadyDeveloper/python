#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch

flight = FlightSearch(fly_from="LAS", fly_to="SAO", date_from="01/18/2021", date_to="01/22/2021")
flight.search_flight()