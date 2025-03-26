from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    address: str
    city: str
    state: str
    country: str
    pin: str
