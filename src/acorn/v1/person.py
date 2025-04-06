from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from phonenumbers import PhoneNumber

from acorn.v1.datatypes import Address


class Person(ABC):
    '''
    Abstract person class for Ayush. All humans in the system have the following attributes.
    Specific classes derived from this abstract classes include User, Personnel, Physician etc.
    - each with their own set of restrictions

    Attributes
    ----------
    name: str
        Name of the person (mutable)
        NOTE: We don't use the often-used anti-pattern of breaking a person's name into first-name, middle-
        name, last-name etc. as it is not a universal format
    phone: PhoneNumber
        Person's phone-number (mutable)

    Properites
    ----------
    name: str
        Gets/sets name
    phone: PhoneNumber
        Gets/sets phone number

    Abstract methods
    ----------------
    def __eq___(Person) -> bool
        Defintion of object equality/equivalence for Person class
    def __hash__()
        Definition of unique object identity
    '''
    def __init__(self, name: str, phone: PhoneNumber):
        '''
        Parameters
        ----------
        name: str
            Person's name
        phone: PhoneNumber
            Person's phonenumber (Google's PhoneNumber class [pypi])
        '''
        self._name = name
        self._phone = phone

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @abstractmethod
    def __eq__(self, person):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()


class VerbosePerson(Person, ABC):
    '''
    Abstract verbose-person class for Ayush. This class contains extra information for the person
    including gender, date-of-birth and address

    Attributes
    ----------
    name: str
        Name of the person (from parent Person class)
    gender: str
        Person's gender (immutable)
    dob: datetime
        Person's date-of-birth (immutable)
        NOTE:
    phone: PhoneNumber
        Person's phone-number (from parent Person class)
    address: Address
        Person's address (mutable)

    Properites
    ----------
    name: str
        Gets/sets name (from parent Person class)
    gender: str
        Gets gender
    dob: datetime
        Gets date-of-birth
    phone: PhoneNumber
        Gets/sets phone number (from parent Person class)
    address: Address
        Gets/sets address
    '''
    def __init__(self, name: str, gender: str, dob: datetime, phone: PhoneNumber, address: Address):
        '''
        Parameters
        ----------
        name: str
            Person's name
        gender: str
            Person's gender
        dob: datetime
            Person's date-of-birth
        phone: PhoneNumber
            Person's phonenumber (Google's PhoneNumber class [pypi])
        address: Address
            Person's address
        '''
        super().__init__(name, phone)
        self._gender = gender
        self._dob = dob
        self._address = address

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def dob(self) -> datetime:
        return self._dob

    @property
    def address(self) -> Address:
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @abstractmethod
    def __eq__(self, person):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()
