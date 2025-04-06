from __future__ import annotations
from phonenumbers import PhoneNumber
# local
from acorn.v1.person import Person


class User(Person):
    def __init__(self, id: int, name: str, phone: PhoneNumber):
        super().__init__(name, phone)
        self._id = id

    @property
    def id(self) -> int:
        return self._id

    def __eq__(self, user):
        return self._id == user.id

    def __hash__(self):
        return hash(id)


class UserWithEmail(User):
    def __init__(self, id: int, name: str, phone: PhoneNumber, email: str):
        super().__init__(id, name, phone)
        self._email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
