import time
import datetime
import requests


class Updater:
    session: requests.Session
    url: str = "https://r.onliner.by/sdapi/ak.api/search/apartments"
    params: dict = {
        "price[min]": "50",
        "price[max]": "350",
        "currency": "usd",
        "rent_type[]": "1_room",
        "only_owner": "true",
        "bounds[lb][lat]": "53.70036513128374",
        "bounds[lb][long]": "27.39097595214844",
        "bounds[rt][lat]": "54.09524154586939",
        "bounds[rt][long]": "27.734298706054688",
        "order": "created_at:desc",
        "page": "1",
        "v": "0.2356445485412635",
    }
    cached: list = []
    data: list = []

    def _get_data_json(self) -> list:
        data = []
        response = self.session.get(self.url, params=self.params).json()
        for apartment in response['apartments']:
            data.append(
                Apartment(
                    price=apartment['price']['converted']['USD'],
                    location=apartment['location']['user_address'],
                    photo=apartment['photo'],
                    url=apartment['url']
                )
            )
        return data

    def run(self):
        self.session = requests.Session()

    def update(self):
        self.cached = self.data
        updated_data = self._get_data_json()
        self.data = updated_data
        self._check_update()

    def _check_update(self):
        difference = [
            apartment for apartment
            in self.data
            if apartment.location not in [cached.location for cached in self.cached]
        ]
        if difference and self.cached:
            for apartment in difference:
                apartment.show()
            return
        print(f"No updates at {datetime.datetime.now().strftime('%H:%M:%S')}")


class Apartment:
    price: int
    location: str
    photo: str
    url: str

    def __init__(self, price, location, photo, url):
        self.price = price
        self.location = location
        self.photo = photo
        self.url = url

    def show(self):
        print(f"Location: {self.location}\nPrice: {self.price}\nURL: {self.url}\nPhoto: {self.photo}\n")


if __name__ == '__main__':
    updater = Updater()
    updater.run()
    while True:
        updater.update()
        time.sleep(60)
