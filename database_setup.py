from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }


class Game(Base):
    __tablename__ = 'game'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(300))
    developed_by = Column(String(100))
    published_by = Column(String(100))
    release_year = Column(String(4))
    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date_added = Column(DateTime, nullable=False)
    genre = relationship('Genre', backref=backref('game', order_by=id))
    user = relationship('User', backref=backref('game', order_by=id))

    @property
    def serialize(self):
        return {
            'title': self.name,
            'id': self.id,
            'description': self.description,
            'developed by': self.developed_by,
            'published by': self.published_by,
            'released on': self.release_year
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

engine = create_engine('sqlite:///videogame.db')
Base.metadata.create_all(engine)
