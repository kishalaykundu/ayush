from __future__ import annotations
from phonenumbers import PhoneNumber
from typing import Optional
# local
from acorn.v1.person import Person


class User(Person):
    def __init__(self,
        id: int,
        user_id: Optional[int] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[PhoneNumber] = None):
        super().__init__(name=name, email=email, phone=phone)
        self._id = id
        self._userid = user_id
        self._password = password

    @property
    def id(self) -> int:
        return self._id

    def __eq__(self, user):
        return self._id == user.id

    def __hash__(self):
        return hash(self._id)
