from __future__ import annotations
from datetime import datetime
from phonenumbers import PhoneNumber
from typing import Optional
# local
from acorn.v1.datatypes import Address
from acorn.v1.person import Indian


class Patient(Indian):
    def __init__(self,
        id: int,
        uhid: Optional[str] = None,
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
        id: int
            Person's id in the system
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
        uhid: str
            Person's Universal/Unique Health ID
        aadhaar: int
            Aadhaar Number of an Indian
        pan: str
            PAN Number of an Indian
        '''
        super().__init__(name, gender, dob, phone, email, address, aadhaar, pan)
        self._id = id
        self._uhid = uhid

    @property
    def uhid(self) -> Optional[str]:
        return self._uhid

    def __eq__(self, user):
        return self._id == user.id

    def __hash__(self):
        return hash(self._id)
