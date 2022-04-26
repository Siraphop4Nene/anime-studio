import create as c
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class DAOFactory:
    def __init__(self):
        self.engine = create_engine('sqlite:///anime-studio.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.dao = DAO(self.session)


class DAO:

    def __init__(self, session):
        self.session = session

    def get_all_animes(self):
        return self.session.query(c.Anime).all()

    def get_anime_by_id(self, id):
        return self.session.query(c.Anime).filter_by(id=id).first()

    def get_anime_by_name(self, name):
        return self.session.query(c.Anime).filter_by(name=name).first()

    def get_anime_by_episode(self, episode):
        return self.session.query(c.Anime).filter_by(episode=episode).first()

    def get_studios(self):
        return self.session.query(c.Studio).all()

    def get_studio_by_id(self, id):
        return self.session.query(c.Studio).filter_by(id=id).first()

    def get_studio_by_name(self, name):
        return self.session.query(c.Studio).filter_by(name=name).first()

    def get_anime_by_studio_id(self, studio_id):
        return self.session.query(c.Anime).filter_by(studio_id=studio_id).all()

    def get_anime_by_studio_name(self, studio_name):
        return self.session.query(c.Anime).filter_by(studio_name=studio_name).all()

    def get_anime_by_studio_name_and_episode(self, studio_name, episode):
        return self.session.query(c.Anime).filter_by(studio_name=studio_name, episode=episode).first()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def add_anime(self, anime):
        self.session.add(anime)
        self.commit()

    def add_studio(self, studio):
        self.session.add(studio)
        self.commit()

    def delete_anime(self, anime):
        self.session.delete(anime)
        self.commit()

    def delete_studio(self, studio):
        self.session.delete(studio)
        self.commit()

    def update_anime(self, anime):
        self.session.merge(anime)
        self.commit()

    def update_studio(self, studio):
        self.session.merge(studio)
        self.commit()

