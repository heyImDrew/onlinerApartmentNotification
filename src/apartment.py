from datetime import datetime

from src.printstyle import PrintStyle


class Apartment:
    price: int
    location: str
    url: str
    created_at: datetime

    def __init__(self, created_at, price, location, url):
        self.created_at = created_at
        self.price = price
        self.location = location
        self.url = url

    def show(self):
        print(
            f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}Location: {PrintStyle.ENDC}"
            f"{self.location}\n"
            f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}Price: {PrintStyle.ENDC}"
            f"{self.price} USD\n"
            f"{PrintStyle.OKGREEN}{PrintStyle.BOLD}URL: {PrintStyle.ENDC}"
            f"{self.url}"
            f"{PrintStyle.ENDC}"
        )
