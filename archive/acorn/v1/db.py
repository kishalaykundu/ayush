from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class DB(Generic[T], ABC):
    '''
    Abstract implementation of the Repository pattern in Ayush
    This is the base class from which abstract repository pattern
    of specific types are implemented.

    Abstract methods (mandatory)
    ----------------------------
    def add(record) -> T
        Adds record to corpus and returns record object
    def get(reference) -> Optional[T]
        Gets object by reference
    def get_many(**filters) -> List[T]
        Gets list of objects based on filtering criteria
    def invalidate(reference)
        Deletes records from corpus (in Ayush pattern followed is cancel/invalidate)
    def modify(record) -> T
        Modifies/updates a record and returns changed object

    Abstract methods (optional)
    ---------------------------
    def add_many(records) -> List[T]
        Adds multiple records in bulk and returns added list
    def modify_many(records) -> List[T]
        Modify multiple records in bulk and returns modified list

    Concrete method
    ---------------
    def delete(reference)
        Calls invalidate function
    '''
    @abstractmethod
    def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def add_many(self, records: List[T]) -> List[T]:
        pass

    @abstractmethod
    def get(self, reference) -> Optional[T]:
        raise NotImplementedError()

    @abstractmethod
    def get_many(self, **filters) -> List[T]:
        raise NotImplementedError()

    @abstractmethod
    def invalidate(self, reference) -> None:
        raise NotImplementedError()

    @abstractmethod
    def modify(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    def modify_many(self, records: List[T]) -> List[T]:
        pass

    def delete(self, reference) -> None:
        self.invalidate(reference)
