from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Task(Generic[T], ABC):
    '''
    Abstract unit of work pattern that bridges the repository layer and the service layer.
    This is an abstraction of abstract classes to join concrete repository to conrete service.
    '''
    def __init__(self, db: T):
        self._db = db

    @abstractmethod
    def db(self) -> T:
        return self._db

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()
