from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Address:
    '''
    Address dataclass for the Ayush module. Immutable type

    Attributes
    ----------
    address: str
        eg. "1313 Mockingbird Lane, Bristol County"
    city: str
        eg. "Gotham City" (enum-style restricted-string list)
    state: str
        eg. "New York" (enum-style restricted-string list)
    country: str
        eg. "USA" (enum-style restricted-string list)
    area_code: str
        eg. "10001" (restricted-string list - string type allows for different postal area-code schemes)

    Notes
    -----
    Field-level restrictions should be enforced at the usage level (modules that use this class).
    '''
    address: str
    city: str
    state: str
    country: str
    area_code: str


@dataclass
class Price:
    '''
    Price dataclass for the Ayush module. Immutable type

    Attributes
    ----------
    currency: str
        eg. "INR" (enum-style restricted-string list)
    amount: Decimal
        eg. 1000.05
    '''
    currency: str
    amount: Decimal
