from typing import List, Union
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import CONNECTION_STRING


engine = create_engine(CONNECTION_STRING)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = Session()


class DBException(Exception):
    def __init__(self, message):
        super().__init__(message)


class User(Base):
    '''Model for user'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    @staticmethod
    def get_by_name(name: str) -> 'User':
        user = session.query(User).filter(User.name == name).first()
        return user

    @staticmethod
    def new(login: str, name: str, last_name: str, password: str) -> 'User':
        user = User(login=login, name=name, last_name=last_name, password=password)
        session.add(user)
        session.commit()
        return user

    def update(self, **kwargs) -> 'User':
        for attr in kwargs:
            if not getattr(self, attr, None):
                raise DBException(message="invalid attribute")
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.add(self)
        session.commit()
        return self

    def delete(self) -> 'User':
        session.delete(self)
        session.commit()
        return self

    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'name': self.name,
            'last_name': self.last_name,
        }


def drop_all():
    Base.metadata.drop_all(bind=engine)


def create_all():
    Base.metadata.create_all(bind=engine)
    User.new('admin', 'admin', 'admin', 'admin')
    User.new('ivan.petrov', 'Ivan', 'Petrov', 'qwerty')
    User.new('petr.ivanov', 'Petr', 'Ivanov', 'qwerty')


if __name__ == '__main__':
    create_all()
