import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_from, fly_to, date_from, date_to):
        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.fly_from = fly_from,
        self.fly_to = fly_to,
        self.date_from = date_from,
        self.date_to = date_to,
        self.header = {
        "apikey": "GVIjuPQ8gw5Vt0NWjmmOBZIORMch4A2u",
        }
        self.query = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
        }
        self.response = ""

    def search_flight(self):
        self.response = requests.get(url=self.url, headers=self.header, json=self.query)
        print(self.response.status_code)
        return self.response.json()
