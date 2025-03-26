from __future__ import annotations
from admin.src.models.v1.tenant import Tenant
from core.models.v1.address import Address


class Organization:
    def __init__(self, oid: str, address: Address, tenant: Tenant):
        self.id = oid
        self.address = address
        self.tenants = [tenant, ]

    def __eq__(self, other):
        if not isinstance(other, Tenant):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)

    def add_tenant(self, tenant: Tenant):
        exists = next((i for i in self.tenants if i == tenant), None)
        if exists is None:
            self.tenants.append(tenant)
