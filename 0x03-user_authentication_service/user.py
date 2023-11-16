#!/usr/bin/env python3
""" Creating A User Table In SQLAlchemy """

from sqlalchemy import column, integer, string

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
