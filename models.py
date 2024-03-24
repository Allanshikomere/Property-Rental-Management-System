from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    rent = Column(Integer)
    tenant_id = Column(Integer, ForeignKey('tenants.id'))

    def __repr__(self):
        return f"<Property(address='{self.address}', rent={self.rent})>"

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))

    def __repr__(self):
        return f"<Tenant(name='{self.name}')>"

class UnderConstructionProperty(Base):
    __tablename__ = 'under_construction_properties'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<UnderConstructionProperty(name='{self.name}')>"