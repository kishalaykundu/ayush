from __future__ import annotations
from typing import List, Optional
# local
from acorn.t1.staff import Employee


class Department():
    def __init__(self,
        id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        head: Optional[Employee] = None,
        deputies: Optional[List[Employee]] = None):
        self._id = id
        self._name = name
        self._desc = description
        self._head = head
        self._deputies = deputies
