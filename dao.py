import create as model
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DAOFactory:
    def __init__(self):
        self.engine = create_engine('sqlite:///anime-studio.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.dao = DAO(self.session)

    def get_dao(self):
        return self.dao


class DAO:

    def __init__(self, session):
        self.session = session

    def get_all_anime(self):
        return self.session.query(model.Anime).all()

    def get_anime_by_id(self, id):
        return self.session.query(model.Anime).filter_by(id=id).first()

    def get_anime_by_name(self, name):
        return self.session.query(model.Anime).filter_by(name=name).first()

    def get_all_studios(self):
        return self.session.query(model.Studio).all()

    def get_studio_by_id(self, id):
        return self.session.query(model.Studio).filter_by(id=id).first()

    def get_studio_by_name(self, name):
        return self.session.query(model.Studio).filter_by(name=name).first()

    def commit(self):
        self.session.commit()

    def update_anime(self, anime, id, name, studio_id, episodes):
        anime.id = id
        anime.name = name
        anime.studio_id = studio_id
        anime.ep = episodes

    def update_studio(self, studio, id, name):
        studio.id = id
        studio.name = name

    def add_anime(self, id, name, studio_id, episodes):
        anime = model.Anime(id, name, studio_id, episodes)
        self.session.add(anime)

    def add_studio(self, id, name):
        studio = model.Studio(id, name)
        self.session.add(studio)
