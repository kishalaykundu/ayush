from __future__ import annotations
from core.models.v1.address import Address


class Tenant:
    def __init__(self, tid: str, name: str, address: Address):
        self.id = tid
        self.name = name
        self.address = address
        self.services = list()

    def __eq__(self, other):
        if not isinstance(other, Tenant):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    def add_service(self, service: Service):
        exists = next((i for i in self.services if i == service), None)
        if exists is None:
            self.tenants.append(service)
