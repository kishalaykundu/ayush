from __future__ import annotations
from phonenumbers import PhoneNumber
from typing import List, Optional
# local
from acorn.v1.person import Person


class Employee(Person):
    def __init__(self,
        id: int,
        eid: int,  # employee id
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[PhoneNumber] = None):
        super().__init__(name=name, email=email, phone=phone)
        self._id = id
        self._eid = eid

    @property
    def id(self) -> int:
        return self._id

    @property
    def eid(self) -> int:
        return self._eid

    @eid.setter
    def eid(self, eid: int):
        self._eid = eid


class Physician(Employee):
    def __init__(self,
        id: int,
        eid: int,
        dids: Optional[List[int]] = None,  # department id
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[PhoneNumber] = None,
        degrees: Optional[List[str]] = None):
        super().__init__(id=id, eid=eid, name=name, email=email, phone=phone)
        self._degrees = degrees
        self._departments = dids

    @property
    def degrees(self) -> Optional[List[str]]:
        return self._degrees

    @degrees.setter
    def degrees(self, degrees: List[str]):
        self._degrees = degrees

    def add_degree(self, degree: str):
        if not self._degrees:
            self._degrees = [degree,]
        elif degree not in self._degrees:
            self._degrees.append(degree)
