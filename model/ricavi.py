from dataclasses import dataclass
from datetime import date


@dataclass
class Ricavi:
    data: date
    ricavo: float
    retailer: str
    prodotto: int

    def __eq__(self, other):
        return self.ricavo == other.ricavo

    def __lt__(self, other):
        return self.ricavo < other.ricavo

    def __str__(self):
        return f"Data: {self.data}; Ricavo: {self.ricavo}; Retailer: {self.retailer}; Product: {self.prodotto}"