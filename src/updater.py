from datetime import datetime, timedelta

import requests

from src.apartment import Apartment
from src.base import datetime_differ
from src.input import get_user_input


class Updater:
    session: requests.Session
    url: str = "https://r.onliner.by/sdapi/ak.api/search/apartments"
    params: dict = {
        "currency": "usd",
        "rent_type[]": "1_room",
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
    delay: int = 60

    def _get_data_json(self) -> list:
        data = []
        response = self.session.get(self.url, params=self.params).json()
        for apartment in response['apartments']:
            data.append(
                Apartment(
                    created_at=datetime.strptime(apartment['created_at'][:-5], "%Y-%m-%dT%H:%M:%S"),
                    price=apartment['price']['amount'],
                    location=apartment['location']['user_address'],
                    url=apartment['url']
                )
            )
        return data

    def load_settings(self):
        data = get_user_input()
        self.delay = data.pop('delay')
        self.params.update(data)

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
                if datetime_differ(apartment.created_at, self.delay * 2):
                    continue
                print("Update found!")
                apartment.show()
            return
        print(f"No updates at {datetime.now().strftime('%H:%M:%S')}")
