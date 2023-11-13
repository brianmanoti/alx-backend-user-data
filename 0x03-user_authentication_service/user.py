#!/usr/bin/env python3
"""
in This Module We are Going to create a class user to represent
a table in sqlalchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, integer, string

Base = declarative_base()

class User:
    """ The class user to represent our user table """
    __tablename__ = 'users'

    id = Column(integer, primary_key=True)
    email = Column(string(250), nullable=False)
    hashed_password = Column(string(250), nullable=False)
    session_id = Column(string(250), nullable=True)
    reset_token = column(string, nullable=True)

    def __repr__(self):
        """
        String Rep
        """
        return f"User: id={self.id}"
