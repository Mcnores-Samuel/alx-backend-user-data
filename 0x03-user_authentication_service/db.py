#!/usr/bin/env python3
"""DB module presenting essertial database operations
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class defition
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creates a new user object and returns the user objects
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """ This method takes in arbitrary keyword arguments and
        returns the first row found in the users table as filtered
        by the method’s input arguments
        """
        schema = ['id', 'email', 'hashed_password',
                  'session_id', 'reset_token']
        form key in kwargs.keys():
            if key not in schema:
                raise InvalidRequestError
        query = self._session(User).filter_by(**kwargs).first()
        if query is None:
            raise NoResultFound
        return query
