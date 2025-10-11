from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from phonenumbers import PhoneNumber
from typing import Optional

from acorn.v1.datatypes import Address


class Person(ABC):
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

    Abstract methods
    ----------------
    def __eq___(Person) -> bool
        Defintion of object equality/equivalence for Person class
    def __hash__()
        Definition of unique object identity
    '''
    def __init__(self,
        name: Optional[str] = None,
        gender: Optional[str] = None,
        dob: Optional[datetime] = None,
        phone: Optional[PhoneNumber] = None,
        email: Optional[str] = None,
        address: Optional[Address] = None):
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
        email: str
            Email-id of a person
        address: Address
            Person's address
        '''
        self._name = name
        self._gender = gender
        self._dob = dob
        self._phone = phone
        self._email = email
        self._address = address

    @property
    def address(self) -> Optional[Address]:
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @property
    def gender(self) -> Optional[str]:
        return self._gender

    @property
    def dob(self) -> Optional[datetime]:
        return self._dob

    @property
    def email(self) -> Optional[str]:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def phone(self) -> Optional[PhoneNumber]:
        return self._phone

    @phone.setter
    def phone(self, phone: PhoneNumber):
        self._phone = phone

    @abstractmethod
    def __eq__(self, person):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()


class Indian(Person, ABC):
    def __init__(self,
        name: Optional[str] = None,
        gender: Optional[str] = None,
        dob: Optional[datetime] = None,
        phone: Optional[PhoneNumber] = None,
        email: Optional[str] = None,
        address: Optional[Address] = None,
        aadhaar: Optional[int] = None,
        pan: Optional[str] = None):
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
        email: str
            Email-id of a person
        address: Address
            Person's address
        aadhaar: int
            Aadhaar Number of an Indian
        pan: str
            PAN Number of an Indian
        '''
        super().__init__(name, gender, dob, phone, email, address)
        self._aadhaar = aadhaar
        self._pan = pan

    @property
    def aadhaar(self) -> Optional[int]:
        return self._aadhaar

    @property
    def pan(self) -> Optional[str]:
        return self._pan

    @abstractmethod
    def __eq__(self, person):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()
