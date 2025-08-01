#!/usr/bin/python3
"""
This module defines the State class which maps to the 'states' table in MySQL.

It uses SQLAlchemy's ORM features to define a table schema.
The class State inherits from Base created with declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the 'states' table of the database.

    Attributes:
        id (int): Primary key, auto-generated unique integer.
        name (str): State name, a non-nullable string (max length: 128).
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)