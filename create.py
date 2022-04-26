from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///anime-studio.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Studio(Base):
    __tablename__ = 'studio'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'ID = {self.id}, Name = {self.name}'


class Anime(Base):
    __tablename__ = 'anime'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    studio_id = Column(Integer, ForeignKey('studio.id'))
    ep = Column(Integer)

    def __repr__(self):
        return f'ID = {self.id}, Name = {self.name}, Studio = {self.studio_id}, Ep = {self.ep}'


Base.metadata.create_all(engine)
with open('data/studio.csv', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        studio = Studio(name=line[1])
        session.add(studio)
with open('data/anime.csv', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        anime = Anime(name=line[1], studio_id=int(line[2]), ep=int(line[3]))
        session.add(anime)
session.commit()
